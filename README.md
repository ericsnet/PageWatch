# PageWatch

**PageWatch** es una herramienta en desarrollo para vigilar páginas web y detectar cambios en su contenido a lo largo del tiempo.

## Objetivo

Permitir que una persona registre páginas o secciones de interés, compruebe si han cambiado y consulte un historial de las modificaciones detectadas.

## Funcionalidades previstas

- **Comprobaciones periódicas:** revisar páginas siguiendo un intervalo configurable.
- **Comparación de versiones:** identificar diferencias entre el contenido anterior y el actual.
- **Historial de cambios:** conservar un registro de las modificaciones detectadas.
- **Filtros de ruido:** ignorar cambios irrelevantes, como partes variables de una página.
- **Seguimiento de secciones:** vigilar una zona concreta de una página cuando sea posible.
- **Notificaciones:** avisar cuando se detecten cambios que cumplan los criterios definidos.

Estas funciones son objetivos del proyecto, no capacidades implementadas todavía.

## Tecnología prevista

- **Python** para la lógica de comprobación y comparación.
- **SQLite** para almacenar páginas vigiladas, versiones y eventos.
- **Interfaz web** para gestionar el seguimiento y consultar el historial.

Las comprobaciones automáticas requerirán que el proceso de vigilancia esté en ejecución en un equipo o servidor. La arquitectura definitiva está pendiente de diseño.

## Estado

**Fase inicial — planificación.** Este repositorio contiene únicamente documentación y la licencia del proyecto. Todavía no incluye código ejecutable.

## Hoja de ruta inicial

1. Definir cómo se registran las páginas y la frecuencia de comprobación.
2. Diseñar el almacenamiento del contenido y del historial.
3. Implementar la descarga y normalización de páginas.
4. Comparar versiones y filtrar cambios irrelevantes.
5. Añadir seguimiento de secciones y notificaciones.
6. Crear una interfaz web para administrar las páginas vigiladas.

## Uso responsable

PageWatch está pensado para páginas públicas. Su futuro uso deberá respetar los términos del sitio, las restricciones de acceso, las políticas aplicables y una frecuencia de consulta razonable.

## Licencia y uso

El proyecto está publicado en GitHub para que pueda consultarse públicamente, pero **no es software de código abierto**. Todos los derechos están reservados. La consulta pública del repositorio no concede permiso para copiar, modificar, redistribuir o utilizar el contenido fuera de los límites permitidos por la legislación aplicable. Consulta el archivo [LICENSE](./LICENSE).
