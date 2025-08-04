# AR.04.01.01 Problemario: Ciclos Termodinámicos

## Instrucciones

Resuelva los siguientes problemas aplicando los conceptos y ecuaciones estudiadas en las lecturas de ciclos termodinámicos. Muestre todos los pasos de su solución, identifique claramente los datos, suposiciones y justifique el uso de las ecuaciones.

**Datos útiles:**
- γ (aire) = 1.4
- cp (aire) = 1.005 kJ/kg·K  
- cv (aire) = 0.718 kJ/kg·K
- R (aire) = 0.287 kJ/kg·K

---

## Problema 1: Ciclo de Otto - Análisis de Eficiencia

Un motor de automóvil opera según un **ciclo ideal de Otto** con una **relación de compresión de 9.5**. El aire entra al cilindro a **95 kPa** y **25°C**, y el motor funciona a **2800 rpm**. Durante el proceso de combustión se agregan **1800 kJ/kg** de calor. Usando **calores específicos constantes** a temperatura ambiente, determine:

a) La **eficiencia térmica** del ciclo
b) La **temperatura máxima** del ciclo (estado 3)
c) La **presión máxima** del ciclo (estado 3)
d) El **trabajo neto específico** producido por ciclo
e) La **potencia** desarrollada si el motor tiene una **cilindrada total de 2.2 L** y una **eficiencia volumétrica del 85%**

**Pistas:** 
- Use las relaciones isentrópicas para los procesos 1-2 y 3-4
- La temperatura máxima ocurre al final de la combustión (estado 3)
- Para calcular la potencia, considere el flujo másico de aire

---

## Problema 2: Ciclo Diesel - Comparación de Rendimiento

Un **motor diesel** opera según un **ciclo ideal Diesel** con una **relación de compresión de 18** y una **relación de corte de 2.2**. Las condiciones iniciales son **100 kPa** y **20°C**. Compare este motor con un **motor Otto** de **relación de compresión 10** que opera entre las mismas condiciones iniciales. Para ambos ciclos, determine:

a) La **eficiencia térmica**
b) El **trabajo neto específico** si ambos reciben la **misma cantidad de calor** (2000 kJ/kg)
c) Las **temperaturas en todos los estados** del ciclo
d) ¿Cuál motor es más eficiente y por qué?

**Pistas:**
- Para el ciclo Diesel: $\eta = 1 - \frac{1}{r^{\gamma-1}} \left[ \frac{r_c^{\gamma} - 1}{\gamma (r_c - 1)} \right]$
- Para el ciclo Otto: $\eta = 1 - \frac{1}{r^{\gamma-1}}$
- Use el balance de energía para encontrar las temperaturas

---

## Problema 3: Ciclo de Carnot - Límite Teórico

Una **planta de potencia** opera según un **ciclo de Carnot** entre un **depósito caliente a 650°C** y un **depósito frío a 25°C**. La planta debe generar **50 MW** de potencia. Determine:

a) La **eficiencia térmica** del ciclo de Carnot
b) La **tasa de suministro de calor** requerida
c) La **tasa de rechazo de calor** al ambiente
d) Si un **motor Otto real** con **eficiencia del 35%** operara entre las mismas temperaturas de reservorio, ¿cuál sería su **tasa de suministro de calor** para la misma potencia?
e) Compare y comente los resultados

**Pistas:**
- Use temperaturas absolutas para el ciclo de Carnot
- $\eta_{Carnot} = 1 - \frac{T_L}{T_H}$
- Para el motor real, use la definición básica de eficiencia térmica

---

## Problema 4: Análisis Paramétrico del Ciclo Otto

Un **motor de motocicleta** opera según un **ciclo Otto ideal**. Las condiciones de admisión son **90 kPa** y **35°C**. Se desea analizar el efecto de la **relación de compresión** en el rendimiento. Considere relaciones de compresión de **8, 9, 10, 11 y 12**. Para cada caso, determine:

a) La **eficiencia térmica**
b) La **temperatura después de la compresión** (estado 2)
c) La **presión después de la compresión** (estado 2)

Si se agregan **1600 kJ/kg** de calor durante la combustión:

d) La **temperatura máxima** del ciclo (estado 3)
e) El **trabajo neto específico**
f) Construya una **tabla comparativa** y **grafique** la eficiencia vs. relación de compresión
g) ¿Cuál es el **beneficio porcentual** de aumentar la relación de compresión de 8 a 12?

**Pistas:**
- Use una hoja de cálculo o calcule punto por punto
- La relación temperatura-presión para procesos isentrópicos: $\frac{T_2}{T_1} = \left(\frac{P_2}{P_1}\right)^{\frac{\gamma-1}{\gamma}}$

---

## Problema 5: Aplicación Automotriz Integrada

Un **ingeniero automotriz** está diseñando un nuevo **motor de 4 cilindros** que debe cumplir las siguientes especificaciones:

