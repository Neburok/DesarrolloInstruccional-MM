# AD.04.01.01 - Ciclo de Carnot: Eficiencia Máxima Teórica

## Contenido

1. [Introducción](#introducción)
2. [Desarrollo](#desarrollo)
   - [Información Teórica](#información-teórica)
   - [Gráficos y Diagramas](#gráficos-y-diagramas)
   - [Fórmulas Fundamentales](#fórmulas-fundamentales)
   - [Ejemplos Resueltos](#ejemplos-resueltos)
   - [Ejercicios Propuestos](#ejercicios-propuestos)
3. [Ejercicios de Reforzamiento](#ejercicios-de-reforzamiento)
4. [Conclusiones](#conclusiones)
5. [Bibliografía](#bibliografía)

---

## Introducción

El **Ciclo de Carnot** representa el ciclo termodinámico más eficiente posible que puede operar entre dos reservorios térmicos a temperaturas constantes. Propuesto por Sadi Carnot en 1824, este ciclo teórico establece el límite superior de eficiencia para cualquier máquina térmica que opere entre dos fuentes de calor.

En el contexto de la **ingeniería automotriz**, comprender el ciclo de Carnot es fundamental para:
- Establecer los límites teóricos de eficiencia de los motores
- Comparar el rendimiento de motores reales con el ideal teórico
- Diseñar sistemas de refrigeración y climatización vehicular
- Optimizar la gestión térmica en vehículos híbridos y eléctricos

**Competencia a desarrollar:** *Identificar y representar el ciclo termodinámico de Carnot, calculando eficiencia, trabajo y transferencia de calor durante el ciclo desarrollado.*

---

## Desarrollo

### Información Teórica

#### Definición del Ciclo de Carnot

El **Ciclo de Carnot** es un ciclo termodinámico reversible que opera entre dos reservorios térmicos: una fuente caliente a temperatura $T_H$ y una fuente fría a temperatura $T_C$. Este ciclo consta de **cuatro procesos reversibles**:

1. **Proceso 1-2: Expansión isotérmica reversible** a temperatura $T_H$
2. **Proceso 2-3: Expansión adiabática reversible** 
3. **Proceso 3-4: Compresión isotérmica reversible** a temperatura $T_C$
4. **Proceso 4-1: Compresión adiabática reversible**

#### Principios Fundamentales de Carnot

**Primer Principio:** *Es imposible que una máquina térmica que opere en ciclos entre dos reservorios térmicos sea más eficiente que una máquina de Carnot que opere entre los mismos reservorios.*

**Segundo Principio:** *Todas las máquinas de Carnot reversibles que operen entre los mismos dos reservorios térmicos tienen la misma eficiencia.*

#### Características del Ciclo de Carnot

- **Reversibilidad completa:** Todos los procesos son **reversibles**
- **Eficiencia máxima:** Proporciona la **máxima eficiencia teórica** posible
- **Independencia del fluido de trabajo:** La eficiencia depende únicamente de las temperaturas de los reservorios
- **Aplicabilidad universal:** Válido para cualquier sustancia de trabajo

### Gráficos y Diagramas

#### Diagrama P-V (Presión-Volumen)

```
     P
     │
     │    1 ────────→ 2
     │    │             │
     │    │             ↓ (Expansión adiabática)
     │    ↑             │
     │    │             │
     │    4 ←────────── 3
     │________________________ V
           V₁  V₄    V₃  V₂
```

#### Diagrama T-S (Temperatura-Entropía)

```
     T
     │
  TH │ ────────────────────
     │ │1              2│
     │ │                │
     │ │4              3│
  TC │ ────────────────────
     │________________________ S
         S₁=S₄        S₂=S₃
```

### Fórmulas Fundamentales

#### Eficiencia del Ciclo de Carnot

La **eficiencia térmica** del ciclo de Carnot está dada por:

$$\eta_{Carnot} = 1 - \frac{T_C}{T_H}$$

Donde:
- $\eta_{Carnot}$ = Eficiencia del ciclo de Carnot (adimensional)
- $T_C$ = Temperatura absoluta del reservorio frío (K)
- $T_H$ = Temperatura absoluta del reservorio caliente (K)

#### Trabajo Neto del Ciclo

$$W_{neto} = Q_H - Q_C$$

$$W_{neto} = Q_H \left(1 - \frac{T_C}{T_H}\right)$$

#### Relación de Calores

Para el ciclo de Carnot reversible:

$$\frac{Q_H}{T_H} = \frac{Q_C}{T_C}$$

Por lo tanto:

$$Q_C = Q_H \frac{T_C}{T_H}$$

#### Coeficiente de Rendimiento (COP) para Refrigeración

$$COP_{refrigeración} = \frac{T_C}{T_H - T_C}$$

#### Coeficiente de Rendimiento (COP) para Bomba de Calor

$$COP_{bomba\_de\_calor} = \frac{T_H}{T_H - T_C}$$

### Ejemplos Resueltos

#### Ejemplo 1: Cálculo de Eficiencia de una Máquina de Carnot

**Problema:** Una máquina térmica de Carnot opera entre un reservorio caliente a 800 K y un reservorio frío a 300 K. Calcular:
a) La eficiencia térmica
b) El trabajo producido si absorbe 1000 kJ de calor del reservorio caliente
c) El calor rechazado al reservorio frío

**Solución:**

**Datos:**
- $T_H = 800$ K
- $T_C = 300$ K  
- $Q_H = 1000$ kJ

**a) Eficiencia térmica:**

$$\eta_{Carnot} = 1 - \frac{T_C}{T_H} = 1 - \frac{300}{800} = 1 - 0.375 = 0.625$$

$$\eta_{Carnot} = 62.5\%$$

**b) Trabajo producido:**

$$W_{neto} = \eta_{Carnot} \times Q_H = 0.625 \times 1000 = 625 \text{ kJ}$$

**c) Calor rechazado:**

$$Q_C = Q_H - W_{neto} = 1000 - 625 = 375 \text{ kJ}$$

**Verificación:**
$$Q_C = Q_H \frac{T_C}{T_H} = 1000 \times \frac{300}{800} = 375 \text{ kJ} \checkmark$$

#### Ejemplo 2: Aplicación Automotriz - Sistema de Refrigeración

**Problema:** Un sistema de aire acondicionado automotriz opera como un ciclo de Carnot inverso entre el habitáculo a 20°C y el ambiente exterior a 35°C. Calcular el COP del sistema.

**Solución:**

**Datos:**
- $T_C = 20°C = 293.15$ K (habitáculo)
- $T_H = 35°C = 308.15$ K (ambiente exterior)

**COP para refrigeración:**

$$COP_{refrigeración} = \frac{T_C}{T_H - T_C} = \frac{293.15}{308.15 - 293.15} = \frac{293.15}{15} = 19.54$$

**Interpretación:** Por cada unidad de trabajo invertida, el sistema puede extraer 19.54 unidades de calor del habitáculo. Este valor representa el **límite teórico máximo** para este rango de temperaturas.

### Ejercicios Propuestos

1. **Ejercicio 1:** Una máquina de Carnot opera entre 1000 K y 400 K. Si produce 300 kJ de trabajo, calcular el calor absorbido y rechazado.

2. **Ejercicio 2:** Determinar la temperatura mínima del reservorio caliente para que una máquina de Carnot tenga una eficiencia del 75%, si el reservorio frío está a 25°C.

3. **Ejercicio 3:** Comparar la eficiencia de una máquina de Carnot con un motor Otto real que tiene una eficiencia del 35%, operando entre las mismas temperaturas (TH = 600 K, TC = 300 K).

---

## Ejercicios de Reforzamiento

### Ejercicio de Reforzamiento 1

**Problema:** Un refrigerador automotriz opera según un ciclo de Carnot inverso entre -10°C (compartimento de congelación) y 25°C (temperatura ambiente del vehículo). Si se requiere extraer 5 kJ/min del compartimento de congelación, calcular:

a) El COP del refrigerador
b) La potencia mínima requerida
c) El calor rechazado al ambiente

**Solución:**

**Datos:**
- $T_C = -10°C = 263.15$ K
- $T_H = 25°C = 298.15$ K
- $\dot{Q}_C = 5$ kJ/min = $\frac{5}{60}$ kW = 0.0833 kW

**a) COP del refrigerador:**
$$COP = \frac{T_C}{T_H - T_C} = \frac{263.15}{298.15 - 263.15} = \frac{263.15}{35} = 7.52$$

