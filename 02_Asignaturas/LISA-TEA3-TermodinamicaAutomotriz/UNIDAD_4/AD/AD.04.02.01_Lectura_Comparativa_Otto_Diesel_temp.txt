# AD.04.02.01 - Ciclos Otto y Diesel: Análisis Comparativo de Motores Automotrices

## Contenido

1. [Introducción](#introducción)
2. [Desarrollo](#desarrollo)
   - [Ciclo Otto: Motores de Encendido por Chispa](#ciclo-otto-motores-de-encendido-por-chispa)
   - [Ciclo Diesel: Motores de Encendido por Compresión](#ciclo-diesel-motores-de-encendido-por-compresión)
   - [Análisis Comparativo](#análisis-comparativo)
   - [Gráficos y Diagramas](#gráficos-y-diagramas)
   - [Fórmulas Fundamentales](#fórmulas-fundamentales)
   - [Ejemplos Resueltos](#ejemplos-resueltos)
   - [Ejercicios Propuestos](#ejercicios-propuestos)
3. [Ejercicios de Reforzamiento](#ejercicios-de-reforzamiento)
4. [Conclusiones](#conclusiones)
5. [Bibliografía](#bibliografía)

---

## Introducción

Los **motores de combustión interna** son el corazón de la industria automotriz moderna. Dos de los ciclos termodinámicos más importantes que rigen su funcionamiento son el **Ciclo Otto** y el **Ciclo Diesel**, que representan los fundamentos teóricos de los **motores de gasolina** y **motores diesel**, respectivamente.

Estos ciclos ideales nos permiten:
- Comprender los principios fundamentales de operación de los motores
- Calcular eficiencias teóricas máximas
- Comparar el desempeño entre diferentes tipos de motores
- Optimizar parámetros de diseño como la **relación de compresión**
- Analizar el impacto de variables operativas en el rendimiento

**Competencia a desarrollar:** *Identificar y representar los ciclos termodinámicos Otto y Diesel, calculando eficiencia, potencia y parámetros de rendimiento durante los ciclos desarrollados en aplicaciones automotrices.*

---

## Desarrollo

### Ciclo Otto: Motores de Encendido por Chispa

#### Descripción del Ciclo

El **Ciclo Otto** es el modelo termodinámico idealizado que describe el funcionamiento de los **motores de gasolina** (encendido por chispa). Fue propuesto por Nikolaus Otto en 1876 y consta de **cuatro procesos termodinámicos**:

#### Los Cuatro Procesos del Ciclo Otto

**Proceso 1-2: Compresión Adiabática**
- El **aire-combustible** se comprime sin intercambio de calor
- **Aumento** de presión y temperatura
- **Disminución** del volumen según la relación de compresión

**Proceso 2-3: Adición de Calor a Volumen Constante**
- **Combustión instantánea** simulada por adición de calor
- **Aumento drástico** de presión y temperatura
- El **volumen permanece constante** (proceso isocórico)

**Proceso 3-4: Expansión Adiabática (Carrera de Potencia)**
- Los **gases calientes** se expanden realizando **trabajo útil**
- **Disminución** de presión y temperatura
- **Aumento** del volumen

**Proceso 4-1: Rechazo de Calor a Volumen Constante**
- **Expulsión** de gases de escape simulada
- **Disminución** de presión a volumen constante
- **Retorno** al estado inicial del ciclo

#### Parámetros Clave del Ciclo Otto

**Relación de Compresión ($r$):**
$$r = \frac{V_1}{V_2} = \frac{V_{max}}{V_{min}}$$

Donde:
- $V_1$ = Volumen al final de la admisión
- $V_2$ = Volumen al final de la compresión

**Rango típico en motores de gasolina:** $8:1$ a $12:1$

### Ciclo Diesel: Motores de Encendido por Compresión

#### Descripción del Ciclo

El **Ciclo Diesel** representa el funcionamiento idealizado de los **motores diesel** (encendido por compresión). Propuesto por Rudolf Diesel en 1892, se diferencia del ciclo Otto principalmente en el **proceso de combustión**.

#### Los Cuatro Procesos del Ciclo Diesel

**Proceso 1-2: Compresión Adiabática**
- Solo **aire** se comprime sin intercambio de calor
- **Mayor relación de compresión** que en Otto
- **Temperatura final** suficiente para autoignición del combustible

**Proceso 2-3: Adición de Calor a Presión Constante**
- **Inyección y combustión** progresiva del combustible
- La **presión permanece constante** (proceso isobárico)
- **Aumento** de volumen y temperatura

**Proceso 3-4: Expansión Adiabática (Carrera de Potencia)**
- **Expansión** de gases calientes realizando **trabajo útil**
- **Disminución** de presión y temperatura
- **Aumento** del volumen

**Proceso 4-1: Rechazo de Calor a Volumen Constante**
- **Expulsión** de gases de escape
- **Disminución** de presión a volumen constante
- **Retorno** al estado inicial

#### Parámetros Clave del Ciclo Diesel

**Relación de Compresión ($r$):**
$$r = \frac{V_1}{V_2}$$

**Rango típico en motores diesel:** $14:1$ a $25:1$

**Relación de Corte ($r_c$):**
$$r_c = \frac{V_3}{V_2}$$

Donde:
- $V_3$ = Volumen al final de la adición de calor
- $V_2$ = Volumen al final de la compresión

### Análisis Comparativo

#### Tabla Comparativa Detallada

| **Característica** | **Ciclo Otto (Gasolina)** | **Ciclo Diesel** |
|:-------------------|:--------------------------|:-----------------|
| **Tipo de Encendido** | **Chispa eléctrica** (bujías) | **Autoencendido** por compresión |
| **Combustible** | **Gasolina** (C₈H₁₈) | **Diesel** (C₁₂H₂₃) |
| **Proceso de Combustión** | **Volumen constante** (isocórico) | **Presión constante** (isobárico) |
| **Relación de Compresión** | **8:1 a 12:1** | **14:1 a 25:1** |
| **Velocidad de Combustión** | **Muy rápida** (instantánea) | **Controlada** (progresiva) |
| **Temperatura Máxima** | **2200-2500 K** | **2000-2200 K** |
| **Presión Máxima** | **40-60 bar** | **60-100 bar** |
| **Eficiencia Térmica Típica** | **25-35%** | **35-45%** |
| **Aplicaciones Principales** | **Automóviles**, motocicletas | **Camiones**, autobuses, generadores |

#### Ventajas y Desventajas

**Motores Otto (Gasolina):**

**Ventajas:**
- **Operación más suave** y silenciosa
- **Mayor velocidad** de rotación (RPM)
- **Menor peso** específico
- **Arranque en frío** más fácil

**Desventajas:**
- **Menor eficiencia térmica**
- **Mayor consumo** de combustible
- **Combustible más costoso**

**Motores Diesel:**

**Ventajas:**
- **Mayor eficiencia térmica**
- **Menor consumo** de combustible
- **Mayor durabilidad**
- **Combustible menos costoso**

**Desventajas:**
- **Mayor ruido** y vibración
- **Mayor peso** específico
- **Arranque en frío** más difícil
- **Mayores emisiones** de NOₓ y partículas

### Gráficos y Diagramas

#### Diagrama P-V Comparativo

```
     P
     │
     │    Otto: 2 ──────── 3
     │         │           │
     │         │           │ Diesel: 2 ─── 3
     │         │           │          │     │
     │         │           │          │     │
     │         1 ──────── 4          1 ─── 4
     │________________________________ V
           V₂    V₁              V₂  V₃ V₁
```

#### Diagrama T-S Comparativo

```
     T
     │     Otto y Diesel
     │  3 ─────────────────
     │  │                 │
     │  │                 │
     │  2                 4
     │  │                 │
     │  1 ─────────────────
     │________________________ S
         S₁=S₄           S₂=S₃
```

### Fórmulas Fundamentales

#### Eficiencia del Ciclo Otto

$$\eta_{Otto} = 1 - \frac{1}{r^{\gamma-1}}$$

Donde:
- $\eta_{Otto}$ = Eficiencia térmica del ciclo Otto
- $r$ = Relación de compresión
- $\gamma$ = Relación de calores específicos ($c_p/c_v \approx 1.4$ para aire)

#### Eficiencia del Ciclo Diesel

$$\eta_{Diesel} = 1 - \frac{1}{r^{\gamma-1}} \left[ \frac{r_c^{\gamma} - 1}{\gamma (r_c - 1)} \right]$$

Donde:
- $\eta_{Diesel}$ = Eficiencia térmica del ciclo Diesel
- $r$ = Relación de compresión
- $r_c$ = Relación de corte
- $\gamma$ = Relación de calores específicos

#### Trabajo Neto por Ciclo

**Para ambos ciclos:**
$$W_{neto} = Q_{in} - Q_{out}$$

**Ciclo Otto:**
$$W_{neto} = m c_v [(T_3 - T_2) - (T_4 - T_1)]$$

**Ciclo Diesel:**
$$W_{neto} = m [c_p (T_3 - T_2) - c_v (T_4 - T_1)]$$

#### Potencia del Motor

$$\dot{W} = \frac{W_{neto} \times n \times N}{60 \times n_R}$$

Donde:
- $\dot{W}$ = Potencia del motor (kW)
- $W_{neto}$ = Trabajo neto por ciclo (kJ)
- $n$ = Velocidad del motor (RPM)
- $N$ = Número de cilindros
- $n_R$ = Número de revoluciones por ciclo (2 para motores de 4 tiempos)

### Ejemplos Resueltos

#### Ejemplo 1: Comparación de Eficiencia Otto vs Diesel

**Problema:** Comparar la eficiencia térmica de un motor Otto con $r = 10$ y un motor Diesel con $r = 18$ y $r_c = 2$. Usar $\gamma = 1.4$.

**Solución:**

**Motor Otto:**
$$\eta_{Otto} = 1 - \frac{1}{r^{\gamma-1}} = 1 - \frac{1}{10^{1.4-1}} = 1 - \frac{1}{10^{0.4}}$$
$$\eta_{Otto} = 1 - \frac{1}{2.512} = 1 - 0.398 = 0.602$$
$$\eta_{Otto} = 60.2\%$$

**Motor Diesel:**
$$\eta_{Diesel} = 1 - \frac{1}{18^{0.4}} \left[ \frac{2^{1.4} - 1}{1.4 (2 - 1)} \right]$$
$$\eta_{Diesel} = 1 - \frac{1}{3.314} \left[ \frac{2.639 - 1}{1.4} \right]$$
$$\eta_{Diesel} = 1 - 0.302 \times 1.171 = 1 - 0.354 = 0.646$$
$$\eta_{Diesel} = 64.6\%$$

**Conclusión:** El motor Diesel es más eficiente (64.6% vs 60.2%).

#### Ejemplo 2: Cálculo de Potencia de Motor Otto

**Problema:** Un motor de gasolina de 4 cilindros y 2.0 L opera a 3000 RPM con una eficiencia del 30%. Si cada cilindro produce 0.5 kJ de trabajo neto por ciclo, calcular la potencia del motor.

**Solución:**

**Datos:**
- $N = 4$ cilindros
- $W_{neto} = 0.5$ kJ por cilindro por ciclo
- $n = 3000$ RPM
- $n_R = 2$ (motor de 4 tiempos)

**Trabajo total por ciclo:**
$$W_{total} = N \times W_{neto} = 4 \times 0.5 = 2.0 \text{ kJ por ciclo}$$

**Potencia:**
$$\dot{W} = \frac{W_{total} \times n}{60 \times n_R} = \frac{2.0 \times 3000}{60 \times 2} = \frac{6000}{120} = 50 \text{ kW}$$

**Resultado:** $\dot{W} = 50$ kW = 67 HP

### Ejercicios Propuestos

1. **Ejercicio 1:** Calcular la eficiencia de un motor Otto con relación de compresión 9:1 y compararla con un motor Diesel de relación de compresión 16:1 y relación de corte 1.8.

2. **Ejercicio 2:** Un motor de 6 cilindros produce 120 kW a 4000 RPM. Calcular el trabajo neto por cilindro por ciclo.

3. **Ejercicio 3:** Determinar el aumento porcentual de eficiencia al incrementar la relación de compresión de un motor Otto de 8:1 a 11:1.

---

## Ejercicios de Reforzamiento

### Ejercicio de Reforzamiento 1

**Problema:** Una flota de transporte está evaluando reemplazar sus camiones con motores Otto por motores Diesel. Compare el consumo de combustible teórico considerando:

- **Motor Otto:** Relación de compresión 10:1, eficiencia real 28%
- **Motor Diesel:** Relación de compresión 20:1, relación de corte 2.2, eficiencia real 38%
- **Poder calorífico gasolina:** 44 MJ/kg
- **Poder calorífico diesel:** 42 MJ/kg
- **Trabajo requerido:** 1000 kJ/s para cada camión

**Solución:**

**Consumo de combustible motor Otto:**
$$\dot{m}_{gasolina} = \frac{\dot{W}_{requerido}}{\eta_{real} \times PCI_{gasolina}} = \frac{1000}{0.28 \times 44000} = 0.0812 \text{ kg/s}$$

**Consumo de combustible motor Diesel:**
$$\dot{m}_{diesel} = \frac{\dot{W}_{requerido}}{\eta_{real} \times PCI_{diesel}} = \frac{1000}{0.38 \times 42000} = 0.0627 \text{ kg/s}$$

**Ahorro de combustible:**
$$\text{Ahorro} = \frac{0.0812 - 0.0627}{0.0812} \times 100\% = 22.8\%$$

**Conclusión:** Los motores Diesel consumen 22.8% menos combustible.

### Ejercicio de Reforzamiento 2

**Problema:** Un fabricante automotriz está desarrollando un motor Otto de alta compresión. Analizar el efecto de aumentar la relación de compresión de 9:1 a 12:1 en:
a) Eficiencia térmica teórica
b) Temperatura máxima del ciclo (T₁ = 300 K, T₂ calculada)

**Solución:**

**a) Eficiencias térmicas:**

**Para r = 9:1:**
$$\eta_1 = 1 - \frac{1}{9^{0.4}} = 1 - \frac{1}{2.408} = 0.585 = 58.5\%$$

**Para r = 12:1:**
$$\eta_2 = 1 - \frac{1}{12^{0.4}} = 1 - \frac{1}{2.635} = 0.620 = 62.0\%$$

**Aumento de eficiencia:**
$$\Delta\eta = 62.0\% - 58.5\% = 3.5\%$$

**b) Temperaturas máximas (proceso adiabático 1-2):**

$$T_2 = T_1 \times r^{\gamma-1}$$

**Para r = 9:1:**
$$T_{2a} = 300 \times 9^{0.4} = 300 \times 2.408 = 722 \text{ K}$$

**Para r = 12:1:**
$$T_{2b} = 300 \times 12^{0.4} = 300 \times 2.635 = 791 \text{ K}$$

**Aumento de temperatura:**
$$\Delta T = 791 - 722 = 69 \text{ K}$$

### Ejercicio de Reforzamiento 3

**Problema:** Un taller automotriz necesita determinar las especificaciones de un sistema de enfriamiento para dos tipos de motores:

- **Motor A (Otto):** 4 cilindros, 2.5 L, 4000 RPM, eficiencia 32%
- **Motor B (Diesel):** 4 cilindros, 2.8 L, 2500 RPM, eficiencia 42%

Si ambos motores producen la misma potencia (80 kW), calcular el calor que debe disipar el sistema de enfriamiento de cada uno.

**Solución:**

**Para ambos motores:**
$$\dot{W} = 80 \text{ kW}$$

**Energía total suministrada:**

**Motor A (Otto):**
$$\dot{Q}_{in,A} = \frac{\dot{W}}{\eta_A} = \frac{80}{0.32} = 250 \text{ kW}$$

**Motor B (Diesel):**
$$\dot{Q}_{in,B} = \frac{\dot{W}}{\eta_B} = \frac{80}{0.42} = 190.5 \text{ kW}$$

**Calor a disipar:**

**Motor A:**
$$\dot{Q}_{out,A} = \dot{Q}_{in,A} - \dot{W} = 250 - 80 = 170 \text{ kW}$$

**Motor B:**
$$\dot{Q}_{out,B} = \dot{Q}_{in,B} - \dot{W} = 190.5 - 80 = 110.5 \text{ kW}$$

**Conclusión:** El motor Otto requiere disipar 53.8% más calor que el motor Diesel.

---

## Conclusiones

1. **Diferencias fundamentales:** Los ciclos Otto y Diesel difieren principalmente en el **proceso de combustión**: Otto a **volumen constante** vs Diesel a **presión constante**, lo que determina sus características operativas distintivas.

2. **Eficiencia térmica:** Los **motores Diesel** presentan **mayor eficiencia térmica** debido a su **mayor relación de compresión** y al **proceso de combustión a presión constante**, resultando en menor consumo de combustible por unidad de trabajo producido.

3. **Aplicaciones específicas:** Los **motores Otto** son ideales para aplicaciones que requieren **alta velocidad** y **operación suave** (automóviles, motocicletas), mientras que los **motores Diesel** son superiores para aplicaciones de **alto torque** y **eficiencia energética** (camiones, autobuses, maquinaria pesada).

4. **Parámetros de diseño críticos:** La **relación de compresión** es el parámetro más influyente en la eficiencia de ambos ciclos, pero está limitada por consideraciones prácticas como el **knock** en motores Otto y las **presiones máximas** en motores Diesel.

5. **Tendencias tecnológicas:** La industria automotriz está desarrollando **tecnologías híbridas** que combinan las ventajas de ambos ciclos, como motores de **encendido por compresión controlado** (HCCI) y sistemas de **inyección directa** en motores de gasolina.

6. **Consideraciones ambientales:** Aunque los motores Diesel son más eficientes, presentan **mayores desafíos** en términos de **emisiones de NOₓ y partículas**, mientras que los motores Otto tienen **menores emisiones** de estos contaminantes pero **mayor producción de CO₂** por su menor eficiencia.

---

## Bibliografía

Çengel, Y. A., & Boles, M. A. (2019). *Termodinámica* (9ª ed.). McGraw-Hill Education.

Heywood, J. B. (2018). *Internal combustion engine fundamentals* (2nd ed.). McGraw-Hill Education.

Stone, R. (2012). *Introduction to internal combustion engines* (4th ed.). Palgrave Macmillan.

Ferguson, C. R., & Kirkpatrick, A. T. (2015). *Internal combustion engines: Applied thermosciences* (3rd ed.). John Wiley & Sons.

Borgnakke, C., & Sonntag, R. E. (2020). *Fundamentals of thermodynamics* (10th ed.). John Wiley & Sons.

Pulkrabek, W. W. (2003). *Engineering fundamentals of the internal combustion engine* (2nd ed.). Prentice Hall.

Martins, J. (2013). *Motores de combustão interna* (4ª ed.). Publindústria.