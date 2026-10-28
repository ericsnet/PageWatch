#!/usr/bin/env python3
"""Local PageWatch service. Browser UI remains static and can also be hosted on GitHub Pages."""
from __future__ import annotations
import hashlib, json, os, re, sqlite3, threading, time
from datetime import datetime, timezone
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from urllib.error import HTTPError, URLError
from urllib.parse import urlparse
from urllib.request import Request, urlopen

ROOT = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(ROOT, "pagewatch.db")
HOST, PORT = "127.0.0.1", int(os.environ.get("PAGEWATCH_PORT", "8765"))
ALLOWED_ORIGINS = {"https://ericsnet.github.io", "http://127.0.0.1:8765", "http://localhost:8765"}
USER_AGENT = "PageWatch/0.1 (+local page-change monitor)"
def now(): return datetime.now(timezone.utc).isoformat(timespec="seconds")
def connect():
    db = sqlite3.connect(DB_PATH, timeout=10)
    db.row_factory = sqlite3.Row
    db.execute("""CREATE TABLE IF NOT EXISTS monitors (id TEXT PRIMARY KEY, name TEXT NOT NULL, url TEXT NOT NULL UNIQUE, created_at TEXT NOT NULL, last_checked TEXT, content_hash TEXT, last_changed TEXT, last_error TEXT, interval_minutes INTEGER NOT NULL DEFAULT 60)""")
    db.execute("""CREATE TABLE IF NOT EXISTS history (id INTEGER PRIMARY KEY AUTOINCREMENT, monitor_id TEXT, name TEXT NOT NULL, url TEXT NOT NULL, message TEXT NOT NULL, kind TEXT NOT NULL, created_at TEXT NOT NULL)""")
    return db
def valid_url(value):
    p=urlparse(value or "")
    return p.scheme in ("http","https") and bool(p.hostname) and not any(c in value for c in "\r\n")
def fetch_page(url):
    if not valid_url(url): raise ValueError("Only valid http and https URLs are supported")
    request=Request(url,headers={"User-Agent":USER_AGENT,"Accept":"text/html,application/xhtml+xml,text/plain;q=0.9,*/*;q=0.5"})
    with urlopen(request,timeout=15) as response:
        final=response.geturl()
        if not valid_url(final): raise ValueError("Unsafe redirect destination")
        raw=response.read(3_000_000)
        content_type=response.headers.get("Content-Type","")
        charset=response.headers.get_content_charset() or "utf-8"
    if "html" in content_type.lower():
        text=raw.decode(charset,errors="replace")
        text=re.sub(r"(?is)<(script|style|noscript|svg)\b[^>]*>.*?</\1\s*>"," ",text)
        text=re.sub(r"(?s)<!--.*?-->"," ",text)
        text=re.sub(r"(?s)<[^>]+>"," ",text)
        text=re.sub(r"&nbsp;"," ",text,flags=re.I)
        text=re.sub(r"&amp;","&",text,flags=re.I)
        text=re.sub(r"\s+"," ",text).strip()
    else: text=raw.decode(charset,errors="replace").strip()
    if not text: raise ValueError("The page returned no readable text")
    return text[:1_000_000]
def digest(text): return hashlib.sha256(text.encode("utf-8",errors="replace")).hexdigest()
def add_event(db, monitor_id, name, url, message, kind):
    db.execute("INSERT INTO history(monitor_id,name,url,message,kind,created_at) VALUES(?,?,?,?,?,?)",(monitor_id,name,url,message,kind,now()))
def check_one(db, row):
    checked=now()
    try:
        content=fetch_page(row["url"]); new_hash=digest(content)
        changed=bool(row["content_hash"] and row["content_hash"] != new_hash)
        if not row["content_hash"]: add_event(db,row["id"],row["name"],row["url"],"Initial snapshot saved","info")
        elif changed:
            db.execute("UPDATE monitors SET last_changed=? WHERE id=?",(checked,row["id"]))
            add_event(db,row["id"],row["name"],row["url"],"Page content changed","change")
        db.execute("UPDATE monitors SET last_checked=?,content_hash=?,last_error=NULL WHERE id=?",(checked,new_hash,row["id"]))
        db.commit()
        return {"ok":True,"content":content,"checked_at":checked,"changed":changed}
    except Exception as exc:
        message=f"{type(exc).__name__}: {str(exc)[:240]}"
        db.execute("UPDATE monitors SET last_checked=?,last_error=? WHERE id=?",(checked,message,row["id"]))
        add_event(db,row["id"],row["name"],row["url"],message,"error"); db.commit()
        return {"ok":False,"error":message,"checked_at":checked}
def monitor_dict(row):
    return {"id":row["id"],"name":row["name"],"url":row["url"],"created_at":row["created_at"],"last_checked":row["last_checked"],"last_changed":row["last_changed"],"last_error":row["last_error"],"interval_minutes":row["interval_minutes"]}
def periodic_worker():
    while True:
        try:
            with connect() as db:
                rows=db.execute("SELECT * FROM monitors WHERE last_checked IS NULL OR (julianday('now')-julianday(last_checked))*1440 >= interval_minutes").fetchall()
                for row in rows: check_one(db,row)
        except Exception as exc: print("Scheduler error:",exc,flush=True)
        time.sleep(30)