**b) Potencia mínima requerida:**
$$\dot{W} = \frac{\dot{Q}_C}{COP} = \frac{0.0833}{7.52} = 0.0111 \text{ kW} = 11.1 \text{ W}$$

**c) Calor rechazado:**
$$\dot{Q}_H = \dot{Q}_C + \dot{W} = 0.0833 + 0.0111 = 0.0944 \text{ kW}$$

### Ejercicio de Reforzamiento 2

**Problema:** Se desea diseñar una máquina térmica que opere entre los gases de escape de un motor (550°C) y el aire ambiente (20°C). Si la máquina debe producir 10 kW de potencia y opera como un ciclo de Carnot:

a) Calcular la eficiencia máxima posible
b) Determinar el flujo de calor requerido de los gases de escape
c) Calcular el calor rechazado al ambiente

**Solución:**

**Datos:**
- $T_H = 550°C = 823.15$ K
- $T_C = 20°C = 293.15$ K  
- $\dot{W} = 10$ kW

**a) Eficiencia máxima:**
$$\eta_{max} = 1 - \frac{T_C}{T_H} = 1 - \frac{293.15}{823.15} = 1 - 0.356 = 0.644 = 64.4\%$$

**b) Flujo de calor de los gases de escape:**
$$\dot{Q}_H = \frac{\dot{W}}{\eta} = \frac{10}{0.644} = 15.53 \text{ kW}$$

