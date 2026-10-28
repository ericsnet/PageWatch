# PageWatch

**[English](#english) · [Español](#español)**

<a id="english"></a>

## English

PageWatch is a project in its planning stage that aims to monitor web pages over time and detect meaningful changes in their content.

### Planned features

- **Scheduled checks:** revisit pages at a configurable interval.
- **Version comparison:** identify differences between previous and current content.
- **Change history:** keep a record of detected updates.
- **Noise filters:** ignore irrelevant changes, such as dynamic page elements.
- **Section monitoring:** track a specific part of a page where feasible.
- **Notifications:** alert users when changes match their configured criteria.

These are planned goals, not implemented features.

### Planned technology

- **Python** for fetching, checking, and comparing page content.
- **SQLite** for storing monitored pages, snapshots, and change events.
- **Web interface** for managing monitored pages and reviewing history.

Automated checks will require the monitoring process to be running on a computer or server. The final architecture has not yet been decided.

### Status

**Early planning.** This repository currently contains documentation and a license only. No executable code is included yet.

### Initial roadmap

1. Define how pages are registered and how check intervals are configured.
2. Design storage for page content and change history.
3. Implement page fetching and content normalization.
4. Compare versions and filter irrelevant changes.
5. Add section monitoring and notifications.
6. Build a web interface for managing monitored pages.

### Responsible use

PageWatch is intended for public web pages. Future use must respect website terms, access restrictions, applicable policies, and reasonable request rates.

### License

PageWatch is publicly viewable on GitHub but is **not open-source software**. All rights are reserved. Public access does not grant permission to copy, modify, redistribute, or otherwise use this project's contents except as permitted by applicable law or with prior written permission. See [LICENSE](./LICENSE).

---

<a id="español"></a>

## Español

PageWatch es un proyecto en fase de planificación cuyo objetivo es vigilar páginas web a lo largo del tiempo y detectar cambios relevantes en su contenido.

### Funcionalidades previstas

- **Comprobaciones periódicas:** revisar páginas con un intervalo configurable.
- **Comparación de versiones:** identificar diferencias entre el contenido anterior y el actual.
- **Historial de cambios:** mantener un registro de las actualizaciones detectadas.
- **Filtros de ruido:** ignorar cambios irrelevantes, como elementos dinámicos de una página.
- **Seguimiento de secciones:** vigilar una parte concreta de una página cuando sea viable.
- **Notificaciones:** avisar cuando los cambios coincidan con los criterios configurados.

Estas funciones son objetivos futuros, no funcionalidades implementadas.

### Tecnologías previstas

- **Python** para descargar, comprobar y comparar contenido.
- **SQLite** para almacenar páginas vigiladas, capturas y eventos de cambio.
- **Interfaz web** para gestionar páginas y consultar el historial.

Las comprobaciones automáticas requerirán que el proceso de vigilancia esté en ejecución en un equipo o servidor. La arquitectura definitiva aún no se ha decidido.

### Estado

**Planificación inicial.** Actualmente, este repositorio contiene únicamente documentación y una licencia. Todavía no incluye código ejecutable.

### Hoja de ruta inicial

1. Definir cómo registrar páginas y configurar los intervalos de comprobación.
2. Diseñar el almacenamiento del contenido y del historial.
3. Implementar la descarga y normalización de páginas.
4. Comparar versiones y filtrar cambios irrelevantes.
5. Añadir seguimiento de secciones y notificaciones.
6. Crear una interfaz web para gestionar las páginas vigiladas.

### Uso responsable

PageWatch está pensado para páginas web públicas. Su uso futuro deberá respetar los términos de los sitios, las restricciones de acceso, las políticas aplicables y una frecuencia de consulta razonable.

### Licencia

PageWatch puede consultarse públicamente en GitHub, pero **no es software de código abierto**. Todos los derechos están reservados. El acceso público no concede permiso para copiar, modificar, redistribuir ni utilizar de otro modo el contenido del proyecto, salvo en los casos permitidos por la legislación aplicable o con autorización previa por escrito. Consulta [LICENSE](./LICENSE).