class Handler(SimpleHTTPRequestHandler):
    def __init__(self,*args,**kwargs): super().__init__(*args,directory=ROOT,**kwargs)
    def log_message(self,fmt,*args): print("%s - %s"%(self.address_string(),fmt%args))
    def end_headers(self):
        self.send_header("X-Content-Type-Options","nosniff")
        super().end_headers()
    def cors_headers(self):
        origin = self.headers.get("Origin", "")
        if origin in ALLOWED_ORIGINS:
            self.send_header("Access-Control-Allow-Origin", origin)
            self.send_header("Vary", "Origin")
            self.send_header("Access-Control-Allow-Methods", "GET, POST, DELETE, OPTIONS")
            self.send_header("Access-Control-Allow-Headers", "Content-Type")
    def send_json(self,code,payload):
        body=json.dumps(payload).encode()
        self.send_response(code); self.send_header("Content-Type","application/json; charset=utf-8"); self.send_header("Content-Length",str(len(body)))
        self.cors_headers(); self.end_headers(); self.wfile.write(body)
    def do_OPTIONS(self):
        self.send_response(204); self.cors_headers(); self.end_headers()
    def do_GET(self):
        path=urlparse(self.path).path
        if path.startswith("/api/"):
            with connect() as db:
                if path=="/api/health": return self.send_json(200,{"ok":True,"monitors":db.execute("SELECT COUNT(*) FROM monitors").fetchone()[0]})
                if path=="/api/monitors": return self.send_json(200,{"monitors":[monitor_dict(r) for r in db.execute("SELECT * FROM monitors ORDER BY created_at DESC")]})
                if path=="/api/history": return self.send_json(200,{"history":[dict(r) for r in db.execute("SELECT * FROM history ORDER BY id DESC LIMIT 100")]})
            return self.send_json(404,{"error":"Not found"})
        return super().do_GET()
    def do_POST(self):
        path=urlparse(self.path).path
        try: data=json.loads(self.rfile.read(int(self.headers.get("Content-Length","0")) or 0) or b"{}")
        except Exception: return self.send_json(400,{"error":"Invalid JSON"})
        if path=="/api/check":
            url=data.get("url","")
            if not valid_url(url): return self.send_json(400,{"error":"A valid http(s) URL is required"})
            with connect() as db:
                row=db.execute("SELECT * FROM monitors WHERE url=?",(url,)).fetchone()
                if not row:
                    mid=str(data.get("monitor_id") or hashlib.sha1(url.encode()).hexdigest()[:16])
                    name=str(data.get("name") or urlparse(url).hostname or url)[:100]
                    try:
                        db.execute("INSERT INTO monitors(id,name,url,created_at) VALUES(?,?,?,?)",(mid,name,url,now())); db.commit()
                    except sqlite3.IntegrityError: pass
                    row=db.execute("SELECT * FROM monitors WHERE url=?",(url,)).fetchone()
                result=check_one(db,row)
                return self.send_json(200 if result["ok"] else 502,result)
        if path=="/api/monitors":
            url=data.get("url",""); name=str(data.get("name") or urlparse(url).hostname or "Untitled")[:100]; mid=str(data.get("id") or hashlib.sha1(url.encode()).hexdigest()[:16])
            if not valid_url(url): return self.send_json(400,{"error":"A valid http(s) URL is required"})
            try:
                with connect() as db:
                    db.execute("INSERT INTO monitors(id,name,url,created_at,interval_minutes) VALUES(?,?,?,?,?)",(mid,name,url,now(),max(5,min(10080,int(data.get("interval_minutes",60))))));db.commit()
                return self.send_json(201,{"ok":True,"id":mid})
            except sqlite3.IntegrityError: return self.send_json(409,{"error":"This URL is already monitored"})
        if path.startswith("/api/monitors/") and path.endswith("/check"):
            mid=path.split("/")[3]
            with connect() as db:
                row=db.execute("SELECT * FROM monitors WHERE id=?",(mid,)).fetchone()
                if not row:return self.send_json(404,{"error":"Monitor not found"})
                return self.send_json(200 if (result:=check_one(db,row))["ok"] else 502,result)
        return self.send_json(404,{"error":"Not found"})
    def do_DELETE(self):
        path=urlparse(self.path).path
        if path.startswith("/api/monitors/"):
            mid=path.rsplit("/",1)[-1]
            with connect() as db:
                db.execute("DELETE FROM monitors WHERE id=?",(mid,));db.execute("DELETE FROM history WHERE monitor_id=?",(mid,));db.commit()
            return self.send_json(200,{"ok":True})
        return self.send_json(404,{"error":"Not found"})
if __name__=="__main__":
    with connect() as db: pass
    threading.Thread(target=periodic_worker,daemon=True).start()
    print(f"PageWatch running at http://{HOST}:{PORT}",flush=True)
    ThreadingHTTPServer((HOST,PORT),Handler).serve_forever()
