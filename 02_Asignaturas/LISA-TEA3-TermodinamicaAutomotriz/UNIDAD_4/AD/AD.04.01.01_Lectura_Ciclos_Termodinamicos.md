# Actividad de desarrollo (AD): Ciclos termodinámicos fundamentales

## AD.04.01.01_Lectura_Ciclos_Termodinamicos

### Introducción a los ciclos termodinámicos

Los **ciclos termodinámicos** son secuencias de **procesos** que transforman **energía térmica** en **trabajo mecánico**, o viceversa. Son la base de funcionamiento de **máquinas térmicas** como **motores de combustión interna**, refrigeradores y bombas de calor. Comprender estos ciclos es fundamental para el **análisis** y **diseño** de **sistemas energéticos** en la **ingeniería automotriz**.

En esta lectura, exploraremos los **ciclos ideales** de **Carnot**, **Otto** y **Diesel**, que sirven como **modelos teóricos** para entender los límites y el comportamiento de los motores reales.

---

### 1. El ciclo de Carnot: el límite ideal

El **ciclo de Carnot** es un **ciclo termodinámico ideal** y **reversible** que opera entre dos **fuentes de calor** a **temperaturas constantes**. Es de suma **importancia teórica** porque establece el **límite superior de eficiencia** para cualquier **máquina térmica** que opere entre esas dos temperaturas. Aunque no es realizable en la práctica, sirve como **referencia** para evaluar el **rendimiento** de los ciclos reales.

El **ciclo de Carnot** consta de cuatro **procesos reversibles**:

1.  **Expansión Isotérmica (1-2):** El **fluido de trabajo** **absorbe calor** ($Q_H$) de una **fuente a alta temperatura** ($T_H$) mientras se **expande**, realizando **trabajo**.
    *   Ecuación del calor absorbido:
        $Q_H = T_H \Delta S_{12}$

2.  **Expansión Adiabática (2-3):** El fluido se expande **sin intercambio de calor**, **disminuyendo su temperatura** de $T_H$ a $T_L$ mientras realiza **trabajo**.
    *   Ecuación de la relación de temperaturas y volúmenes:
        $T_2 V_2^{\gamma-1} = T_3 V_3^{\gamma-1}$

3.  **Compresión Isotérmica (3-4):** El fluido **cede calor** ($Q_L$) a un **sumidero a baja temperatura** ($T_L$) mientras se **comprime**, requiriendo **trabajo**.
    *   Ecuación del calor cedido:
        $Q_L = T_L \Delta S_{34}$

4.  **Compresión Adiabática (4-1):** El fluido se comprime **sin intercambio de calor**, **aumentando su temperatura** de $T_L$ a $T_H$ mientras se le **aplica trabajo**.
    *   Ecuación de la relación de temperaturas y volúmenes:
        $T_4 V_4^{\gamma-1} = T_1 V_1^{\gamma-1}$

La **eficiencia térmica** del **ciclo de Carnot** ($\eta_{Carnot}$) se define como:

$\eta_{Carnot} = 1 - \frac{T_L}{T_H}$

Donde $T_L$ es la **temperatura absoluta** del **sumidero de calor** y $T_H$ es la **temperatura absoluta** de la **fuente de calor**.

**[INDICACIÓN DE IMAGEN: Incluir un diagrama P-V (Presión-Volumen) y un diagrama T-S (Temperatura-Entropía) para el ciclo de Carnot. Ambos diagramas deben mostrar claramente los cuatro procesos (1-2, 2-3, 3-4, 4-1) y las temperaturas $T_H$ y $T_L$.]**

---

### 2. El ciclo de Otto: motores de gasolina

El **ciclo de Otto** es el **modelo ideal** para los **motores de encendido por chispa** (**motores de gasolina**). Se compone de cuatro **procesos internamente reversibles**, dos **adiabáticos** y dos **isocóricos** (**volumen constante**).

1.  **Compresión Adiabática (1-2):** El **aire-combustible** se **comprime sin intercambio de calor**, **aumentando su temperatura y presión**.
    *   **Relación de compresión** ($r$):
        $r = \frac{V_1}{V_2}$

2.  **Adición de Calor a Volumen Constante (2-3):** Se simula la **combustión**, donde se **añade calor** ($Q_{in}$) al sistema a **volumen constante**, **elevando drásticamente la presión y temperatura**.
    *   **Calor añadido**:
        $Q_{in} = m c_v (T_3 - T_2)$

3.  **Expansión Adiabática (3-4):** Los **gases calientes** se **expanden**, realizando **trabajo** sobre el **pistón** y **disminuyendo su temperatura y presión**.

4.  **Rechazo de Calor a Volumen Constante (4-1):** Se simula la **expulsión de gases de escape**, donde se **cede calor** ($Q_{out}$) al ambiente a **volumen constante**, **disminuyendo la presión**.
    *   **Calor rechazado**:
        $Q_{out} = m c_v (T_4 - T_1)$

La **eficiencia térmica** del **ciclo de Otto** ($\eta_{Otto}$) se expresa como:

$\eta_{Otto} = 1 - \frac{1}{r^{\gamma-1}}$

Donde $r$ es la **relación de compresión** y $\gamma$ es la **relación de calores específicos** ($c_p/c_v$).

