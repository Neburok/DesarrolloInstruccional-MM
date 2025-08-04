# AR.04.02.01 Problemario: Transferencia de Calor

## Instrucciones

Resuelva los siguientes problemas aplicando los conceptos y ecuaciones estudiadas en las lecturas de transferencia de calor. Identifique claramente el mecanismo de transferencia predominante, muestre todos los pasos de su solución y justifique las suposiciones realizadas.

**Datos útiles:**
- σ = 5.67 × 10⁻⁸ W/m²·K⁴ (constante de Stefan-Boltzmann)
- Conductividades térmicas típicas:
  - Hierro fundido: k = 52 W/m·K
  - Aluminio: k = 237 W/m·K
  - Acero inoxidable: k = 16 W/m·K
  - Vidrio: k = 0.78 W/m·K

---

## Problema 1: Conducción en Componentes Automotrices

Un **pistón de motor** está fabricado de **aleación de aluminio** con conductividad térmica **k = 180 W/m·K**. La **corona del pistón** tiene un espesor efectivo de **15 mm** y un área de transferencia de **0.008 m²**. Durante la operación, la superficie superior alcanza **350°C** debido a los gases de combustión, mientras que la superficie inferior (en contacto con el aceite) se mantiene a **120°C**.

Determine:
a) La **razón de transferencia de calor** por conducción a través de la corona del pistón
b) El **flujo de calor** (W/m²)
c) Si se cambia el material a **hierro fundido** (k = 52 W/m·K), ¿cuál sería la nueva razón de transferencia de calor?
d) ¿Qué material es mejor para la **gestión térmica** del pistón y por qué?

**Pistas:**
- Use la ley de Fourier para conducción unidimensional
- Compare los resultados para evaluar el efecto del material

---

## Problema 2: Convección en Sistema de Enfriamiento

El **radiador** de un automóvil tiene una superficie efectiva de **1.8 m²** expuesta al flujo de aire. Durante la operación en carretera a **100 km/h**, el aire fluye sobre el radiador a **25°C** con un **coeficiente de convección promedio h = 85 W/m²·K**. La superficie del radiador se mantiene a una **temperatura promedio de 75°C** mediante la circulación interna del refrigerante.

Determine:
a) La **razón de transferencia de calor** por convección del radiador al aire
b) Si el vehículo se detiene (velocidad = 0) y el coeficiente de convección se reduce a **h = 12 W/m²·K** (convección natural), ¿cuál sería la nueva razón de transferencia?
c) ¿En cuánto se **reduce** la capacidad de enfriamiento al detenerse?
d) Explique por qué los automóviles requieren **ventiladores eléctricos** para el enfriamiento en ralentí

**Pistas:**
- Use la ley de Newton del enfriamiento
- Compare los dos escenarios de operación

---

## Problema 3: Radiación en Sistema de Escape

Un **múltiple de escape** de acero inoxidable con **emisividad ε = 0.7** tiene una superficie exterior de **0.25 m²**. Durante la operación, la superficie alcanza una temperatura de **450°C**. El múltiple está ubicado en el compartimento del motor donde la temperatura ambiente promedio es **60°C**. Las superficies circundantes (chasis, carrocería) se consideran mucho más grandes que el múltiple.

Determine:
a) La **razón de pérdida de calor** por radiación del múltiple al ambiente
b) Si se aplica un **recubrimiento térmico** que reduce la emisividad a **ε = 0.3**, ¿cuál sería la nueva pérdida por radiación?
c) La **reducción porcentual** en la pérdida de calor con el recubrimiento
d) ¿Por qué es importante controlar la radiación en el compartimento del motor?

**Pistas:**
- Use temperaturas absolutas (Kelvin)
- Aplique la ley de Stefan-Boltzmann para radiación neta

---

## Problema 4: Transferencia Combinada en Frenos de Disco

Un **disco de freno ventilado** de hierro fundido tiene las siguientes características:
- **Espesor efectivo:** 25 mm
- **Área de fricción:** 0.15 m² (cada lado)
- **Área expuesta al aire:** 0.12 m² (superficie externa)
- **Conductividad térmica:** k = 52 W/m·K
- **Emisividad:** ε = 0.8

Durante una **frenada intensa**, la superficie de fricción alcanza **400°C**, mientras que la superficie externa expuesta al aire se mantiene a **250°C**. El aire ambiente está a **30°C** con un coeficiente de convección **h = 95 W/m²·K** debido al movimiento del vehículo.

Determine:
a) La **razón de transferencia de calor por conducción** desde la superficie de fricción hacia la superficie externa
b) La **razón de transferencia de calor por convección** desde la superficie externa al aire
c) La **razón de transferencia de calor por radiación** desde la superficie externa
d) La **razón total de disipación de calor** del disco
e) ¿Cuál mecanismo es más efectivo para el enfriamiento?

**Pistas:**
- Trate cada mecanismo por separado
- La transferencia total es la suma de convección y radiación desde la superficie externa

---

## Problema 5: Diseño Térmico Integrado

Un **ingeniero automotriz** está diseñando el sistema de **gestión térmica** para un **motor turboalimentado**. El **turbocompresor** genera una **potencia de calor de 15 kW** que debe ser disipada para mantener temperaturas operativas seguras. El sistema propuesto incluye:

**Componente 1: Carcasa del turbo**
- Material: Hierro fundido (k = 52 W/m·K)
- Espesor de pared: 12 mm
- Área de transferencia: 0.08 m²
- Temperatura interna: 650°C
- Temperatura externa de la carcasa: ?

