# Lista de Pendientes y Mejoras (ToDo)

Este archivo sirve para registrar tareas importantes pero no urgentes, ideas de mejora y optimizaciones para nuestro flujo de trabajo. El objetivo es no perder estas ideas mientras nos enfocamos en las prioridades actuales.

---

## Pendientes de Alta Prioridad (Próxima Sesión)

1.  **Generar/Integrar Diagramas P-V en Lecturas AD (Ciclos Termodinámicos)**
    -   **Tarea:** Crear o conseguir los diagramas P-V para los ciclos de Carnot, Otto y Diesel.
    -   **Acción:** Insertar las referencias a estas imágenes en el archivo `AD.04.01.01_Lectura_Ciclos_Termodinamicos.tex`.
    -   **Prioridad:** Alta (Crucial para la comprensión visual de la lectura).

2.  **Generar PDFs de todos los Materiales de la Unidad 4**
    -   **Tarea:** Compilar todos los archivos `.tex` generados para la Unidad 4 a sus respectivos PDFs.
    -   **Acción:** Colocar los PDFs resultantes en la carpeta `_PRODUCTOS/` de la Unidad 4, siguiendo la nomenclatura estándar.
    -   **Prioridad:** Alta (Producto final de la prueba piloto).

---

## 1. Automatizar la Compilación de Documentos LaTeX

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

---

## 2. Mantener la Organización de Carpetas

- **Tarea:** Revisar periódicamente las carpetas de las unidades para eliminar archivos temporales o innecesarios (ej. `.aux`, `.log`, `.fdb_latexmk`, `.fls`).
- **Acción:** Crear un script o definir un proceso manual para limpiar los directorios de trabajo y mantener solo los archivos fuente (`.md`, `.tex`) y los productos finales (`.pdf`).
- **Estado:** Pendiente.
- **Prioridad:** Baja (Buenas prácticas de organización).