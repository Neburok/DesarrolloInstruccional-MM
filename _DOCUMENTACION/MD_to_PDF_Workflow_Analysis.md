## Análisis del Flujo de Trabajo Markdown (MD) -> LaTeX (TeX) -> PDF

Este informe detalla la viabilidad técnica y los requisitos para automatizar la conversión de documentos desde Markdown, pasando por LaTeX, hasta generar un PDF final.

### Flujo de Trabajo Recomendado: MD -> LaTeX -> PDF

La combinación más robusta y flexible para lograr esto es utilizando **Pandoc** (a través de su *wrapper* de Python `pypandoc`) para la conversión de MD a LaTeX, y luego **PyLaTeX** para la compilación del archivo LaTeX resultante a PDF.

#### 1. Herramientas y Lenguajes Necesarios:

*   **Lenguaje de Programación:** Python.
*   **Herramienta de Conversión:** **Pandoc**. Es un conversor universal de documentos de línea de comandos. Es el motor principal para transformar Markdown a LaTeX.
*   **Compilador LaTeX:** Una distribución completa de LaTeX instalada en el sistema (ej. **TeX Live** para Linux/macOS o **MiKTeX** para Windows). Esto es *indispensable* ya que `PyLaTeX` y Pandoc lo utilizan para generar el PDF final.

#### 2. Librerías de Python Requeridas:

Para interactuar con Pandoc y LaTeX desde Python, necesitaríamos instalar:

*   `pypandoc_binary`: Un *wrapper* de Python para Pandoc. La versión `_binary` incluye el ejecutable de Pandoc, simplificando su instalación.
    ```bash
    pip install pypandoc_binary
    ```
*   `pylatex`: Una librería de Python para generar y compilar documentos LaTeX programáticamente.
    ```bash
    pip install pylatex
    ```

#### 3. Camino Técnico (Paso a Paso):

1.  **Contenido en Markdown:** Usted escribiría el contenido de sus materiales didácticos (AD, AR, AVS) en archivos `.md`. Es crucial que las ecuaciones matemáticas se escriban en sintaxis LaTeX dentro del Markdown (ej. `$E=mc^2$` o `$$\int x^2 dx$$`). Pandoc es muy bueno reconociendo esto.

2.  **Conversión MD a LaTeX (usando `pypandoc`):**
    *   Un script de Python leería el archivo `.md`.
    *   Utilizaría `pypandoc.convert_text()` para transformar el contenido Markdown a una cadena de texto en formato LaTeX. Pandoc se encargaría de traducir la sintaxis Markdown (encabezados, listas, negritas, etc.) a los comandos LaTeX correspondientes.

3.  **Creación y Compilación de Documento LaTeX (usando `pylatex`):**
    *   La cadena de texto LaTeX generada por Pandoc se insertaría en un objeto `Document` de `PyLaTeX`. Aquí es donde podríamos integrar nuestra plantilla `utp-doc.sty` y otros elementos de formato específicos de la UTP (encabezados, pies de página, etc.) para asegurar la consistencia visual.
    *   `PyLaTeX` escribiría este contenido a un archivo `.tex` temporal.
    *   Finalmente, `PyLaTeX` invocaría al compilador LaTeX (`pdflatex` o `latexmk`) de su instalación de TeX Live/MiKTeX para generar el PDF final.

#### ¿Es "engorroso"?

*   **Configuración Inicial:** La parte más "engorrosa" sería la **instalación y configuración inicial de una distribución LaTeX completa** (TeX Live o MiKTeX) en el entorno donde se ejecute el script. Esto puede ser pesado (varios GB) y a veces requiere ajustes de PATH.
*   **Manejo de Plantillas:** Adaptar `PyLaTeX` para que utilice nuestra plantilla `utp-doc.sty` y mantenga el formato deseado requerirá un poco de trabajo inicial de programación en Python.
*   **Control de Ecuaciones:** Si bien Pandoc maneja bien las ecuaciones LaTeX dentro de Markdown, la complejidad de las ecuaciones y el formato específico que requerimos para variables y unidades ($kg/m^3$) significa que el Markdown debe ser escrito con precisión LaTeX en mente.

**Conclusión de la Exploración:**

El flujo **MD -> LaTeX -> PDF es técnicamente viable y ofrece un control de calidad superior** para nuestros documentos académicos, especialmente por el manejo de ecuaciones y el formato profesional que LaTeX proporciona.

Sin embargo, **no es un camino trivial**. Requiere:
1.  La instalación de una distribución LaTeX completa.
2.  Conocimientos de Python para escribir el script de automatización.
3.  Un esfuerzo inicial para configurar el script para que respete nuestra plantilla y estilos.