**Componente 2: Intercambiador de calor aire-aire**
- Área efectiva: 0.6 m²
- Coeficiente de convección: h = 125 W/m²·K
- Temperatura del aire ambiente: 35°C
- Temperatura de la superficie del intercambiador: ?

**Componente 3: Radiación desde la carcasa**
- Emisividad: ε = 0.75
- Temperatura ambiente: 35°C

El sistema opera en **estado estacionario** donde toda la potencia generada debe ser disipada.

Determine:
a) La **temperatura de la superficie externa** de la carcasa del turbo
b) La **distribución de la disipación de calor** entre convección y radiación
c) Si el **coeficiente de convección se reduce a 60 W/m²·K** (baja velocidad), ¿cuál sería la nueva temperatura de la carcasa?
d) **Proponga mejoras** al diseño para mantener temperaturas seguras en todas las condiciones

**Pistas:**
- Use balance de energía: Qgenerado = Qconducción = Qconvección + Qradiación
- Plantee el sistema de ecuaciones considerando las temperaturas como incógnitas
- Resuelva iterativamente si es necesario

---

## Soluciones

### Solución Problema 1

**Dados:**
- k = 180 W/m·K (aluminio)
- L = 15 mm = 0.015 m
- A = 0.008 m²
- T₁ = 350°C, T₂ = 120°C

**a) Razón de transferencia de calor:**
Aplicando la ley de Fourier:
$$\dot{Q} = \frac{kA(T_1 - T_2)}{L} = \frac{180 \times 0.008 \times (350 - 120)}{0.015}$$
$$\dot{Q} = \frac{180 \times 0.008 \times 230}{0.015} = \frac{331.2}{0.015} = 22,080 \text{ W} = 22.08 \text{ kW}$$

**b) Flujo de calor:**
$$\dot{q} = \frac{\dot{Q}}{A} = \frac{22,080}{0.008} = 2,760,000 \text{ W/m}^2 = 2.76 \text{ MW/m}^2$$

**c) Con hierro fundido (k = 52 W/m·K):**
$$\dot{Q}_{hierro} = \frac{52 \times 0.008 \times 230}{0.015} = \frac{95.68}{0.015} = 6,379 \text{ W} = 6.38 \text{ kW}$$

**d) Comparación:**
El **aluminio** transfiere 3.46 veces más calor que el hierro fundido, siendo **mejor para la gestión térmica** ya que evacúa más eficientemente el calor de la corona del pistón, reduciendo temperaturas pico y el estrés térmico.

### Solución Problema 2

**Dados:**
- As = 1.8 m²
- Ts = 75°C, T∞ = 25°C
- h₁ = 85 W/m²·K (carretera)
- h₂ = 12 W/m²·K (parado)

**a) Transferencia en carretera:**
$$\dot{Q}_1 = h_1 A_s (T_s - T_\infty) = 85 \times 1.8 \times (75 - 25) = 85 \times 1.8 \times 50 = 7,650 \text{ W} = 7.65 \text{ kW}$$

**b) Transferencia parado:**
$$\dot{Q}_2 = h_2 A_s (T_s - T_\infty) = 12 \times 1.8 \times 50 = 1,080 \text{ W} = 1.08 \text{ kW}$$

**c) Reducción:**
$$\text{Reducción} = \frac{7.65 - 1.08}{7.65} \times 100\% = 85.9\%$$

**d) Los ventiladores compensan** la pérdida de convección forzada natural, manteniendo un flujo de aire adecuado para el enfriamiento cuando el vehículo está detenido.

### Solución Problema 3

**Dados:**
- ε = 0.7
- As = 0.25 m²
- Ts = 450°C = 723.15 K
- Talred = 60°C = 333.15 K

**a) Pérdida por radiación:**
$$\dot{Q}_{rad} = \varepsilon \sigma A_s (T_s^4 - T_{alred}^4)$$
$$\dot{Q}_{rad} = 0.7 \times 5.67 \times 10^{-8} \times 0.25 \times [(723.15)^4 - (333.15)^4]$$
$$\dot{Q}_{rad} = 0.7 \times 5.67 \times 10^{-8} \times 0.25 \times [2.735 \times 10^{11} - 1.234 \times 10^{10}]$$
$$\dot{Q}_{rad} = 9.92 \times 10^{-9} \times 2.612 \times 10^{11} = 2,591 \text{ W} = 2.59 \text{ kW}$$

**b) Con recubrimiento (ε = 0.3):**
$$\dot{Q}_{rad,nuevo} = \frac{0.3}{0.7} \times 2,591 = 1,111 \text{ W} = 1.11 \text{ kW}$$

**c) Reducción porcentual:**
$$\text{Reducción} = \frac{2.59 - 1.11}{2.59} \times 100\% = 57.1\%$$

---

*[Las soluciones de los problemas 4 y 5 seguirían el mismo formato detallado]*

## Criterios de Evaluación

- **Identificación del mecanismo correcto** (15%)
- **Aplicación correcta de ecuaciones** (25%)
- **Cálculos numéricos precisos** (30%)
- **Análisis e interpretación de resultados** (20%)
- **Presentación y organización** (10%)

## Referencias

Çengel, Y. A. (2020). *Heat and mass transfer: Fundamentals and applications* (6th ed.). McGraw-Hill Education.

Bergman, T. L., Lavine, A. S., Incropera, F. P., & DeWitt, D. P. (2017). *Fundamentals of heat and mass transfer* (8th ed.). John Wiley & Sons.