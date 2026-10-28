# PageWatch

**[English](./README.md) · [Español](./README.es.md)**

**Versión web:** [Abrir PageWatch en GitHub Pages](https://ericsnet.github.io/PageWatch/)

PageWatch es una herramienta ligera para detectar cambios en páginas web, con dos modos de uso: una aplicación estática para GitHub Pages y un servicio local opcional en Python para descargar contenido y realizar comprobaciones periódicas.

## Funciones de esta primera versión

- Añadir y gestionar una lista de páginas públicas HTTP(S).
- Guardar monitores e historial en el navegador, sin necesidad de cuenta.
- Comprobaciones manuales y detección de cambios cuando las políticas de seguridad del navegador permiten acceder al contenido.
- Servicio local opcional con Python, SQLite y comprobaciones periódicas.
- Interfaz adaptable a ordenadores y móviles.
- Flujo de GitHub Actions para publicar en GitHub Pages.

## Importante: limitaciones de CORS en GitHub Pages

La versión de GitHub Pages se ejecuta por completo en el navegador. **Las comprobaciones fallarán en sitios que no permitan solicitudes de otros orígenes mediante CORS**; PageWatch no puede anular esa protección del navegador.

Si controlas la web que quieres vigilar, configura su servidor para permitir el origen de PageWatch, `https://ericsnet.github.io`, mediante la cabecera de respuesta `Access-Control-Allow-Origin` (y los métodos o encabezados que sean necesarios). No desactives CORS indiscriminadamente ni permitas todos los orígenes en una web sensible. Si no controlas la web de destino, no puedes corregir su política CORS desde PageWatch: utiliza el servicio local de Python o un backend independiente para descargar la página desde el servidor. Algunas webs también pueden bloquear solicitudes automatizadas o exigir autenticación.

Las comprobaciones realizadas únicamente desde el navegador son manuales y no están programadas. El servicio local descarga el contenido desde tu ordenador y realiza comprobaciones periódicas mientras está en funcionamiento.

## Ejecución local

Necesitas Python 3.10 o posterior. No se requieren paquetes Python de terceros.

```bash
python server.py
```

Abre [http://127.0.0.1:8765](http://127.0.0.1:8765). La base de datos SQLite, `pagewatch.db`, se crea en la carpeta del proyecto. Mantén el proceso en ejecución para que funcionen las comprobaciones periódicas. Para detenerlo, pulsa Ctrl+C.

En Windows puedes usar el mismo comando desde PowerShell o Símbolo del sistema si Python está en PATH.

## Publicar en GitHub Pages

1. Sube el repositorio a GitHub.
2. Abre **Settings → Pages**.
3. Selecciona **GitHub Actions** como origen de compilación y despliegue.
4. Sube un cambio a `main` o ejecuta manualmente el flujo **Deploy PageWatch to GitHub Pages**.

El flujo publica únicamente los archivos estáticos del frontend. Python y SQLite no se ejecutan en Pages; usa el modo local para esas funciones.

## Privacidad y uso responsable

Los datos del modo navegador permanecen en el almacenamiento local del navegador. El modo local guarda los datos en una base SQLite de tu ordenador. Vigila únicamente páginas a las que tengas permiso de acceder, respeta las condiciones y restricciones de cada sitio y utiliza intervalos de consulta razonables.

## Estado

Desarrollo inicial. No todas las funciones previstas en la descripción original están implementadas todavía.

## Licencia

Todos los derechos reservados. Consulta [LICENSE](./LICENSE). La visibilidad pública no concede permiso para copiar, modificar o redistribuir este proyecto sin autorización, salvo en los casos permitidos por la legislación aplicable.
