# Proyecto de Desarrollo Instruccional por Competencias

## Objetivo del Repositorio

Este repositorio centraliza el desarrollo de materiales didácticos para asignaturas de nivel universitario, siguiendo el **Enfoque Basado en Competencias (EBC)** y una metodología de trabajo estructurada para la **modalidad mixta**.

## Metodología de Trabajo: Enfoque en la Fase de Desarrollo (ADDIE)

Nos concentramos en la fase de **Desarrollo** del modelo ADDIE. Partimos de un programa de asignatura definido y nos dedicamos a la creación de los recursos de aprendizaje.

Para cada unidad, se genera un paquete de materiales con cuatro componentes clave:

1.  **AD (Actividades de Desarrollo):** Material de aprendizaje autónomo.
2.  **AR (Actividades de Reforzamiento):** Material complementario para práctica y profundización.
3.  **AVS (Actividades de Verificación de Saberes):** Evaluación sumativa presencial.
4.  **ER (Evaluación de Recuperación):** Evaluación alternativa.

## 📁 Estructura del Repositorio

El repositorio se organiza de la siguiente manera:

```
[RAÍZ]/
├── _PLANTILLAS/
│   └── PLANTILLA_UNIDAD/
└── 02_Asignaturas/
    └── [ACRÓNIMO_CARRERA]-[CLAVE]-[ASIGNATURA]/
        ├── _PROGRAMA/
        │   └── [programa_de_la_asignatura].pdf
        ├── UNIDAD_1/
        ├── UNIDAD_2/
        └── ...
```

### Estructura Estándar de una Unidad

Cada carpeta de unidad (ej. `UNIDAD_1/`) se crea a partir de `_PLANTILLAS/PLANTILLA_UNIDAD/` y contiene:

```
UNIDAD_X/
├── README.md
├── AD/
│   └── actividad-desarrollo.md
├── AR/
│   └── actividad-reforzamiento.md
├── AVS/
│   └── verificacion-saberes.md
├── ER/
│   └── evaluacion-recuperacion.md
├── _RECURSOS/
│   ├── img/
│   └── docs/
└── _PRODUCTOS/
    └── ...
```

- **`README.md`**: Describe la competencia y temas de la unidad.
- **`AD`, `AR`, `AVS`, `ER`**: Contienen los archivos fuente (`.md`, `.tex`) de cada componente.
- **`_RECURSOS/`**: Almacena imágenes, diagramas, etc.
- **`_PRODUCTOS/`**: Carpeta de salida para los PDFs finales.

---
*Este proyecto es asistido por Gema, una IA especializada en diseño instruccional.*