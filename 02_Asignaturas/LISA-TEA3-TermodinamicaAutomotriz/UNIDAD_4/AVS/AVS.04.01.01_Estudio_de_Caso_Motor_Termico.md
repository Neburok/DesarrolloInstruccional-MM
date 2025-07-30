# Actividad de Verificación de Saberes (AVS): Estudio de Caso - Análisis Termodinámico de un Motor Automotriz

**Asignatura:** Termodinámica Automotriz
**Unidad 4:** Procesos Termodinámicos y de Transferencia de Calor

---

### Objetivo de la Actividad

Al completar este estudio de caso, el estudiante será capaz de aplicar los principios de los ciclos termodinámicos y los mecanismos de transferencia de calor para analizar el desempeño energético y térmico de un motor de combustión interna, y comunicar sus hallazgos en un informe técnico estructurado.

---

### Instrucciones Generales

1.  Esta actividad es de carácter individual y se realizará en el laboratorio/aula bajo supervisión.
2.  El informe técnico debe ser original y reflejar su propio análisis y comprensión.
3.  Utilice las lecturas y guías de ejercicios proporcionadas en las Actividades de Desarrollo (AD) y Reforzamiento (AR) como material de apoyo.
4.  Presente todos los cálculos de manera clara y ordenada, incluyendo unidades y el uso correcto de la notación LaTeX para ecuaciones.
5.  El informe final debe ser entregado en formato PDF.

---

### Descripción del Caso de Estudio: Evaluación de un Motor de Gasolina de 4 Cilindros

Usted es un ingeniero de desarrollo en una empresa automotriz y se le ha asignado la tarea de evaluar el desempeño termodinámico y la gestión térmica de un motor de gasolina de 4 cilindros, 2.0 litros, que opera bajo ciertas condiciones. El objetivo es identificar áreas de mejora en su eficiencia y en la disipación de calor.

**Datos del Motor y Condiciones de Operación:**

*   **Tipo de Motor:** 4 cilindros, 2.0 L, gasolina.
*   **Ciclo Ideal:** Otto.
*   **Relación de Compresión ($r$):** 10:1.
*   **Relación de calores específicos ($k$ o $\gamma$):** 1.4 (para el aire).
*   **Calor suministrado por ciclo ($Q_{in}$):** $1800 \, kJ/kg$ (por cada kg de mezcla aire-combustible).
*   **Temperatura de la superficie exterior del bloque del motor ($T_{superficie}$):** $110^\circ C$.
*   **Temperatura del aire ambiente ($T_{ambiente}$):** $30^\circ C$.
*   **Área superficial expuesta del bloque del motor ($A_{bloque}$):** $0.6 \, m^2$.
*   **Coeficiente de transferencia de calor por convección ($h_{aire}$):** $15 \, W/m^2 \cdot K$ (entre el bloque y el aire ambiente).
*   **Emisividad del bloque del motor ($\epsilon$):** $0.85$.
*   **Constante de Stefan-Boltzmann ($\sigma$):** $5.67 \times 10^{-8} \, W/m^2 \cdot K^4$.

---

### Requerimientos del Informe Técnico

Su informe técnico debe incluir las siguientes secciones:

#### 1. Análisis del Ciclo Termodinámico (Ciclo Otto Ideal)

a)  **Representación Gráfica:** Dibuje un diagrama P-V del ciclo Otto ideal, identificando claramente los cuatro procesos y los estados principales (1, 2, 3, 4).

b)  **Cálculo de Eficiencia:** Calcule la eficiencia térmica ideal del motor ($\eta_{th,Otto}$) utilizando la relación de compresión y la relación de calores específicos.

c)  **Balance de Energía:** Si el motor procesa $0.005 \, kg$ de mezcla aire-combustible por ciclo, calcule:
    *   El calor total suministrado al motor por ciclo ($Q_{suministrado}$). (Considere $Q_{in}$ dado por kg de mezcla).
    *   El trabajo neto producido por ciclo ($W_{neto}$). (Utilice la eficiencia calculada).
    *   El calor rechazado por ciclo ($Q_{rechazado}$). (Utilice el balance de energía).

#### 2. Análisis de Transferencia de Calor del Bloque del Motor

a)  **Transferencia de Calor por Convección:** Calcule la tasa de transferencia de calor por convección desde la superficie exterior del bloque del motor al aire ambiente.

b)  **Transferencia de Calor por Radiación:** Calcule la tasa de transferencia de calor por radiación desde la superficie exterior del bloque del motor a los alrededores. Asegúrese de usar temperaturas absolutas.

c)  **Discusión:** Explique cuál de los dos mecanismos (convección o radiación) es más significativo para la disipación de calor en este escenario y por qué.

#### 3. Conclusiones y Recomendaciones

a)  **Conclusiones:** Resuma los hallazgos clave de su análisis, destacando la eficiencia del motor y la importancia de la gestión térmica.

b)  **Recomendaciones:** Proponga al menos dos recomendaciones técnicas para mejorar la eficiencia del motor o su sistema de disipación de calor, justificando brevemente cada una.

---

### Rúbrica de Evaluación

| Criterio de Evaluación | Insuficiente (0-59%) | Suficiente (60-79%) | Bueno (80-89%) | Excelente (90-100%) |
| :--------------------- | :------------------- | :------------------ | :------------- | :------------------ |
| **1. Análisis Ciclo Otto** | No presenta diagrama o cálculos incorrectos. | Diagrama básico, cálculos con errores menores. | Diagrama claro, cálculos correctos. | Diagrama claro y detallado, cálculos precisos y bien justificados. |
| **2. Balance de Energía** | Cálculos de energía incorrectos o ausentes. | Cálculos con errores significativos. | Cálculos correctos, pero con alguna omisión. | Cálculos precisos y completos de $Q_{suministrado}$, $W_{neto}$ y $Q_{rechazado}$. |
| **3. Transferencia de Calor (Convección)** | Cálculo incorrecto o ausente. | Cálculo con errores menores. | Cálculo correcto. | Cálculo preciso y bien presentado. |
| **4. Transferencia de Calor (Radiación)** | Cálculo incorrecto o ausente. | Cálculo con errores menores. | Cálculo correcto. | Cálculo preciso y bien presentado. |
| **5. Discusión de Mecanismos** | No discute o discusión incorrecta. | Discusión básica, sin justificación clara. | Discusión adecuada, con justificación. | Discusión profunda y bien fundamentada, comparando ambos mecanismos. |
| **6. Conclusiones** | Ausentes o irrelevantes. | Superficiales o poco claras. | Claras y relevantes. | Claras, concisas, relevantes y bien fundamentadas. |
| **7. Recomendaciones** | Ausentes o no justificadas. | Presenta pocas, sin justificación sólida. | Presenta recomendaciones justificadas. | Propone recomendaciones innovadoras y bien justificadas. |
| **8. Formato y Presentación** | Desorganizado, errores de LaTeX. | Formato básico, algunos errores. | Formato adecuado, pocos errores. | Formato profesional, uso impecable de LaTeX y claridad. |


