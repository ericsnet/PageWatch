# PageWatch

**[English](./README.md) · [Español](./README.es.md)**

PageWatch es un proyecto en fase de planificación cuyo objetivo es vigilar páginas web a lo largo del tiempo y detectar cambios relevantes en su contenido.

## Funcionalidades previstas

- **Comprobaciones periódicas:** revisar páginas con un intervalo configurable.
- **Comparación de versiones:** identificar diferencias entre el contenido anterior y el actual.
- **Historial de cambios:** mantener un registro de las actualizaciones detectadas.
- **Filtros de ruido:** ignorar cambios irrelevantes, como elementos dinámicos de una página.
- **Seguimiento de secciones:** vigilar una parte concreta de una página cuando sea viable.
- **Notificaciones:** avisar cuando los cambios coincidan con los criterios configurados.

Estas funciones son objetivos futuros, no funcionalidades implementadas.

## Tecnologías previstas

- **Python** para descargar, comprobar y comparar contenido.
- **SQLite** para almacenar páginas vigiladas, capturas y eventos de cambio.
- **Interfaz web** para gestionar páginas y consultar el historial.

Las comprobaciones automáticas requerirán que el proceso de vigilancia esté en ejecución en un equipo o servidor. La arquitectura definitiva aún no se ha decidido.

## Estado

**Planificación inicial.** Actualmente, este repositorio contiene únicamente documentación y una licencia. Todavía no incluye código ejecutable.

## Hoja de ruta inicial

1. Definir cómo registrar páginas y configurar los intervalos de comprobación.
2. Diseñar el almacenamiento del contenido y del historial.
3. Implementar la descarga y normalización de páginas.
4. Comparar versiones y filtrar cambios irrelevantes.
5. Añadir seguimiento de secciones y notificaciones.
6. Crear una interfaz web para gestionar las páginas vigiladas.

## Uso responsable

PageWatch está pensado para páginas web públicas. Su uso futuro deberá respetar los términos de los sitios, las restricciones de acceso, las políticas aplicables y una frecuencia de consulta razonable.

## Licencia

PageWatch puede consultarse públicamente en GitHub, pero **no es software de código abierto**. Todos los derechos están reservados. El acceso público no concede permiso para copiar, modificar, redistribuir ni utilizar de otro modo el contenido del proyecto, salvo en los casos permitidos por la legislación aplicable o con autorización previa por escrito. Consulta [LICENSE](./LICENSE).