**c) Calor rechazado al ambiente:**
$$\dot{Q}_C = \dot{Q}_H - \dot{W} = 15.53 - 10 = 5.53 \text{ kW}$$

### Ejercicio de Reforzamiento 3

**Problema:** Un sistema de calefacción vehicular utiliza una bomba de calor que opera según un ciclo de Carnot entre el aire exterior a -5°C y el habitáculo a 22°C. Si se requiere suministrar 3 kW de calefacción:

a) Calcular el COP de la bomba de calor
b) Determinar la potencia eléctrica consumida
c) Calcular el calor extraído del aire exterior

**Solución:**

**Datos:**
- $T_C = -5°C = 268.15$ K (aire exterior)
- $T_H = 22°C = 295.15$ K (habitáculo)
- $\dot{Q}_H = 3$ kW

**a) COP de la bomba de calor:**
$$COP_{BC} = \frac{T_H}{T_H - T_C} = \frac{295.15}{295.15 - 268.15} = \frac{295.15}{27} = 10.93$$

**b) Potencia eléctrica consumida:**
$$\dot{W} = \frac{\dot{Q}_H}{COP} = \frac{3}{10.93} = 0.274 \text{ kW} = 274 \text{ W}$$

**c) Calor extraído del aire exterior:**
$$\dot{Q}_C = \dot{Q}_H - \dot{W} = 3 - 0.274 = 2.726 \text{ kW}$$

---

## Conclusiones

1. **Límite teórico de eficiencia:** El ciclo de Carnot establece el **límite superior absoluto** de eficiencia para cualquier máquina térmica que opere entre dos reservorios térmicos, proporcionando una referencia fundamental para evaluar el desempeño de motores reales.

2. **Dependencia únicamente de temperaturas:** La eficiencia del ciclo de Carnot depende **exclusivamente** de las temperaturas absolutas de los reservorios térmicos, siendo independiente del tipo de fluido de trabajo o del diseño específico de la máquina.

3. **Aplicaciones en ingeniería automotriz:** Los principios del ciclo de Carnot son **fundamentales** para:
   - Evaluar la eficiencia límite de motores de combustión interna
   - Diseñar sistemas de aire acondicionado y calefacción vehicular
   - Optimizar sistemas de recuperación de calor de gases de escape
   - Desarrollar tecnologías de gestión térmica en vehículos híbridos y eléctricos

4. **Reversibilidad y eficiencia:** La **reversibilidad completa** del ciclo de Carnot es la clave de su máxima eficiencia, aunque en la práctica es imposible de alcanzar debido a las irreversibilidades inherentes en todos los procesos reales.

5. **Herramienta de comparación:** El ciclo de Carnot sirve como **estándar de referencia** para comparar y evaluar el desempeño de ciclos termodinámicos reales, permitiendo identificar áreas de mejora en el diseño de sistemas térmicos automotrices.

---

## Bibliografía

Çengel, Y. A., & Boles, M. A. (2019). *Termodinámica* (9ª ed.). McGraw-Hill Education. https://www.mheducation.com

Moran, M. J., Shapiro, H. N., Boettner, D. D., & Bailey, M. B. (2018). *Fundamentals of engineering thermodynamics* (9th ed.). John Wiley & Sons.

Bejan, A. (2016). *Advanced engineering thermodynamics* (4th ed.). John Wiley & Sons.

Stone, R. (2012). *Introduction to internal combustion engines* (4th ed.). Palgrave Macmillan.

Heywood, J. B. (2018). *Internal combustion engine fundamentals* (2nd ed.). McGraw-Hill Education.

Borgnakke, C., & Sonntag, R. E. (2020). *Fundamentals of thermodynamics* (10th ed.). John Wiley & Sons.