**[INDICACIÓN DE IMAGEN: Incluir un diagrama P-V (Presión-Volumen) para el ciclo de Otto, mostrando los cuatro procesos y la relación de compresión. Opcionalmente, un diagrama T-S.]**

---

### 3. El ciclo Diesel: motores de encendido por compresión

El **ciclo Diesel** es el **modelo ideal** para los **motores de encendido por compresión** (**motores diésel**). A diferencia del **ciclo de Otto**, la **adición de calor** ocurre a **presión constante**.

1.  **Compresión Adiabática (1-2):** El **aire** se **comprime sin intercambio de calor**, **aumentando su temperatura y presión**.

2.  **Adición de Calor a Presión Constante (2-3):** Se simula la **combustión**, donde se **añade calor** ($Q_{in}$) al sistema a **presión constante**, **elevando el volumen y la temperatura**.
    *   **Calor añadido**:
        $Q_{in} = m c_p (T_3 - T_2)$

3.  **Expansión Adiabática (3-4):** Los **gases calientes** se **expanden**, realizando **trabajo** sobre el **pistón** y **disminuyendo su temperatura y presión**.

4.  **Rechazo de Calor a Volumen Constante (4-1):** Se simula la **expulsión de gases de escape**, donde se **cede calor** ($Q_{out}$) al ambiente a **volumen constante**, **disminuyendo la presión**.
    *   **Calor rechazado**:
        $Q_{out} = m c_v (T_4 - T_1)$

La **eficiencia térmica** del **ciclo Diesel** ($
eta_{Diesel}$) se calcula con la siguiente fórmula:

$\eta_{Diesel} = 1 - \frac{1}{r^{\gamma-1}} \left[ \frac{r_c^{\gamma} - 1}{\gamma (r_c - 1)} \right]$

Donde $r$ es la **relación de compresión** y $r_c$ es la **relación de corte** (relación de volúmenes al final y al inicio de la adición de calor a presión constante).

**[INDICACIÓN DE IMAGEN: Incluir un diagrama P-V (Presión-Volumen) para el ciclo Diesel, mostrando los cuatro procesos y la adición de calor a presión constante. Opcionalmente, un diagrama T-S.]**

---

### 4. Comparación de ciclos y parámetros clave en motores

Aunque los **ciclos de Otto y Diesel** son **modos ideales**, su **comparación** nos permite entender las **diferencias fundamentales** en el **diseño** y **operación** de los **motores de gasolina y diésel**.

| Característica           | Ciclo de Otto (Gasolina)                               | Ciclo Diesel (Diésel)                                  |
| :----------------------- | :----------------------------------------------------- | :----------------------------------------------------- |
| **Combustión**           | Por **chispa** (bujía)                                     | Por **compresión** (autoignición)                          |
| **Adición de Calor**     | A **volumen constante**                                    | A **presión constante**                                    |
| **Combustible**          | **Gasolina**                                               | **Diésel**                                                 |
| **Relación de Compresión** | Típicamente **más baja** (8:1 a 12:1)                      | Típicamente **más alta** (14:1 a 25:1)                     |
| **Eficiencia**           | Depende fuertemente de la **relación de compresión**       | Depende de la **relación de compresión** y de **corte**        |

**Parámetros Clave en Motores de Combustión Interna:**

*   **Potencia** ($W$): **Tasa** a la que se realiza **trabajo**. En motores, se refiere a la **potencia generada** por el motor.
    *   **Ecuación general de potencia**:
        $W = \frac{\text{Trabajo}}{\text{Tiempo}}$
*   **Cilindrada** ($V_d$): **Volumen total desplazado** por todos los **pistones** en un ciclo. Es un **indicador del tamaño del motor**.
    *   **Ecuación de cilindrada unitaria**:
        $V_d = \frac{\pi D^2}{4} L$
        Donde $D$ es el **diámetro del cilindro** y $L$ es la **carrera del pistón**.
*   **Rendimiento** (**Eficiencia**): **Relación** entre el **trabajo útil obtenido** y la **energía suministrada**. Puede ser **térmica**, **mecánica** o **volumétrica**.

**[INDICACIÓN DE IMAGEN: Incluir un diagrama P-V que superponga los ciclos de Otto y Diesel para una comparación visual directa, mostrando cómo la adición de calor difiere.]**

---

### Conclusión

Los **ciclos de Carnot, Otto y Diesel** son **pilares fundamentales** en la **termodinámica aplicada** a la **ingeniería automotriz**. Aunque son **idealizaciones**, proporcionan las **herramientas conceptuales y analíticas** para entender el **funcionamiento**, las **limitaciones** y las **oportunidades de mejora** en los **motores de combustión interna**. La **comprensión** de sus **procesos**, **eficiencias** y los **parámetros clave** asociados es **esencial** para el **análisis** y **diseño** de **sistemas energéticos eficientes y sostenibles**.

---

### Referencias Bibliográficas

*   Çengel, Y. A., & Boles, M. A. (2011). *Termodinámica* (6a. ed.). McGraw-Hill.
*   Moran, M. J., Shapiro, H. N., Boettner, D. D., & Bailey, M. B. (2018). *Fundamentals of Engineering Thermodynamics* (9th ed.). Wiley.
*   Payri, F., & Desantes, J. M. (Coords.). (2011). *Motores de combustión interna alternativos*. Editorial de la UPV.