- **Potencia objetivo:** 120 kW a 5500 rpm
- **Eficiencia mínima:** 40%
- **Condiciones de admisión:** 85 kPa, 30°C
- **Combustible:** Gasolina (Qcomb = 44,000 kJ/kg)
- **Relación aire-combustible:** 15:1
- **Eficiencia volumétrica:** 82%

El motor operará según un **ciclo Otto modificado** donde la **eficiencia real** es el **75%** de la **eficiencia ideal**. Determine:

a) La **relación de compresión** necesaria para alcanzar la eficiencia objetivo
b) La **cilindrada total** requerida del motor
c) El **consumo de combustible** en kg/h a la potencia máxima
d) La **tasa de rechazo de calor** que debe manejar el sistema de enfriamiento
e) El **consumo específico de combustible** (g/kW·h)

**Pistas:**
- Primero determine la eficiencia ideal requerida
- Use la relación de eficiencia-compresión del Otto para encontrar r
- Considere el flujo másico de aire y la estequiometría de la combustión
- $\dot{m}_{aire} = \rho_{1} \times V_{cilindrada} \times n \times \eta_{vol} \times \frac{rpm}{120}$ (para 4 tiempos)

---

## Soluciones

### Solución Problema 1

**Dados:**
- r = 9.5
- P₁ = 95 kPa, T₁ = 25°C = 298.15 K
- rpm = 2800
- qᵢₙ = 1800 kJ/kg
- γ = 1.4

**a) Eficiencia térmica:**
$$\eta = 1 - \frac{1}{r^{\gamma-1}} = 1 - \frac{1}{9.5^{1.4-1}} = 1 - \frac{1}{9.5^{0.4}} = 1 - \frac{1}{2.29} = 0.563 = 56.3\%$$

**b) Proceso 1-2 (compresión isentrópica):**
$$T_2 = T_1 \times r^{\gamma-1} = 298.15 \times 9.5^{0.4} = 298.15 \times 2.29 = 683.0 \text{ K}$$

**Para el estado 3 (final de combustión):**
$$q_{in} = c_v(T_3 - T_2) \Rightarrow T_3 = T_2 + \frac{q_{in}}{c_v} = 683.0 + \frac{1800}{0.718} = 683.0 + 2507.5 = 3190.5 \text{ K}$$

**c) Presión máxima:**
$$P_2 = P_1 \times r^{\gamma} = 95 \times 9.5^{1.4} = 95 \times 21.8 = 2071 \text{ kPa}$$
$$P_3 = P_2 \times \frac{T_3}{T_2} = 2071 \times \frac{3190.5}{683.0} = 9679 \text{ kPa}$$

**d) Trabajo neto específico:**
$$w_{neto} = \eta \times q_{in} = 0.563 \times 1800 = 1013.4 \text{ kJ/kg}$$

**e) Para la potencia, necesitamos el flujo másico:**
$$\rho_1 = \frac{P_1}{RT_1} = \frac{95}{0.287 \times 298.15} = 1.111 \text{ kg/m}^3$$

$$\dot{m} = \rho_1 \times V_{cilindrada} \times \eta_{vol} \times \frac{rpm}{120} = 1.111 \times 0.0022 \times 0.85 \times \frac{2800}{120} = 0.0493 \text{ kg/s}$$

$$\dot{W} = \dot{m} \times w_{neto} = 0.0493 \times 1013.4 = 49.96 \text{ kW}$$

### Solución Problema 2

**Ciclo Diesel (r = 18, rᶜ = 2.2):**
$$\eta_{Diesel} = 1 - \frac{1}{18^{0.4}} \left[ \frac{2.2^{1.4} - 1}{1.4(2.2-1)} \right] = 1 - \frac{1}{3.482} \left[ \frac{2.639 - 1}{1.4 \times 1.2} \right] = 1 - 0.287 \times 0.977 = 0.720 = 72.0\%$$

**Ciclo Otto (r = 10):**
$$\eta_{Otto} = 1 - \frac{1}{10^{0.4}} = 1 - \frac{1}{2.512} = 0.602 = 60.2\%$$

**El motor Diesel es más eficiente debido a su mayor relación de compresión.**

---

*[Las soluciones de los problemas 3, 4 y 5 seguirían el mismo formato detallado]*

## Criterios de Evaluación

- **Identificación correcta de datos** (10%)
- **Selección apropiada de ecuaciones** (20%)
- **Desarrollo matemático correcto** (40%)
- **Interpretación física de resultados** (20%)
- **Presentación y claridad** (10%)

## Referencias

Çengel, Y. A., & Boles, M. A. (2019). *Termodinámica* (8ª ed.). McGraw-Hill Interamericana.

Moran, M. J., Shapiro, H. N., Boettner, D. D., & Bailey, M. B. (2018). *Fundamentals of engineering thermodynamics* (9th ed.). John Wiley & Sons.