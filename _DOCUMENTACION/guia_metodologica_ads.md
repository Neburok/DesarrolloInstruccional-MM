### **Guía Metodológica para el Desarrollo de Actividades de Desarrollo (ADs)**

**Objetivo:** Estandarizar el proceso de creación de Actividades de Desarrollo (ADs) para garantizar la coherencia, calidad y alineación con el Enfoque Basado en Competencias (EBC), facilitando un desarrollo colaborativo y escalable de materiales didácticos que promuevan la adquisición de conocimientos y habilidades aplicadas.

---

#### **Fase 1: Análisis y Diseño Pedagógico**

El objetivo de esta fase es definir el propósito de la AD, su formato y cómo contribuirá a la construcción de la competencia.

1.  **Consultar el Programa de la Asignatura:**
    *   **Acción:** Localizar y analizar el archivo PDF del programa de la asignatura, ubicado en la carpeta `_PROGRAMA/`.
    *   **Propósito:** Identificar la **competencia específica** de la unidad y los **saberes (saber, saber hacer, saber ser)** que el estudiante debe adquirir y aplicar. La AD debe ser un medio directo para construir estos elementos.

2.  **Selección Metodológica del Tipo(s) y Alcance de la AD:**
    *   **Acción:** Para determinar el tipo o tipos de material didáctico más adecuados, se debe realizar un análisis guiado por las siguientes preguntas:
        *   **a) Naturaleza del Contenido:**
            *   ¿Es un concepto **teórico/abstracto** que requiere explicación detallada y ejemplos? (Ej: Leyes de la Termodinámica, Estructura Cristalina)
            *   ¿Es un **procedimiento/proceso** que necesita una secuencia clara de pasos? (Ej: Ciclo de Otto, Proceso de manufactura)
            *   ¿Implica **visualización** de estructuras, relaciones o flujos? (Ej: Diagramas P-V, Componentes de un motor)
            *   ¿Requiere la **interpretación de datos** o gráficos? (Ej: Curvas de rendimiento, Tablas de propiedades)
        *   **b) Objetivo de Aprendizaje (Nivel Cognitivo):**
            *   ¿El objetivo principal es **comprender y recordar** información clave?
            *   ¿Se busca que el estudiante **aplique** un concepto o **analice** una situación?
            *   ¿Se espera que el estudiante **sintetice** información o **cree** algo nuevo (aunque sea un prototipo conceptual)?
        *   **c) Complementariedad:**
            *   ¿Qué formatos se complementarían mejor para abordar el tema de manera integral y atender diferentes estilos de aprendizaje? (Ej: Lectura + Infografía; Presentación + Video corto).

    *   **Propuesta de Tipos de AD según el Análisis:**
        *   **Para Contenido Teórico/Conceptual (Comprender/Recordar):**
            *   **Documento de Lectura Formal (`AD`):** Profundidad, explicaciones detalladas, ejemplos, analogías.
            *   **Presentación (`AVS` - si es un guion para clase):** Resumen de puntos clave, apoyo visual, estructura lógica.
        *   **Para Contenido Procedural/Procesos (Aplicar/Analizar):**
            *   **Infografía (`AVS` - si es visual):** Secuencia de pasos, diagramas de flujo, componentes.
            *   **Guía de Ejercicios Resueltos (`AR` - si es para desarrollo):** Aplicación paso a paso de procedimientos.
        *   **Para Contenido Visual/Estructural (Comprender/Aplicar):**
            *   **Infografía (`AVS` - si es visual):** Diagramas, esquemas, componentes con etiquetas.
            *   **Video Explicativo (Guion `AVS`):** Animaciones, demostraciones visuales.
        *   **Para Contenido de Aplicación/Análisis (Analizar/Sintetizar):**
            *   **Estudio de Caso Introductorio (`AD`):** Presentación de un problema real para contextualizar la teoría.

    *   **Alcance:** Definir la extensión y profundidad de cada componente seleccionado.

    *   **Propósito:** Asegurar que la combinación de formatos del material didáctico sea la más efectiva para la construcción de la competencia, abordando diferentes estilos de aprendizaje y profundizando en el tema de manera integral, de forma metodológicamente replicable.

3.  **Estructurar el Contenido de la AD:**
    *   **Acción:** Desglosar el tema en secciones lógicas, subtemas y puntos clave. Considerar la progresión del conocimiento, desde lo fundamental hasta la aplicación práctica.
    *   **Propósito:** Facilitar la comprensión del estudiante y la construcción progresiva de la competencia.

