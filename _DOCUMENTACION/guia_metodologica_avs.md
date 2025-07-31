### **Guía Metodológica para el Desarrollo de Actividades de Verificación de Saberes (AVS) - v2**

**Objetivo:** Estandarizar el proceso de creación de Actividades de Verificación de Saberes (AVS) para garantizar la coherencia, calidad y alineación con el Enfoque Basado en Competencias (EBC), facilitando un desarrollo colaborativo y escalable.

---

#### **Fase 1: Análisis y Planificación Estratégica**

El objetivo de esta fase es definir qué se va a evaluar y cómo se conectará con una situación realista, antes de escribir una sola línea de la actividad.

1.  **Consultar el Programa de la Asignatura:**
    *   **Acción:** Localizar y analizar el archivo PDF del programa de la asignatura, ubicado en la carpeta `_PROGRAMA/`.
    *   **Propósito:** Identificar la **competencia específica** de la unidad y los **saberes (saber, saber hacer, saber ser)** que el estudiante debe demostrar. La AVS debe ser un reflejo directo de estos elementos.

2.  **Definir el Escenario de Aplicación (Contexto Real):**
    *   **Acción:** Proponer un escenario o caso de estudio que sea relevante para un ingeniero en el contexto industrial de México (automotriz, aeroespacial, manufactura, etc.).
    *   **Propósito:** Crear una **evaluación auténtica**. El problema debe simular un desafío profesional real, donde el estudiante no solo calcula, sino que analiza, interpreta y toma de decisiones.

3.  **Estructurar la Actividad en Fases Lógicas:**
    *   **Acción:** Desglosar la resolución del problema en 2 a 5 fases progresivas. Por ejemplo: `Fase 1: Análisis de Datos`, `Fase 2: Cálculos de Ingeniería`, `Fase 3: Propuesta de Solución`.
    *   **Propósito:** Guiar al estudiante a través de un proceso de pensamiento estructurado y facilitar una evaluación por partes.

---

#### **Fase 2: Diseño y Redacción del Contenido**

En esta fase se crea el borrador de la actividad, asegurando que el lenguaje y los datos sean precisos y profesionales.

1.  **Redactar el Borrador Inicial en Markdown (`.md`):**
    *   **Acción:** Crear el contenido completo de la AVS, incluyendo introducción, descripción del caso, datos técnicos, y las tareas a realizar en cada fase.
    *   **Propósito:** Utilizar un formato base que es fácil de editar, versionar y posteriormente convertir a LaTeX.

2.  **Aplicar el Formato LaTeX (Regla No Negociable):**
    *   **Acción:** Asegurar que **TODAS** las expresiones matemáticas, variables ($P, V, T$), unidades ($kg/m^3, Pa, N \cdot m$) y símbolos se escriban en formato LaTeX.
    *   **Propósito:** Garantizar la precisión técnica y el profesionalismo del documento final, eliminando ambigüedades.

---

#### **Fase 3: Estandarización y Documentación**

Esta fase asegura que la actividad se integre correctamente en la estructura del proyecto.

1.  **Asignar la Nomenclatura de Archivo Correcta:**
    *   **Acción:** Nombrar el archivo Markdown siguiendo la convención estricta: `AVS.[UNIDAD].[TEMA].[ACTIVIDAD]_[Nombre_Descriptivo].md`.
    *   **Ejemplo:** `AVS.01.01.01_Analisis_Metrologico_Vehiculo_Electrico.md`.
    *   **Propósito:** Mantener una organización impecable que permita la fácil localización y gestión de los recursos.

2.  **Definir la "Forma de Entrega del Trabajo":**
    *   **Acción:** Crear un apartado final con este título exacto. Debe detallar de forma clara y concisa qué debe entregar el estudiante (formato, estructura del reporte, elementos obligatorios).
    *   **Propósito:** Proporcionar instrucciones inequívocas al estudiante, reduciendo dudas y estandarizando los trabajos recibidos.

3.  **Crear el "Instrumento de Evaluación":**
    *   **Acción:** En una sección aparte, desarrollar la rúbrica o escala estimativa que se usará para calificar. Se debe basar en los ejemplos de la `01_Documentacion_Base/`.
    *   **Propósito:** Ofrecer total transparencia al estudiante sobre los criterios y ponderaciones que se utilizarán para medir su desempeño.

---

#### **Fase 4: Revisión, Validación y Generación de Entregables**

El ciclo se cierra con la validación por pares y la producción de los archivos finales.

1.  **Revisión Interna (Profesor-Gema):**
    *   **Acción:** El profesor revisa el archivo `.md` y proporciona retroalimentación inicial. Se realizan los primeros ajustes.
    *   **Propósito:** Asegurar que la versión base del instrumento es pedagógica y técnicamente sólida antes de pasar a una revisión externa.

2.  **Ciclo de Revisión por Pares (Punto de Control Clave):**
    *   **Acción:** Compartir el archivo `.md` con dos grupos de revisores:
        *   **a) Pares Colaboradores:** Colegas que conocen la metodología del proyecto.
        *   **b) Pares Expertos en el Tema:** Especialistas en la materia (ej. un ingeniero de la industria) que no necesariamente conocen la metodología interna.
    *   **Propósito:**
        *   **Revisión de Colaboradores:** Garantizar la **coherencia metodológica**, la estandarización y la correcta aplicación de las plantillas y nomenclaturas del proyecto.
        *   **Revisión de Expertos:** Validar la **precisión técnica**, la relevancia del caso de estudio con la industria actual y el nivel de dificultad de la actividad.

3.  **Incorporación de Retroalimentación:**
    *   **Acción:** Analizar y consolidar la retroalimentación recibida de todos los pares. Realizar los ajustes finales al archivo `.md`.
    *   **Propósito:** Crear una versión final robusta, validada y enriquecida por múltiples perspectivas.

4.  **Generación del Archivo LaTeX (`.tex`):**
    *   **Acción:** Una vez aprobado y validado el `.md`, se genera el archivo `.tex` correspondiente.
    *   **Propósito:** Preparar el documento para su compilación final.

5.  **Compilación del PDF Final:**
    *   **Acción:** Se compila el archivo `.tex` para producir el documento PDF.
    *   **Propósito:** Obtener el recurso didáctico final, listo para ser distribuido.
