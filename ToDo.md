# Lista de Pendientes y Mejoras (ToDo)

Este archivo sirve para registrar tareas importantes pero no urgentes, ideas de mejora y optimizaciones para nuestro flujo de trabajo. El objetivo es no perder estas ideas mientras nos enfocamos en las prioridades actuales.

---

## Instrucciones de Sesión

-   Al inicio de cada sesión, por favor, revisa este `ToDo.md` para conocer las tareas pendientes y prioridades.
-   También, revisa el resumen de la sesión anterior (`Resumen_Sesion_AAAA-MM-DD.md`) para retomar el contexto.

---

## Mejoras de Flujo de Trabajo y Documentación

### 1. Automatizar la Compilación de Documentos LaTeX

- **Tarea:** Crear un script (`compilador.bat` o similar) que automatice el proceso de generación de PDFs a partir de los archivos `.tex`.
- **Descripción del Proceso a Automatizar:**
    1.  Recibir la ruta de un archivo `.tex` como argumento.
    2.  Crear una carpeta de compilación temporal.
    3.  Copiar el archivo `.tex` y todos los recursos de la plantilla (`_PLANTILLAS/TEMPLATE_LECTURA_PDF/`) a la carpeta temporal.
    4.  Ejecutar `pdflatex` dos veces dentro de la carpeta temporal.
    5.  Mover el PDF resultante a la carpeta `_PRODUCTOS/` correspondiente a su unidad, usando la nomenclatura estándar.
    6.  Eliminar la carpeta temporal con todos los archivos auxiliares (`.log`, `.aux`, etc.).
- **Estado:** Pendiente.
- **Prioridad:** Media-Baja (Mejora de flujo de trabajo).

### 2. Documentar Procesos Establecidos
- **Tarea:** Crear y mantener documentos (`.md`) que formalicen los flujos de trabajo clave del proyecto (ej. la "Guía Metodológica para AVS").
- **Acción:** Ubicar estos documentos en la carpeta `_DOCUMENTACION/`.
- **Estado:** En progreso (creada la primera versión para AVS).
- **Prioridad:** Media (Fundamental para la escalabilidad y la incorporación de nuevos colaboradores).

### 3. Documentar Casos de Éxito
- **Tarea:** Al finalizar un hito importante (ej. completar todos los materiales de una unidad), crear un breve reporte o "Post-mortem" del proceso.
- **Acción:** El reporte debe incluir: qué funcionó bien, qué desafíos se encontraron y qué lecciones se aprendieron. Se guardará en una subcarpeta dentro de `_DOCUMENTACION/CasosDeExito/`.
- **Estado:** Pendiente.
- **Prioridad:** Baja (Valioso para la mejora continua y el registro histórico).

### 4. Mantener la Organización de Carpetas

- **Tarea:** Revisar periódicamente las carpetas de las unidades para eliminar archivos temporales o innecesarios (ej. `.aux`, `.log`, `.fdb_latexmk`, `.fls`).
- **Acción:** Crear un script o definir un proceso manual para limpiar los directorios de trabajo y mantener solo los archivos fuente (`.md`, `.tex`) y los productos finales (`.pdf`).
- **Estado:** Pendiente.
- **Prioridad:** Baja (Buenas prácticas de organización).

### 5. Exploración del Flujo MD -> LaTeX -> PDF

- **Tarea:** Investigar y prototipar la automatización de la conversión de Markdown a PDF vía LaTeX.
- **Estado:** Exploración inicial completada. Se determinó que es técnicamente viable pero no trivial de implementar con la plantilla actual.
- **Prioridad:** Posponer (Se prioriza el flujo .tex a PDF por ahora, debido a la complejidad y otras tareas pendientes).
