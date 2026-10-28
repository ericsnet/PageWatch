# PageWatch

**[English](./README.md) · [Español](./README.es.md)**

**Live demo:** [Open PageWatch on GitHub Pages](https://ericsnet.github.io/PageWatch/)

PageWatch is a lightweight web-page change monitor with two deployment modes: a static browser app for GitHub Pages and an optional local Python service for server-side fetching and scheduled checks.

## Features in this first version

- Add and manage a watchlist of public HTTP(S) pages.
- Browser-local storage for monitors and change history; no account required.
- Manual checks and content-change detection where browser security policies allow cross-origin access.
- Optional local Python service with SQLite persistence and periodic checks.
- Responsive interface designed for desktop and mobile.
- GitHub Actions workflow for GitHub Pages deployment.

## Important: CORS limitations in GitHub Pages mode

The GitHub Pages version runs entirely in the browser. **A check will fail on sites that do not allow cross-origin requests (CORS)**; PageWatch cannot override that browser security policy.

If you control the website being monitored, configure its web server to allow the PageWatch origin, `https://ericsnet.github.io`, using an appropriate `Access-Control-Allow-Origin` response header (and any required methods/headers). Do not blindly disable CORS or allow every origin on a sensitive site. If you do not control the target website, you cannot fix its CORS policy from PageWatch; use the local Python service or a separately deployed backend to fetch the page server-side instead. Some sites may still block automated requests or require authentication.

Browser-only checks are manual and are not scheduled. The local service performs fetching from your computer and runs scheduled checks while it is running.

## Run locally

Requires Python 3.10 or newer. No third-party Python packages are needed.

```bash
python server.py
```

Open [http://127.0.0.1:8765](http://127.0.0.1:8765). The SQLite database, `pagewatch.db`, is created in the project directory after startup. Keep the process running for periodic checks. Stop it with Ctrl+C.

On Windows, the same command works from PowerShell or Command Prompt if Python is on PATH.

## Deploy to GitHub Pages

1. Push the repository to GitHub.
2. Open **Settings → Pages**.
3. Set the build and deployment source to **GitHub Actions**.
4. Push a change to `main` or manually run the **Deploy PageWatch to GitHub Pages** workflow.

The workflow publishes the static frontend files. Python and SQLite are not deployed to Pages; use local mode for those features.

## Privacy and responsible use

Browser-mode data remains in your browser's local storage. Local-mode data is stored in the SQLite database on your computer. Only monitor pages you are allowed to access, respect site terms and access controls, and use reasonable request intervals.

## Status

Early development. The planned features in the original project description are not all implemented yet.

## License

All rights reserved. See [LICENSE](./LICENSE). Public visibility does not grant permission to copy, modify, or redistribute this project without authorization, except as allowed by applicable law.