---

#### **Fase 2: Creación y Redacción del Contenido**

En esta fase se crea el borrador del material didáctico, asegurando la precisión técnica, la claridad pedagógica y la relevancia.

1.  **Redactar el Borrador Inicial en Markdown (`.md`):**
    *   **Acción:** Crear el contenido completo de la AD, incluyendo explicaciones claras, concisas y con analogías del mundo real para conceptos abstractos o complejos. Generar ejemplos y, si aplica, problemas resueltos paso a paso, mostrando el razonamiento detrás de cada etapa.
    *   **Propósito:** Utilizar un formato base que es fácil de editar, versionar y posteriormente convertir a LaTeX.

2.  **Aplicar el Formato LaTeX (Regla No Negociable):**
    *   **Acción:** Asegurar que **TODAS** las expresiones matemáticas, variables ($P, V, T$), unidades ($kg/m^3, Pa, N \cdot m$) y símbolos se escriban en formato LaTeX.
    *   **Propósito:** Garantizar la precisión técnica y el profesionalismo del documento final, eliminando ambigüedades.

3.  **Integrar Ejemplos y Aplicaciones Reales:**
    *   **Acción:** Incluir ejemplos y aplicaciones del mundo real que sean significativos para estudiantes de ingeniería en México (industria automotriz, aeroespacial, energética, nanotecnología, etc.).
    *   **Propósito:** Conectar la teoría con la práctica y mostrar la aplicabilidad de los conceptos en contextos profesionales.

---

#### **Fase 3: Estandarización y Organización de Archivos**

Esta fase asegura que el material didáctico se integre correctamente en la estructura del proyecto.

1.  **Asignar la Nomenclatura de Archivo Correcta:**
    *   **Acción:** Nombrar el archivo Markdown siguiendo la convención estricta: `AD.[UNIDAD].[TEMA].[ACTIVIDAD]_[Nombre_Descriptivo].md`.
    *   **Ejemplo:** `AD.04.01.01_Lectura_Ciclos_Termodinamicos.md`.
    *   **Propósito:** Mantener una organización impecable que permita la fácil localización y gestión de los recursos.

2.  **Definir Recursos y Materiales Complementarios:**
    *   **Acción:** Sugerir recursos específicos y de alta calidad: simuladores en línea (como PhET), videos (Khan Academy, canales de ingeniería), artículos técnicos, software especializado y lecturas de libros de texto clave.
    *   **Propósito:** Enriquecer la experiencia de aprendizaje del estudiante y proporcionar vías para la profundización.

---

#### **Fase 4: Revisión, Validación y Generación de Entregables**

El ciclo se cierra con la validación por pares y la producción de los archivos finales.

1.  **Revisión Interna (Profesor-Gema):**
    *   **Acción:** El profesor revisa el archivo `.md` y proporciona retroalimentación inicial. Se realizan los primeros ajustes.
    *   **Propósito:** Asegurar que la versión base del material es pedagógica y técnicamente sólida antes de pasar a una revisión externa.

2.  **Ciclo de Revisión por Pares (Punto de Control Clave):**
    *   **Acción:** Compartir el archivo `.md` con dos grupos de revisores:
        *   **a) Pares Colaboradores:** Colegas que conocen la metodología del proyecto.
        *   **b) Pares Expertos en el Tema:** Especialistas en la materia (ej. un ingeniero de la industria) que no necesariamente conocen la metodología interna.
    *   **Propósito:**
        *   **Revisión de Colaboradores:** Garantizar la **coherencia metodológica**, la estandarización y la correcta aplicación de las plantillas y nomenclaturas del proyecto.
        *   **Revisión de Expertos:** Validar la **precisión técnica**, la relevancia del contenido con la industria actual y la claridad pedagógica.

3.  **Incorporación de Retroalimentación:**
    *   **Acción:** Analizar y consolidar la retroalimentación recibida de todos los pares. Realizar los ajustes finales al archivo `.md`.
    *   **Propósito:** Crear una versión final robusta, validada y enriquecida por múltiples perspectivas.

4.  **Generación del Archivo LaTeX (`.tex`):**
    *   **Acción:** Una vez aprobado y validado el `.md`, se genera el archivo `.tex` correspondiente.
    *   **Propósito:** Preparar el documento para su compilación final.

5.  **Compilación del PDF Final:**
    *   **Acción:** Se compila el archivo `.tex` para producir el documento PDF.
    *   **Propósito:** Obtener el recurso didáctico final, listo para ser distribuido.
