# Guía de Ejercicios Resueltos: Transferencia de Calor

**Asignatura:** Termodinámica Automotriz
**Unidad 4:** Procesos Termodinámicos y de Transferencia de Calor

---

### Introducción

Esta guía de ejercicios está diseñada para reforzar su comprensión de los mecanismos de transferencia de calor: conducción, convección y radiación. La resolución de estos problemas le permitirá aplicar las leyes fundamentales y desarrollar sus habilidades de cálculo en contextos relevantes para la ingeniería automotriz. Cada ejercicio incluye una solución detallada paso a paso para facilitar su aprendizaje.

---

### Ejercicio 1: Conducción a través de una Pared Plana

Una pared de un cilindro de motor de $0.5 \, cm$ de espesor está hecha de un material con una conductividad térmica de $k = 45 \, W/m \cdot K$. La temperatura de la superficie interior de la pared es de $800^\circ C$ y la de la superficie exterior es de $150^\circ C$. El área de la superficie de la pared es de $0.01 \, m^2$.

Calcule la tasa de transferencia de calor por conducción a través de esta pared.

#### Solución Detallada

Para calcular la tasa de transferencia de calor por conducción a través de una pared plana, utilizamos la Ley de Fourier:

$$ Q_{cond} = -k A \frac{dT}{dx} $$

Para una pared plana, el gradiente de temperatura $\frac{dT}{dx}$ se puede aproximar como $\frac{\Delta T}{\Delta x}$, donde $\Delta T = T_{exterior} - T_{interior}$ y $\Delta x$ es el espesor de la pared. Sin embargo, para obtener un valor positivo de $Q_{cond}$ (que representa el flujo de calor desde la temperatura más alta a la más baja), es más práctico usar la diferencia de temperatura positiva $(T_{interior} - T_{exterior})$.

$$ Q_{cond} = k A \frac{T_{interior} - T_{exterior}}{\Delta x} $$

**Datos:**
-   Conductividad térmica ($k$) = $45 \, W/m \cdot K$
-   Espesor ($\Delta x$) = $0.5 \, cm = 0.005 \, m$
-   Temperatura interior ($T_{interior}$) = $800^\circ C$
-   Temperatura exterior ($T_{exterior}$) = $150^\circ C$
-   Área ($A$) = $0.01 \, m^2$

**Cálculo:**

$$ Q_{cond} = (45 \, W/m \cdot K)(0.01 \, m^2) \frac{(800 - 150) \, ^\circ C}{0.005 \, m} $$

$$ Q_{cond} = (0.45 \, W/K) \frac{650 \, ^\circ C}{0.005 \, m} $$

$$ Q_{cond} = 0.45 \times 130,000 \, W = 58,500 \, W = 58.5 \, kW $$

La tasa de transferencia de calor por conducción a través de la pared del cilindro es de $58.5 \, kW$.

---

### Ejercicio 2: Convección en un Radiador de Automóvil

Un radiador de automóvil tiene una superficie de $0.8 \, m^2$ y su temperatura superficial promedio es de $90^\circ C$. El aire que fluye a través del radiador está a $25^\circ C$. Si el coeficiente de transferencia de calor por convección es de $120 \, W/m^2 \cdot K$, ¿cuál es la tasa de transferencia de calor por convección del radiador al aire?

#### Solución Detallada

Para calcular la tasa de transferencia de calor por convección, utilizamos la Ley de Enfriamiento de Newton:

$ Q_{conv} = h A (T_s - T_\infty) $

**Datos:**
-   Coeficiente de transferencia de calor por convección ($h$) = $120 \, W/m^2 \cdot K$
-   Área ($A$) = $0.8 \, m^2$
-   Temperatura de la superficie ($T_s$) = $90^\circ C$
-   Temperatura del fluido ($T_\infty$) = $25^\circ C$

**Cálculo:**

$ Q_{conv} = (120 \, W/m^2 \cdot K)(0.8 \, m^2)(90 - 25) \, ^\circ C $

$ Q_{conv} = (96 \, W/K)(65 \, ^\circ C) $

$ Q_{conv} = 6240 \, W = 6.24 \, kW $

La tasa de transferencia de calor por convección del radiador al aire es de $6.24 \, kW$.

---

### Ejercicio 3: Radiación de un Tubo de Escape

Un tubo de escape de acero tiene una superficie exterior con una emisividad de $0.75$ y un área de $0.2 \, m^2$. La temperatura de la superficie del tubo es de $400^\circ C$. Los alrededores (ambiente del motor) están a $80^\circ C$.

Calcule la tasa neta de transferencia de calor por radiación desde el tubo de escape a los alrededores.

#### Solución Detallada

Para calcular la tasa neta de transferencia de calor por radiación, utilizamos la Ley de Stefan-Boltzmann. Es crucial convertir las temperaturas a Kelvin.

$ Q_{rad} = \epsilon \sigma A (T_s^4 - T_{alrededores}^4) $

**Datos:**
-   Emisividad ($\epsilon$) = $0.75$
-   Constante de Stefan-Boltzmann ($\sigma$) = $5.67 \times 10^{-8} \, W/m^2 \cdot K^4$
-   Área ($A$) = $0.2 \, m^2$
-   Temperatura de la superficie ($T_s$) = $400^\circ C = 400 + 273.15 = 673.15 \, K$
-   Temperatura de los alrededores ($T_{alrededores}$) = $80^\circ C = 80 + 273.15 = 353.15 \, K$

**Cálculo:**

$ Q_{rad} = (0.75)(5.67 \times 10^{-8} \, W/m^2 \cdot K^4)(0.2 \, m^2) ((673.15 \, K)^4 - (353.15 \, K)^4) $

$ Q_{rad} = (0.75)(5.67 \times 10^{-8})(0.2) (2.05 \times 10^{11} - 1.56 \times 10^{10}) $

$ Q_{rad} = (8.505 \times 10^{-9}) (1.894 \times 10^{11}) $

$ Q_{rad} = 1610.8 \, W \approx 1.61 \, kW $

La tasa neta de transferencia de calor por radiación desde el tubo de escape es de aproximadamente $1.61 \, kW$.

```