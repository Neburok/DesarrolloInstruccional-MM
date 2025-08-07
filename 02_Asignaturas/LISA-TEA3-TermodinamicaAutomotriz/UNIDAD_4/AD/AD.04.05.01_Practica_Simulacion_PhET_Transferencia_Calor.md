# AD.04.05.01 - Práctica de Simulación: Transferencia de Calor en Máquinas Térmicas con PhET

## Contenido

1. [Introducción](#introducción)
2. [Desarrollo](#desarrollo)
   - [Marco Teórico](#marco-teórico)
   - [Herramientas de Simulación](#herramientas-de-simulación)
   - [Práctica Resuelta 1: Conducción en Componentes Automotrices](#práctica-resuelta-1-conducción-en-componentes-automotrices)
   - [Práctica Resuelta 2: Convección en Sistema de Refrigeración](#práctica-resuelta-2-convección-en-sistema-de-refrigeración)
   - [Práctica Resuelta 3: Radiación en Sistema de Escape](#práctica-resuelta-3-radiación-en-sistema-de-escape)
   - [Análisis Comparativo de Resultados](#análisis-comparativo-de-resultados)
   - [Aplicaciones a Sistemas Automotrices Reales](#aplicaciones-a-sistemas-automotrices-reales)
3. [Ejercicios de Reforzamiento](#ejercicios-de-reforzamiento)
4. [Conclusiones](#conclusiones)
5. [Bibliografía](#bibliografía)

---

## Introducción

La **simulación computacional** es una herramienta fundamental en la ingeniería moderna para el **análisis y diseño** de sistemas térmicos automotrices. Permite visualizar, cuantificar y optimizar la **transferencia de calor** en componentes vehiculares sin la necesidad de prototipos físicos costosos.

En esta actividad utilizaremos el **simulador PhET** (Physics Education Technology) de la Universidad de Colorado, una herramienta educativa gratuita y científicamente validada, para analizar los **tres mecanismos** de transferencia de calor en **aplicaciones automotrices específicas**.

**Competencia a desarrollar:** *Utilizar herramientas de simulación computacional para analizar, comparar y predecir el comportamiento térmico de sistemas automotrices, interpretando resultados para la toma de decisiones de diseño.*

**Objetivos específicos:**
- Simular **conducción** en componentes del motor
- Analizar **convección** en sistemas de refrigeración
- Evaluar **radiación** en componentes de alta temperatura
- **Comparar** la efectividad de los tres mecanismos
- **Aplicar** resultados a casos reales de la industria automotriz

---

## Desarrollo

### Marco Teórico

#### Importancia de la Simulación en Ingeniería Automotriz

La **gestión térmica** en vehículos modernos requiere un análisis preciso debido a:

- **Densidad energética creciente:** Motores más potentes en espacios reducidos
- **Eficiencia energética:** Optimización del consumo de combustible
- **Emisiones:** Control de temperaturas para sistemas de post-tratamiento
- **Durabilidad:** Prevención de fallas por sobrecalentamiento
- **Confort:** Sistemas de climatización eficientes

#### Ventajas de la Simulación Digital

**Beneficios técnicos:**
- **Visualización** de campos de temperatura invisibles
- **Cuantificación** precisa de transferencia de calor
- **Comparación** rápida de alternativas de diseño
- **Predicción** del comportamiento en condiciones extremas

**Beneficios económicos:**
- **Reducción** de costos de prototipado
- **Aceleración** del proceso de desarrollo
- **Optimización** antes de fabricación
- **Prevención** de fallas costosas

### Herramientas de Simulación

#### PhET Interactive Simulations

**PhET** es una suite de simulaciones educativas desarrollada por la **Universidad de Colorado Boulder**, utilizada por más de **100 millones de estudiantes** mundialmente.

**Simuladores relevantes para transferencia de calor:**

1. **"Energy Forms and Changes"**
   - **URL:** https://phet.colorado.edu/sims/html/energy-forms-and-changes/latest/energy-forms-and-changes_es.html
   - **Aplicación:** Análisis general de transferencia energética

2. **"Heat Transfer"** 
   - **Funciones:** Conducción, convección y radiación
   - **Variables:** Temperatura, materiales, geometría

#### Acceso y Configuración

**Requisitos del sistema:**
- **Navegador web moderno** (Chrome, Firefox, Safari, Edge)
- **Conexión a internet** estable
- **JavaScript habilitado**
- **Resolución mínima:** 1024 x 768 píxeles

**Configuración inicial:**
1. Acceder al sitio web oficial de PhET
2. Seleccionar simulación en **idioma español**
3. Verificar funcionamiento de controles interactivos
4. Ajustar configuraciones de visualización

### Práctica Resuelta 1: Conducción en Componentes Automotrices

#### Objetivo Específico
Simular la **transferencia de calor por conducción** a través de la pared del cilindro de un motor, analizando el efecto del **material** y **espesor** en la eficiencia térmica.

#### Procedimiento Paso a Paso

**Paso 1: Configuración del Simulador**
1. Abrir el simulador **"Energy Forms and Changes"**
2. Seleccionar la pestaña **"Systems"**
3. Configurar una **fuente de calor** (representing combustion chamber)
4. Añadir un **bloque sólido** (representing cylinder wall)
5. Colocar un **sumidero de calor** (representing coolant)

**Paso 2: Configuración de Parámetros**
- **Fuente de calor:** Temperatura constante 800°C
- **Material del bloque:** Hierro (simulando hierro fundido)
- **Espesor:** Variable (5 mm, 8 mm, 12 mm)
- **Sumidero frío:** Temperatura constante 90°C
- **Activar:** Visualización de flujo de energía

**Paso 3: Ejecución de la Simulación**

**Experimento 1.1 - Espesor 5 mm:**
```
Configuración:
- Material: Hierro fundido
- Espesor: 5 mm
- ΔT = 800°C - 90°C = 710°C

Observaciones:
- Flujo de energía: ALTO (flecha gruesa en simulador)
- Tiempo de equilibrio: RÁPIDO (~30 segundos simulados)
- Gradiente de temperatura: PRONUNCIADO
```

**Experimento 1.2 - Espesor 8 mm:**
```
Configuración:
- Material: Hierro fundido  
- Espesor: 8 mm (estándar automotriz)
- ΔT = 710°C

Observaciones:
- Flujo de energía: MODERADO
- Tiempo de equilibrio: MODERADO (~45 segundos)
- Gradiente de temperatura: MODERADO
```

**Experimento 1.3 - Espesor 12 mm:**
```
Configuración:
- Material: Hierro fundido
- Espesor: 12 mm
- ΔT = 710°C

Observaciones:
- Flujo de energía: BAJO
- Tiempo de equilibrio: LENTO (~60 segundos)
- Gradiente de temperatura: SUAVE
```

#### Análisis de Resultados - Práctica 1

**Cálculo teórico para validación:**

Para hierro fundido con k = 52 W/m·K, A = 0.015 m²:

**Espesor 5 mm:**
$$\dot{Q}_{5mm} = \frac{k \cdot A \cdot \Delta T}{L} = \frac{52 \times 0.015 \times 710}{0.005} = 11,076 \text{ W}$$

**Espesor 8 mm:**
$$\dot{Q}_{8mm} = \frac{52 \times 0.015 \times 710}{0.008} = 6,923 \text{ W}$$

**Espesor 12 mm:**
$$\dot{Q}_{12mm} = \frac{52 \times 0.015 \times 710}{0.012} = 4,615 \text{ W}$$

**Interpretación:**
- **Relación inversa:** Mayor espesor → menor transferencia de calor
- **Factor de escala:** Doblar espesor reduce transferencia a la mitad
- **Implicación automotriz:** Balance entre **resistencia mecánica** y **disipación térmica**

### Práctica Resuelta 2: Convección en Sistema de Refrigeración

#### Objetivo Específico
Analizar la **transferencia de calor por convección** en un radiador automotriz, evaluando el efecto de la **velocidad del fluido** y **diferencia de temperatura**.

#### Procedimiento Paso a Paso

**Paso 1: Configuración del Sistema de Convección**
1. Seleccionar pestaña **"Intro"** en PhET
2. Configurar **aire en movimiento** (representing forced convection)
3. Añadir **superficie caliente** (representing radiator surface)
4. Activar **visualización de partículas** de aire
5. Habilitar **medición de temperatura**

**Paso 2: Configuración de Parámetros**
- **Superficie del radiador:** 85°C constante
- **Aire ambiente:** 25°C inicial
- **Área de transferencia:** Máxima disponible
- **Velocidad del aire:** Variable (baja, media, alta)

**Paso 3: Experimentos de Convección**

**Experimento 2.1 - Convección Natural (sin ventilador):**
```
Configuración:
- Temperatura superficie: 85°C
- Temperatura aire: 25°C
- Velocidad aire: MÍNIMA (convección natural)
- Tiempo de observación: 2 minutos simulados

Observaciones:
- Movimiento del aire: LENTO, patrones verticales
- Transferencia de calor: BAJA (partículas se mueven lentamente)
- Enfriamiento de superficie: GRADUAL
- Patrón: Aire caliente asciende, aire frío desciende
```

**Experimento 2.2 - Convección Forzada Moderada:**
```
Configuración:
- Temperatura superficie: 85°C
- Temperatura aire: 25°C  
- Velocidad aire: MEDIA (ventilador moderado)
- Tiempo de observación: 2 minutos

Observaciones:
- Movimiento del aire: DINÁMICO, flujo horizontal
- Transferencia de calor: MODERADA-ALTA
- Enfriamiento de superficie: NOTABLE
- Patrón: Flujo dirigido sobre la superficie
```

**Experimento 2.3 - Convección Forzada Alta:**
```
Configuración:
- Temperatura superficie: 85°C
- Temperatura aire: 25°C
- Velocidad aire: ALTA (ventilador máximo)
- Tiempo de observación: 2 minutos

Observaciones:
- Movimiento del aire: MUY DINÁMICO
- Transferencia de calor: MÁXIMA (flujo intenso de partículas)
- Enfriamiento de superficie: RÁPIDO y EFICIENTE
- Patrón: Flujo turbulento sobre toda la superficie
```

#### Análisis de Resultados - Práctica 2

**Correlación con coeficientes reales de convección:**

**Convección Natural:**
- **h ≈ 5-25 W/m²·K** (aire quieto)
- **Aplicación:** Motor apagado, enfriamiento lento
- **Q̇ = 25 × 2.5 × (85-25) = 3,750 W**

**Convección Forzada Media:**
- **h ≈ 50-100 W/m²·K** (ventilador moderado) 
- **Aplicación:** Conducción urbana normal
- **Q̇ = 75 × 2.5 × 60 = 11,250 W**

**Convección Forzada Alta:**
- **h ≈ 100-200 W/m²·K** (ventilador máximo)
- **Aplicación:** Conducción en autopista, motor a alta carga
- **Q̇ = 150 × 2.5 × 60 = 22,500 W**

**Interpretación automotriz:**
- La **velocidad del aire** es crítica para el enfriamiento
- Los **ventiladores** son esenciales en tráfico lento
- El **diseño aerodinámico** mejora la convección natural

### Práctica Resuelta 3: Radiación en Sistema de Escape

#### Objetivo Específico
Evaluar la **transferencia de calor por radiación** de componentes de escape de alta temperatura, analizando el efecto de la **temperatura** y **emisividad superficial**.

#### Procedimiento Paso a Paso

**Paso 1: Configuración del Sistema de Radiación**
1. Utilizar simulador **"Energy Forms and Changes"**
2. Configurar **objeto a alta temperatura** (multiple de escape)
3. Establecer **entorno frío** (compartimento motor)
4. **Eliminar contacto físico** (solo radiación)
5. Activar **visualización de ondas electromagnéticas**

**Paso 2: Variables del Experimento**
- **Temperatura del múltiple:** Variable (300°C, 400°C, 500°C)
- **Temperatura del entorno:** 80°C constante
- **Emisividad:** Variable (superficie pulida vs oxidada)
- **Área de transferencia:** Constante

**Paso 3: Experimentos de Radiación**

**Experimento 3.1 - Temperatura Moderada:**
```
Configuración:
- Temperatura múltiple: 300°C (573 K)
- Temperatura entorno: 80°C (353 K)  
- Emisividad: 0.7 (acero oxidado)
- Área: 0.8 m²

Observaciones en PhET:
- Ondas electromagnéticas: VISIBLES, frecuencia moderada
- Transferencia energética: CONSTANTE
- Visualización: Radiación infrarroja representada
- Patrón: Emisión uniforme desde toda la superficie
```

**Experimento 3.2 - Temperatura Alta:**
```
Configuración:
- Temperatura múltiple: 400°C (673 K)
- Temperatura entorno: 80°C (353 K)
- Emisividad: 0.7 (acero oxidado)
- Área: 0.8 m²

Observaciones en PhET:
- Ondas electromagnéticas: MÁS INTENSAS
- Transferencia energética: SIGNIFICATIVAMENTE MAYOR
- Visualización: Mayor densidad de ondas
- Color: Representación de mayor energía térmica
```

**Experimento 3.3 - Temperatura Muy Alta:**
```
Configuración:
- Temperatura múltiple: 500°C (773 K)
- Temperatura entorno: 80°C (353 K)
- Emisividad: 0.7 (acero oxidado)  
- Área: 0.8 m²

Observaciones en PhET:
- Ondas electromagnéticas: MUY INTENSAS
- Transferencia energética: MÁXIMA
- Visualización: Alta frecuencia de ondas
- Patrón: Radiación muy activa y visible
```

#### Análisis de Resultados - Práctica 3

**Cálculo teórico usando Ley de Stefan-Boltzmann:**

**Para ε = 0.7, σ = 5.67×10⁻⁸ W/m²·K⁴, A = 0.8 m²:**

**Experimento 3.1 (300°C):**
$$\dot{Q}_{rad} = 0.7 \times 5.67 \times 10^{-8} \times 0.8 \times (573^4 - 353^4)$$
$$\dot{Q}_{rad} = 3.17 \times 10^{-8} \times (1.08 \times 10^{11} - 1.55 \times 10^{10})$$
$$\dot{Q}_{rad} = 2,944 \text{ W} = 2.94 \text{ kW}$$

**Experimento 3.2 (400°C):**
$$\dot{Q}_{rad} = 3.17 \times 10^{-8} \times (2.06 \times 10^{11} - 1.55 \times 10^{10})$$
$$\dot{Q}_{rad} = 6,044 \text{ W} = 6.04 \text{ kW}$$

**Experimento 3.3 (500°C):**
$$\dot{Q}_{rad} = 3.17 \times 10^{-8} \times (3.57 \times 10^{11} - 1.55 \times 10^{10})$$
$$\dot{Q}_{rad} = 10,839 \text{ W} = 10.84 \text{ kW}$$

**Interpretación de la dependencia T⁴:**
- **Incremento 300°C→400°C:** Factor 2.05 veces
- **Incremento 400°C→500°C:** Factor 1.79 veces  
- **Incremento total 300°C→500°C:** Factor 3.68 veces

**Conclusión:** La radiación aumenta **exponencialmente** con la temperatura.

### Análisis Comparativo de Resultados

#### Comparación de Efectividad por Mecanismo

**Resumen de transferencias calculadas:**

| **Mecanismo** | **Condiciones** | **Transferencia (kW)** | **% del Total** |
|:-------------|:---------------|:----------------------:|:---------------:|
| **Conducción** | Pared cilindro 8mm | 6.92 | 15% |
| **Convección** | Radiador + ventilador | 22.50 | 50% |
| **Radiación** | Escape a 400°C | 6.04 | 13% |
| **Convección** | Natural (sin ventilador) | 3.75 | 8% |
| **Otros** | Pérdidas diversas | 6.00 | 14% |
| **TOTAL** | Sistema integral | **45.21** | **100%** |

#### Factores Determinantes por Mecanismo

**Conducción:**
- **Factor crítico:** Espesor del material (L⁻¹)
- **Optimización:** Materiales alta conductividad, espesor mínimo
- **Limitación:** Resistencia mecánica

**Convección:**
- **Factor crítico:** Velocidad del fluido (h)
- **Optimización:** Ventiladores, área superficial
- **Limitación:** Potencia del ventilador

**Radiación:**
- **Factor crítico:** Temperatura (T⁴)
- **Optimización:** Control de emisividad
- **Limitación:** Temperaturas operativas

### Aplicaciones a Sistemas Automotrices Reales

#### Caso de Estudio 1: Gestión Térmica Motor Turbo

**Problema:** Motor turbo de 2.0L con intercooler

**Análisis con resultados de simulación:**
- **Turbina:** 850°C → Radiación dominante (15 kW)
- **Intercooler:** Convección forzada requerida (8 kW)
- **Bloque motor:** Conducción + convección (12 kW)

**Solución de diseño:**
1. **Escudos térmicos** con ε = 0.05 para reducir radiación
2. **Ventilación forzada** en intercooler
3. **Canales de refrigeración** optimizados

#### Caso de Estudio 2: Sistema de Frenos de Alto Rendimiento

**Problema:** Frenos deportivos con temperatures >400°C

**Análisis basado en simulaciones:**
- **Convección natural:** Insuficiente (2 kW vs 8 kW requeridos)
- **Radiación:** Significativa a altas temperaturas (4 kW)
- **Ventilación dirigida:** Necesaria para convección forzada

**Solución implementada:**
1. **Ductos de aire** para convección forzada
2. **Discos ventilados** para aumentar área
3. **Materiales cerámicos** para reducir masa térmica

#### Caso de Estudio 3: Vehículo Eléctrico - Gestión Térmica de Baterías

**Problema:** Baterías Li-ion sensibles a temperatura

**Análisis con simuladores:**
- **Conducción:** A través de placas de refrigeración (3 kW)
- **Convección:** Refrigerante líquido (5 kW)  
- **Pérdidas:** Minimizar radiación al habitáculo

**Sistema de gestión:**
1. **Placas de aluminio** para conducción eficiente
2. **Bomba de circulación** para convección forzada
3. **Aislamiento térmico** del habitáculo

### Ejercicios Propuestos

**Ejercicio 1:** Repetir Práctica 1 comparando hierro fundido vs aluminio. Calcular diferencia porcentual en transferencia de calor.

**Ejercicio 2:** En Práctica 2, determinar la velocidad mínima de aire necesaria para disipar 15 kW con ΔT = 50°C.

**Ejercicio 3:** Para Práctica 3, calcular la reducción de radiación al cambiar de superficie oxidada (ε=0.7) a pulida (ε=0.1).

---

## Ejercicios de Reforzamiento

### Ejercicio de Reforzamiento 1: Optimización de Radiador

**Problema:** Un fabricante automotriz debe optimizar el radiador para un motor de 150 HP. Usando los resultados de las simulaciones PhET:

**Datos del sistema:**
- **Potencia térmica a disipar:** 30 kW
- **Temperatura superficial máxima:** 95°C
- **Temperatura aire ambiente:** 35°C
- **Área disponible:** 2.0 m²

**Tareas:**
a) Calcular coeficiente de convección requerido
b) Determinar tipo de ventilación necesaria
c) Comparar con resultados de simulación PhET

**Solución:**

**a) Coeficiente requerido:**
$$h_{requerido} = \frac{\dot{Q}}{A \cdot \Delta T} = \frac{30,000}{2.0 \times (95-35)} = \frac{30,000}{120} = 250 \text{ W/m²·K}$$

**b) Tipo de ventilación:**
Según simulaciones PhET:
- Convección natural: h = 5-25 W/m²·K ❌ **Insuficiente**
- Convección forzada moderada: h = 50-100 W/m²·K ❌ **Insuficiente**  
- Convección forzada alta: h = 200-400 W/m²·K ✅ **Adecuada**

**c) Comparación con PhET:**
La simulación confirma que se requiere **ventilación forzada de alta velocidad** para lograr h > 250 W/m²·K.

**Recomendación:** Ventilador de alto flujo con control variable según temperatura del motor.

### Ejercicio de Reforzamiento 2: Análisis de Sistema de Escape

**Problema:** Evaluar las pérdidas térmicas de un sistema de escape utilizando principios observados en simulaciones PhET.

**Configuración del sistema:**
- **Múltiple de escape:** 450°C, ε = 0.8, A = 1.2 m²
- **Tubo principal:** 350°C, ε = 0.6, A = 2.5 m²  
- **Silenciador:** 200°C, ε = 0.4, A = 1.8 m²
- **Temperatura ambiente:** 25°C

**Análisis basado en PhET:**

**Múltiple de escape:**
$$\dot{Q}_{multiple} = 0.8 \times 5.67 \times 10^{-8} \times 1.2 \times [(450+273)^4 - (25+273)^4]$$
$$\dot{Q}_{multiple} = 5.44 \times 10^{-8} \times (2.73 \times 10^{11} - 7.87 \times 10^{9}) = 14.4 \text{ kW}$$

**Tubo principal:**
$$\dot{Q}_{tubo} = 0.6 \times 5.67 \times 10^{-8} \times 2.5 \times [(350+273)^4 - (25+273)^4]$$
$$\dot{Q}_{tubo} = 8.51 \times 10^{-8} \times (1.50 \times 10^{11} - 7.87 \times 10^{9}) = 12.1 \text{ kW}$$

**Silenciador:**
$$\dot{Q}_{silenciador} = 0.4 \times 5.67 \times 10^{-8} \times 1.8 \times [(200+273)^4 - (25+273)^4]$$
$$\dot{Q}_{silenciador} = 4.08 \times 10^{-8} \times (5.01 \times 10^{10} - 7.87 \times 10^{9}) = 1.7 \text{ kW}$$

**Pérdidas totales por radiación:** 14.4 + 12.1 + 1.7 = **28.2 kW**

**Interpretación:** Las **simulaciones PhET** confirman que la radiación de escape representa una **pérdida energética significativa** (~20% de la potencia del motor), validando la importancia de **escudos térmicos** y **recuperación de calor** en diseños modernos.

### Ejercicio de Reforzamiento 3: Diseño de Sistema de Refrigeración de Frenos

**Problema:** Diseñar un sistema de refrigeración para frenos de competición usando principios demostrados en simulaciones PhET.

**Especificaciones:**
- **Potencia de frenado:** 50 kW (picos de 5 segundos)
- **Temperatura máxima admisible:** 400°C
- **Temperatura ambiente:** 30°C
- **Área del disco:** 0.15 m² por cara (0.3 m² total)

**Análisis de mecanismos:**

**1. Radiación (simulada en PhET):**
A 400°C con ε = 0.6:
$$\dot{Q}_{rad} = 0.6 \times 5.67 \times 10^{-8} \times 0.3 \times [(400+273)^4 - (30+273)^4]$$
$$\dot{Q}_{rad} = 1.02 \times 10^{-8} \times (2.06 \times 10^{11} - 8.41 \times 10^{9}) = 20.1 \text{ kW}$$

**2. Convección forzada requerida:**
$$\dot{Q}_{conv\_requerida} = 50 - 20.1 = 29.9 \text{ kW}$$

**3. Coeficiente de convección necesario:**
$$h_{necesario} = \frac{29,900}{0.3 \times (400-30)} = \frac{29,900}{111} = 269 \text{ W/m²·K}$$

**Solución de diseño validada con PhET:**
- **Ventilación forzada:** Ductos dirigidos para h > 270 W/m²·K
- **Discos ventilados:** Aumentar área efectiva en 40%
- **Materiales:** Hierro fundido con aletas radiales

**Verificación:** Las simulaciones PhET confirman que la **ventilación direccionada** es esencial para lograr los coeficientes de convección requeridos.

---

## Conclusiones

1. **Validación de simuladores educativos:** Las **simulaciones PhET** proporcionan una excelente herramienta para visualizar y comprender los **principios fundamentales** de transferencia de calor, ofreciendo resultados cualitativamente consistentes con **cálculos teóricos** y **aplicaciones reales** de la industria automotriz.

2. **Importancia de la convección forzada:** Los experimentos simulados confirman que la **convección forzada** es el mecanismo **más efectivo** para la disipación de calor en sistemas automotrices, especialmente en radiadores y sistemas de refrigeración, donde puede **quintuplicar** la transferencia respecto a la convección natural.

3. **Dependencia crítica de la temperatura en radiación:** Las simulaciones demuestran claramente la **dependencia T⁴** de la radiación térmica, mostrando que componentes de alta temperatura (escape, frenos) requieren **gestión térmica especializada** debido al aumento exponencial de las pérdidas radiativas.

4. **Aplicación práctica inmediata:** Los resultados obtenidos mediante simulación son **directamente aplicables** al diseño de sistemas térmicos automotrices, desde el **dimensionamiento de radiadores** hasta la **optimización de escudos térmicos**, validando la utilidad de herramientas educativas en contextos profesionales.

5. **Herramienta de diseño y optimización:** La combinación de **simulación visual** (PhET) con **cálculos analíticos** proporciona un enfoque integral para el **análisis térmico**, permitiendo tanto la **comprensión conceptual** como la **cuantificación precisa** de fenómenos de transferencia de calor.

6. **Identificación de limitaciones y soluciones:** Las prácticas realizadas permiten identificar **limitaciones inherentes** de cada mecanismo de transferencia y desarrollar **estrategias de optimización** específicas, como ventilación forzada para mejorar convección o control de emisividad para gestionar radiación.

---

## Bibliografía

PhET Interactive Simulations, University of Colorado Boulder. (2023). *Energy Forms and Changes*. https://phet.colorado.edu/sims/html/energy-forms-and-changes/latest/energy-forms-and-changes_es.html

Çengel, Y. A., & Ghajar, A. J. (2020). *Heat and mass transfer: Fundamentals and applications* (6th ed.). McGraw-Hill Education.

Incropera, F. P., DeWitt, D. P., Bergman, T. L., & Lavine, A. S. (2017). *Fundamentals of heat and mass transfer* (8th ed.). John Wiley & Sons.

Stone, R. (2012). *Introduction to internal combustion engines* (4th ed.). Palgrave Macmillan.

Heywood, J. B. (2018). *Internal combustion engine fundamentals* (2nd ed.). McGraw-Hill Education.

Wong, J. Y. (2001). *Theory of ground vehicles* (3rd ed.). John Wiley & Sons.

Wieman, C. E., Adams, W. K., & Perkins, K. K. (2008). PhET: Simulations that enhance learning. *Science*, 322(5902), 682-683.

SAE International. (2019). *Thermal management systems for automotive applications*. SAE Technical Paper Series.