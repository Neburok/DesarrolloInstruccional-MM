# CLAUDE.md

Este archivo proporciona orientación a Claude Code (claude.ai/code) cuando trabaja con código en este repositorio.

## Propósito del Repositorio

Este repositorio sirve como una colección integral de materiales didácticos generados durante la preparación de clases universitarias. Contiene contenido educativo para cursos de física, ingeniería de materiales y sistemas automotrices impartidos bajo la metodología del Enfoque Basado en Competencias (EBC) en la UTEQ (Universidad Tecnológica de Querétaro).

## Estructura de Organización de Materiales

El repositorio sigue una estructura pedagógica estandarizada para organizar los materiales del curso:

### Recursos Globales (`00_Recursos_Globales/`)
- **Plantillas_LaTeX/**: Plantillas estandarizadas de LaTeX para presentaciones y documentos
- **Recursos_Graficos/**: Logotipos institucionales y recursos gráficos compartidos

### Estructura del Curso
Cada curso (01_Fisica_Moderna, 02_Ingenieria_Materiales, etc.) contiene:
- **00_Planeacion_General/**: Planificación del curso, programas de estudio, documentación de estructura
- **XX_Unidad_[Tema]/**: Unidades temáticas de aprendizaje con:
  - `01_Guias_Didacticas/`: Guías pedagógicas y secuencias didácticas
  - `02_Presentaciones/`: Materiales de presentación para el aula (archivos fuente .tex)
  - `03_Recursos/`: Recursos educativos de apoyo (imágenes, referencias)
  - `04_Codigo_y_Sims/`: Código educativo y simulaciones de física
  - `05_Evaluaciones/`: Materiales de evaluación y rúbricas
- **Manual_Curso/**: Materiales de manual de curso integral

## Tareas Comunes para el Desarrollo de Materiales

### Compilación de Materiales LaTeX
- Usar el preámbulo estandarizado de `00_Recursos_Globales/Plantillas_LaTeX/prambulo.tex`
- Las presentaciones siguen el formato Beamer con tema Madrid y estilo institucional UTEQ
- Compilación estándar de LaTeX: `pdflatex nombre_archivo.tex` (ejecutar dos veces para referencias)

### Simulaciones Educativas
- Los scripts de Python en las carpetas `04_Codigo_y_Sims/` crean visualizaciones de física
- Librerías estándar utilizadas: numpy, matplotlib, scipy
- Ejecutar simulaciones: `python nombre_script.py`
- Notebooks interactivos de Jupyter: `jupyter notebook nombre_archivo.ipynb`

### Flujo de Trabajo de Generación de Contenido
1. Planificar secuencias didácticas en `01_Guias_Didacticas/`
2. Crear presentaciones en `02_Presentaciones/` usando LaTeX
3. Desarrollar código/simulaciones de apoyo en `04_Codigo_y_Sims/`
4. Compilar todos los materiales para entrega del curso

## Tipos de Archivos Clave y Convenciones

### Materiales Educativos
- **Archivos .tex**: Fuente LaTeX para presentaciones y manuales (español, UTF-8)
- **Archivos .py**: Simulaciones educativas y demostraciones de física
- **Archivos .md**: Planificación pedagógica, guías de enseñanza, documentación de sesiones
- **Archivos .html**: Contenido educativo interactivo basado en web

### Estándares de Materiales
- Todo el contenido sigue la metodología EBC (Enfoque Basado en Competencias)
- Los materiales están diseñados para el contexto universitario tecnológico mexicano
- Contenido en español con terminología técnica
- Enfoque en aplicación práctica y desarrollo de competencias

## Arquitectura del Repositorio

Este es un repositorio de materiales didácticos organizado por disciplina académica:

1. **Física y Física Moderna** (`01_Fisica_Moderna/`): Mecánica cuántica, funciones de onda, materiales de la ecuación de Schrödinger
2. **Ingeniería de Materiales** (`02_Ingenieria_Materiales/`): Selección de materiales, metodología Ashby, aplicaciones de ingeniería
3. **Transferencia de Calor** (`03_Transferencia_Calor/`): Análisis térmico y principios de transferencia de calor
4. **Materiales Automotrices** (`04_Materiales_Automotrices/`): Materiales para aplicaciones automotrices
5. **Sistemas Automotrices** (`04_Sistemas_Automotrices/`): Sistemas vehiculares y comportamiento mecánico

## Contexto del Asistente de IA

El repositorio incluye GEMINI.md con instrucciones para un asistente de IA que ayuda con el diseño pedagógico y planificación de cursos utilizando la metodología de educación basada en competencias.

## Notas Importantes del Repositorio

- Este es un repositorio de materiales didácticos, no un proyecto de desarrollo de software
- No hay comandos tradicionales de construcción/prueba - los materiales se compilan individualmente según sea necesario
- El contenido abarca múltiples disciplinas de ingeniería con énfasis en física aplicada
- Los materiales se generan a través de planificación pedagógica asistida por IA