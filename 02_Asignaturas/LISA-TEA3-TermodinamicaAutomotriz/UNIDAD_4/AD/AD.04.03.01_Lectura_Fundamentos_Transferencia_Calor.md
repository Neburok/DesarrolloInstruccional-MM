# AD.04.03.01 - Fundamentos de Transferencia de Calor en Sistemas Automotrices

## Contenido

1. [Introducción](#introducción)
2. [Desarrollo](#desarrollo)
   - [Transferencia de Calor vs Termodinámica](#transferencia-de-calor-vs-termodinámica)
   - [Conceptos Fundamentales](#conceptos-fundamentales)
   - [Primera Ley de la Termodinámica aplicada](#primera-ley-de-la-termodinámica-aplicada)
   - [Los Tres Mecanismos de Transferencia](#los-tres-mecanismos-de-transferencia)
   - [Aplicaciones en Ingeniería Automotriz](#aplicaciones-en-ingeniería-automotriz)
   - [Fórmulas Fundamentales](#fórmulas-fundamentales)
   - [Ejemplos Resueltos](#ejemplos-resueltos)
   - [Ejercicios Propuestos](#ejercicios-propuestos)
3. [Ejercicios de Reforzamiento](#ejercicios-de-reforzamiento)
4. [Conclusiones](#conclusiones)
5. [Bibliografía](#bibliografía)

---

## Introducción

La **transferencia de calor** es una disciplina fundamental en la ingeniería automotriz que se ocupa de la **rapidez o razón de transferencia de energía térmica**. En el contexto vehicular, el manejo eficiente del calor es crucial para:

- **Gestión térmica del motor:** Control de temperaturas operativas óptimas
- **Sistemas de climatización:** Calefacción y aire acondicionado vehicular  
- **Refrigeración de componentes:** Radiadores, intercoolers, enfriamiento de frenos
- **Eficiencia energética:** Recuperación de calor residual y optimización térmica
- **Durabilidad de componentes:** Prevención de sobrecalentamientos y degradación térmica

A diferencia de la **termodinámica**, que se enfoca en los **estados de equilibrio** y las cantidades de energía transferida, la transferencia de calor se centra en la **velocidad** de estos procesos térmicos y los **mecanismos** que los gobiernan.

**Competencia a desarrollar:** *Comprender y aplicar los principios fundamentales de transferencia de calor para analizar y diseñar sistemas térmicos automotrices eficientes.*

---

## Desarrollo

### Transferencia de Calor vs Termodinámica

#### Distinción Fundamental

**Termodinámica:**
- Se enfoca en la **cantidad de transferencia de calor** entre estados de equilibrio
- Determina **cuánta energía** se transfiere cuando un sistema cambia de estado
- **No indica el tiempo** requerido para el proceso
- Ejemplo: *¿Cuánto calor debe extraerse para enfriar el refrigerante del motor de 90°C a 80°C?*

**Transferencia de Calor:**
- Se interesa en la **rapidez o razón** (por unidad de tiempo) de la transferencia
- Fundamental para el **diseño de equipos térmicos** automotrices
- Analiza sistemas en **desequilibrio térmico**
- Ejemplo: *¿Qué tan rápido se enfría el refrigerante y qué tamaño de radiador se necesita?*

#### Requisito Básico

El **requisito fundamental** para la transferencia de calor es la existencia de una **diferencia de temperatura** ($\Delta T$). La energía térmica **siempre** se transfiere:

- Del medio de **mayor temperatura** al de **menor temperatura**
- El proceso se detiene cuando se alcanza el **equilibrio térmico**
- **Mayor gradiente de temperatura** → **mayor razón de transferencia**

### Conceptos Fundamentales

#### Formas de Energía Térmica

La **energía interna** ($U$) de un sistema comprende varias formas microscópicas:

**Energía Sensible:**
- Asociada con la **energía cinética** de las moléculas
- **Proporcional a la temperatura** del sistema
- En automotriz: calor almacenado en el bloque del motor, refrigerante

**Energía Latente:**
- Asociada con **cambios de fase** (sólido-líquido-gas)
- Se requiere para **vencer fuerzas intermoleculares**
- En automotriz: evaporación/condensación en sistemas A/C

**Energía Química:**
- Energía de **enlaces moleculares**
- En automotriz: energía almacenada en combustibles

#### Nomenclatura Térmica

**Cantidad de Calor Transferido:**
$$Q = \text{Energía térmica total transferida (J o kJ)}$$

**Razón de Transferencia de Calor:**
$$\dot{Q} = \frac{dQ}{dt} \text{ (W o kW)}$$

Si $\dot{Q}$ es constante:
$$Q = \dot{Q} \cdot \Delta t$$

**Flujo de Calor:**
$$\dot{q} = \frac{\dot{Q}}{A} \text{ (W/m²)}$$

Donde $A$ es el área perpendicular a la dirección de transferencia.

### Primera Ley de la Termodinámica Aplicada

#### Principio de Conservación de Energía

La **Primera Ley** establece que la energía no se crea ni se destruye, solo cambia de forma:

$$E_{entrada} - E_{salida} = \Delta E_{sistema}$$

#### Balance de Energía Térmica

Para análisis de transferencia de calor:

$$Q_{entrada} - Q_{salida} + E_{generada} = \Delta E_{térmica,sistema}$$

#### Aplicaciones Automotrices

**Sistemas Cerrados (Motor):**
Para un bloque de motor con masa fija:
$$Q = m c_v \Delta T$$

**Sistemas de Flujo Estacionario (Radiador):**
Para refrigerante fluyendo a través del radiador:
$$\dot{Q} = \dot{m} c_p \Delta T$$

Donde:
- $\dot{m} = \rho V A_c$ = gasto másico (kg/s)
- $\rho$ = densidad del fluido
- $V$ = velocidad promedio
- $A_c$ = área de sección transversal

### Los Tres Mecanismos de Transferencia

#### 1. Conducción

La **conducción** es la transferencia de energía de partículas más energéticas a las menos energéticas mediante **interacción directa**.

**Características:**
- Ocurre en **sólidos, líquidos y gases**
- En sólidos: **vibraciones moleculares** + **electrones libres**
- En fluidos: **colisiones moleculares** durante movimiento aleatorio

**Ley de Fourier:**
$$\dot{Q}_{cond} = -k A \frac{dT}{dx}$$

Para geometría plana:
$$\dot{Q}_{cond} = \frac{k A \Delta T}{L}$$

Donde:
- $k$ = conductividad térmica (W/m·K)
- $A$ = área de transferencia (m²)
- $L$ = espesor (m)
- $\Delta T$ = diferencia de temperatura (K)

**Conductividad Térmica en Automotriz:**
- **Metales** (bloque motor): $k = 50-400$ W/m·K
- **Aleaciones** (radiador): $k = 20-200$ W/m·K  
- **Fluidos** (refrigerante): $k = 0.3-0.7$ W/m·K
- **Aislantes** (revestimientos): $k = 0.02-0.2$ W/m·K

**Difusividad Térmica:**
$$\alpha = \frac{k}{\rho c_p} \text{ (m²/s)}$$

Representa la **rapidez de propagación** del calor en el material.

#### 2. Convección

La **convección** es la transferencia entre una **superficie sólida** y un **fluido en movimiento**, combinando **conducción** y **movimiento del fluido**.

**Tipos de Convección:**

**Convección Forzada:**
- Fluido forzado por medios externos (bombas, ventiladores)
- Ejemplos: bomba de agua, ventilador del radiador

**Convección Natural:**
- Movimiento inducido por **diferencias de densidad** debido a variaciones de temperatura
- Ejemplos: enfriamiento natural del motor apagado

**Ley de Newton del Enfriamiento:**
$$\dot{Q}_{conv} = h A_s (T_s - T_\infty)$$

Donde:
- $h$ = coeficiente de transferencia por convección (W/m²·K)
- $A_s$ = área superficial (m²)
- $T_s$ = temperatura de la superficie (K)
- $T_\infty$ = temperatura del fluido alejado (K)

**Valores Típicos de $h$ en Automotriz:**
- **Convección natural** (aire): $h = 5-25$ W/m²·K
- **Convección forzada** (aire): $h = 10-200$ W/m²·K
- **Convección forzada** (agua/refrigerante): $h = 100-15000$ W/m²·K

#### 3. Radiación

La **radiación** es la energía emitida como **ondas electromagnéticas** debido a la temperatura del material.

**Características:**
- **No requiere medio material** (funciona en el vacío)
- **Velocidad de la luz** (modo más rápido)
- Todos los cuerpos > 0 K emiten radiación térmica

**Ley de Stefan-Boltzmann:**
$$\dot{Q}_{emitida} = \varepsilon \sigma A_s T_s^4$$

**Radiación Neta:**
$$\dot{Q}_{rad} = \varepsilon \sigma A_s (T_s^4 - T_{alrededores}^4)$$

Donde:
- $\varepsilon$ = emisividad (0 ≤ ε ≤ 1)
- $\sigma = 5.67 \times 10^{-8}$ W/m²·K⁴ (constante Stefan-Boltzmann)
- **Temperaturas en Kelvin absoluto**

**Emisividades Típicas:**
- **Superficies metálicas pulidas**: $\varepsilon = 0.02-0.10$
- **Superficies oxidadas**: $\varepsilon = 0.60-0.85$
- **Superficies pintadas**: $\varepsilon = 0.80-0.95$

### Aplicaciones en Ingeniería Automotriz

#### Sistema de Refrigeración del Motor

**Componentes y Mecanismos:**
1. **Bloque del motor**: Conducción desde cilindros al refrigerante
2. **Radiador**: Convección forzada aire-refrigerante
3. **Mangueras**: Conducción a través de las paredes
4. **Superficies exteriores**: Radiación al ambiente

#### Sistema de Climatización

**Evaporador (Interior del vehículo):**
- **Convección forzada**: Aire del habitáculo → superficie del evaporador
- **Cambio de fase**: Evaporación del refrigerante (energía latente)

**Condensador (Exterior del vehículo):**
- **Cambio de fase**: Condensación del refrigerante
- **Convección forzada**: Superficie → aire ambiente
- **Radiación**: Superficies calientes → ambiente

#### Sistema de Frenos

**Discos de freno:**
- **Generación de calor**: Energía cinética → térmica por fricción
- **Conducción**: A través del disco de freno
- **Convección**: Disipación al aire (natural y forzada)
- **Radiación**: Significativa a altas temperaturas

### Fórmulas Fundamentales

#### Resistencia Térmica

**Analogía eléctrica** para análisis térmico:

**Conducción:**
$$R_{cond} = \frac{L}{k A}$$

**Convección:**
$$R_{conv} = \frac{1}{h A}$$

**Radiación:**
$$R_{rad} = \frac{1}{h_r A}$$

Donde: $h_r = \varepsilon \sigma (T_s + T_\infty)(T_s^2 + T_\infty^2)$

#### Resistencias en Serie y Paralelo

**Serie:**
$$R_{total} = R_1 + R_2 + R_3 + ...$$

**Paralelo:**
$$\frac{1}{R_{total}} = \frac{1}{R_1} + \frac{1}{R_2} + \frac{1}{R_3} + ...$$

### Ejemplos Resueltos

#### Ejemplo 1: Transferencia en Pared del Cilindro

**Problema:** La pared de un cilindro de motor tiene un espesor de 8 mm y está hecha de hierro fundido ($k = 52$ W/m·K). La superficie interior está a 180°C y la exterior (en contacto con refrigerante) a 95°C. El área de transferencia es 0.015 m². Calcular la razón de transferencia de calor por conducción.

**Solución:**

**Datos:**
- $L = 8$ mm $= 0.008$ m
- $k = 52$ W/m·K
- $T_1 = 180°C$, $T_2 = 95°C$
- $A = 0.015$ m²

**Aplicando la Ley de Fourier:**
$$\dot{Q} = \frac{k A (T_1 - T_2)}{L} = \frac{52 \times 0.015 \times (180-95)}{0.008}$$

$$\dot{Q} = \frac{52 \times 0.015 \times 85}{0.008} = \frac{66.3}{0.008} = 8288 \text{ W}$$

**Resultado:** $\dot{Q} = 8.29$ kW

#### Ejemplo 2: Convección en Radiador Automotriz

**Problema:** Un radiador tiene una superficie de transferencia de 2.5 m² expuesta al aire. La temperatura superficial promedio es 85°C y el aire ambiente está a 25°C. Si el coeficiente de convección es 45 W/m²·K, calcular la transferencia de calor.

**Solución:**

**Datos:**
- $A_s = 2.5$ m²
- $T_s = 85°C$
- $T_\infty = 25°C$
- $h = 45$ W/m²·K

**Aplicando la Ley de Newton del Enfriamiento:**
$$\dot{Q} = h A_s (T_s - T_\infty) = 45 \times 2.5 \times (85-25)$$

$$\dot{Q} = 45 \times 2.5 \times 60 = 6750 \text{ W}$$

**Resultado:** $\dot{Q} = 6.75$ kW

#### Ejemplo 3: Radiación de Colector de Escape

**Problema:** Un colector de escape con área superficial 0.8 m² y emisividad 0.7 está a 400°C. Está rodeado por el compartimiento del motor a 80°C. Calcular la pérdida de calor por radiación.

**Solución:**

**Datos:**
- $A_s = 0.8$ m²
- $\varepsilon = 0.7$
- $T_s = 400°C = 673.15$ K
- $T_{alr} = 80°C = 353.15$ K
- $\sigma = 5.67 \times 10^{-8}$ W/m²·K⁴

**Aplicando la ecuación de radiación neta:**
$$\dot{Q}_{rad} = \varepsilon \sigma A_s (T_s^4 - T_{alr}^4)$$

$$\dot{Q}_{rad} = 0.7 \times 5.67 \times 10^{-8} \times 0.8 \times (673.15^4 - 353.15^4)$$

$$\dot{Q}_{rad} = 3.17 \times 10^{-8} \times (2.06 \times 10^{11} - 1.55 \times 10^{10})$$

$$\dot{Q}_{rad} = 3.17 \times 10^{-8} \times 1.91 \times 10^{11} = 6044 \text{ W}$$

**Resultado:** $\dot{Q}_{rad} = 6.04$ kW

### Ejercicios Propuestos

1. **Ejercicio 1:** Un intercooler de turbo tiene paredes de aluminio de 3 mm de espesor. Si la temperatura del aire caliente es 120°C y del aire frío 40°C, calcular la razón de transferencia por conducción. ($k_{Al} = 237$ W/m·K, $A = 0.5$ m²)

2. **Ejercicio 2:** Calcular el coeficiente de convección requerido en un radiador de 3 m² para disipar 15 kW cuando la diferencia de temperatura superficie-aire es 50°C.

3. **Ejercicio 3:** Comparar las pérdidas por radiación y convección de un múltiple de escape a 350°C con $\varepsilon = 0.8$, $A = 0.6$ m², rodeado por aire a 30°C con $h = 25$ W/m²·K.

---

## Ejercicios de Reforzamiento

### Ejercicio de Reforzamiento 1

**Problema:** Un sistema de gestión térmica de batería en vehículo eléctrico debe mantener las celdas a temperatura óptima. Analizar la transferencia de calor en una placa de refrigeración:

- **Material:** Aluminio, $k = 200$ W/m·K
- **Dimensiones:** 300 mm × 200 mm × 5 mm de espesor
- **Temperatura lado caliente:** 45°C (batería)
- **Temperatura lado frío:** 25°C (refrigerante)

Calcular:
a) La razón de transferencia de calor por conducción
b) La resistencia térmica de la placa
c) El flujo de calor por unidad de área

**Solución:**

**a) Razón de transferencia de calor:**

**Datos:**
- $k = 200$ W/m·K
- $L = 5$ mm $= 0.005$ m
- $A = 0.3 \times 0.2 = 0.06$ m²
- $\Delta T = 45 - 25 = 20°C$

$$\dot{Q} = \frac{k A \Delta T}{L} = \frac{200 \times 0.06 \times 20}{0.005} = 48,000 \text{ W} = 48 \text{ kW}$$

**b) Resistencia térmica:**
$$R_{cond} = \frac{L}{k A} = \frac{0.005}{200 \times 0.06} = 4.17 \times 10^{-4} \text{ K/W}$$

**c) Flujo de calor:**
$$\dot{q} = \frac{\dot{Q}}{A} = \frac{48,000}{0.06} = 800,000 \text{ W/m²} = 800 \text{ kW/m²}$$

### Ejercicio de Reforzamiento 2

**Problema:** Un radiador de aceite de transmisión debe disipar 5 kW mediante convección natural. Determinar el área superficial requerida si:

- **Temperatura superficie:** 90°C
- **Temperatura aire:** 35°C  
- **Coeficiente convección natural:** 12 W/m²·K
- **Factor de seguridad:** 1.3

**Solución:**

**Datos:**
- $\dot{Q}_{requerida} = 5$ kW $= 5000$ W
- $T_s = 90°C$
- $T_\infty = 35°C$
- $h = 12$ W/m²·K
- Factor seguridad $= 1.3$

**Área teórica requerida:**
$$A_s = \frac{\dot{Q}}{h (T_s - T_\infty)} = \frac{5000}{12 \times (90-35)} = \frac{5000}{12 \times 55} = 7.58 \text{ m²}$$

**Área con factor de seguridad:**
$$A_{diseño} = 1.3 \times 7.58 = 9.85 \text{ m²}$$

**Resultado:** Se requiere un área superficial de **9.85 m²**

### Ejercicio de Reforzamiento 3

**Problema:** Análisis térmico comparativo de sistema de frenos. Un disco de freno genera 8 kW durante el frenado. Compare la disipación por convección y radiación:

**Condiciones:**
- **Temperatura disco:** 300°C
- **Temperatura ambiente:** 20°C
- **Área efectiva:** 0.15 m² (cada cara)
- **Emisividad:** 0.6
- **Coeficiente convección:** 80 W/m²·K (aire forzado)

**Solución:**

**Datos:**
- $T_s = 300°C = 573.15$ K
- $T_\infty = 20°C = 293.15$ K
- $A = 2 \times 0.15 = 0.3$ m² (ambas caras)
- $\varepsilon = 0.6$
- $h = 80$ W/m²·K

**Disipación por convección:**
$$\dot{Q}_{conv} = h A (T_s - T_\infty) = 80 \times 0.3 \times (300-20) = 6,720 \text{ W}$$

**Disipación por radiación:**
$$\dot{Q}_{rad} = \varepsilon \sigma A (T_s^4 - T_\infty^4)$$
$$\dot{Q}_{rad} = 0.6 \times 5.67 \times 10^{-8} \times 0.3 \times (573.15^4 - 293.15^4)$$
$$\dot{Q}_{rad} = 1.02 \times 10^{-8} \times (1.08 \times 10^{11} - 7.37 \times 10^{9}) = 1,030 \text{ W}$$

**Disipación total:**
$$\dot{Q}_{total} = 6,720 + 1,030 = 7,750 \text{ W} = 7.75 \text{ kW}$$

**Análisis:**
- **Convección:** 86.7% de la disipación total
- **Radiación:** 13.3% de la disipación total
- **Capacidad total:** 7.75 kW vs 8 kW generados
- **Déficit:** 0.25 kW (necesario mejorar ventilación)

---

## Conclusiones

1. **Fundamentos aplicados:** Los principios de transferencia de calor son **esenciales** para el diseño y optimización de sistemas térmicos automotrices, desde la gestión térmica del motor hasta los sistemas de climatización y frenado.

2. **Mecanismos combinados:** En aplicaciones automotrices **raramente** ocurre un solo mecanismo de transferencia; la **conducción, convección y radiación** actúan simultáneamente, requiriendo análisis integral para optimización térmica.

3. **Diseño basado en resistencias térmicas:** La **analogía eléctrica** con resistencias térmicas proporciona una herramienta poderosa para el análisis y diseño de sistemas de gestión térmica vehicular, facilitando la identificación de cuellos de botella térmicos.

4. **Importancia de la convección forzada:** En sistemas automotrices, la **convección forzada** mediante ventiladores y bombas es frecuentemente el mecanismo **dominante** en la disipación de calor, siendo crucial para el dimensionamiento adecuado de equipos.

5. **Gestión térmica integral:** La **eficiencia energética** de vehículos modernos depende críticamicamente de una gestión térmica optimizada que considere la **recuperación de calor residual**, **minimización de pérdidas** y **control preciso de temperaturas operativas**.

6. **Consideraciones de diseño:** El análisis de transferencia de calor permite **predicir comportamientos térmicos**, **dimensionar componentes** apropiadamente y **prevenir fallas** por sobrecalentamiento, siendo fundamental para la confiabilidad y durabilidad vehicular.

---

## Bibliografía

Çengel, Y. A., & Ghajar, A. J. (2020). *Heat and mass transfer: Fundamentals and applications* (6th ed.). McGraw-Hill Education.

Incropera, F. P., DeWitt, D. P., Bergman, T. L., & Lavine, A. S. (2017). *Fundamentals of heat and mass transfer* (8th ed.). John Wiley & Sons.

Holman, J. P. (2010). *Heat transfer* (10th ed.). McGraw-Hill Education.

Lienhard, J. H., & Lienhard, J. H. (2019). *A heat transfer textbook* (5th ed.). Phlogiston Press.

Stone, R. (2012). *Introduction to internal combustion engines* (4th ed.). Palgrave Macmillan.

Wong, J. Y. (2001). *Theory of ground vehicles* (3rd ed.). John Wiley & Sons.

Reif, K. (Ed.). (2014). *Automotive handbook* (9th ed.). Robert Bosch GmbH.