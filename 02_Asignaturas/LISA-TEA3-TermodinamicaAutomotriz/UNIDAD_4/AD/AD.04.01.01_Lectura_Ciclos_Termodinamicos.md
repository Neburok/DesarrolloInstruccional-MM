# Lectura Fundamental: Ciclos Termodinámicos

**Asignatura:** Termodinámica Automotriz
**Unidad 4:** Procesos Termodinámicos y de Transferencia de Calor

---

### Objetivos de Aprendizaje

Al finalizar esta lectura, serás capaz de:

-   Describir el propósito de un ciclo termodinámico y su representación en un diagrama P-V.
-   Explicar los cuatro procesos reversibles que componen el Ciclo de Carnot.
-   Calcular la eficiencia térmica máxima de un motor utilizando la fórmula del Ciclo de Carnot.
-   Diferenciar los procesos de los ciclos de Otto y Diesel y su aplicación en motores de combustión interna.
-   Interpretar las fórmulas de eficiencia para los ciclos de Otto y Diesel.

---

### Introducción a los Ciclos Termodinámicos

Un ciclo termodinámico es una secuencia de procesos que comienza y termina en el mismo estado, permitiendo la conversión continua de calor en trabajo mecánico. Para analizarlos, usamos diagramas P-V, donde el área encerrada por el ciclo representa el trabajo neto ($W_{neto}$) realizado.

### El Ciclo de Carnot: El Límite de la Eficiencia

El Ciclo de Carnot es un ciclo teórico que establece el límite máximo de eficiencia para cualquier motor térmico. Opera entre una fuente de calor a alta temperatura ($T_H$) y un sumidero de calor a baja temperatura ($T_L$) a través de cuatro procesos reversibles: dos isotérmicos y dos adiabáticos.

La eficiencia térmica del Ciclo de Carnot depende únicamente de estas temperaturas absolutas:

$$ \eta_{th,Carnot} = 1 - \frac{T_L}{T_H} $$

**Ejemplo:** Un motor de Carnot que opera entre $600 \, K$ y $300 \, K$ tiene una eficiencia máxima del 50%.

### Ciclos de Motores de Combustión Interna: Otto y Diesel

**Ciclo de Otto (Motores de Gasolina):**

Este ciclo modela los motores de encendido por chispa. Su eficiencia depende de la relación de compresión ($r$):

$$ \eta_{th,Otto} = 1 - \frac{1}{r^{k-1}} $$

**Ciclo de Diesel (Motores Diésel):**

Este ciclo modela los motores de encendido por compresión. La adición de calor ocurre a presión constante. Su eficiencia depende de la relación de compresión ($r$) y de la relación de corte de inyección ($r_c$):

$$ \eta_{th,Diesel} = 1 - \frac{1}{r^{k-1}} \left[ \frac{r_c^k - 1}{k(r_c - 1)} \right] $$

---

### Resumen de Puntos Clave

-   Los ciclos termodinámicos son la base para convertir calor en trabajo útil.
-   El Ciclo de Carnot define la máxima eficiencia teórica posible entre dos temperaturas.
-   El Ciclo de Otto modela los motores de gasolina, con adición de calor a volumen constante.
-   El Ciclo de Diesel modela los motores diésel, con adición de calor a presión constante.
-   La eficiencia de los motores reales siempre será menor que la de los ciclos ideales correspondientes.