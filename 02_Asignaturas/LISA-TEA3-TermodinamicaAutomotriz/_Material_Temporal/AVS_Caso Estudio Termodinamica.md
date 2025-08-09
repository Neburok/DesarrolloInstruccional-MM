
# AVS.01.04.01 Caso de Estudio: "Comparación de motores para vehículo de transporte urbano"

![Logo institucional]

## El presente caso de estudio será evaluado con base en una escala estimativa que considera aspectos técnicos, metodológicos y de presentación. La calificación obtenida será equivalente al 60% del total de la unidad 4.

---

# INTRODUCCIÓN

En el contexto del **transporte urbano moderno**, la **selección del motor adecuado** para una aplicación específica requiere un **análisis termodinámico integral** que considere parámetros como **eficiencia, potencia, consumo de combustible** y **desempeño en diferentes condiciones operativas**. La comprensión de los **ciclos termodinámicos, balances de energía** y el **funcionamiento de componentes** es fundamental para tomar decisiones técnicas informadas.

El presente caso de estudio permite al estudiante **aplicar conceptos de termodinámica** en un escenario real de selección de motores, donde deberá **analizar ciclos P-V, calcular parámetros de desempeño** y **evaluar el funcionamiento** de diferentes configuraciones de motores de combustión interna para una aplicación de transporte urbano.

# OBJETIVO GENERAL

**Analizar y comparar** las características termodinámicas de diferentes motores de combustión interna para **recomendar la mejor opción** para un vehículo de transporte urbano, considerando **ciclos termodinámicos, balances de energía, parámetros de desempeño** y **funcionamiento de componentes**.

# ACTIVIDAD PREVIA AL DESARROLLO DEL CASO

Antes de desarrollar el caso de estudio, revisa el **material teórico** proporcionado y contesta el siguiente **cuestionario**. Esto te ayudará a contextualizar los conceptos y a aprovechar mejor el análisis del caso.

![Icono de cuestionario]

Contesta brevemente:

1. **¿Cuáles son las 4 etapas del ciclo Otto y qué ocurre en cada una?**
    
    R=
    
2. **¿Qué representa el área encerrada en un diagrama P-V de un motor?**
    
3. **¿Cuál es la función principal del pistón, cilindro y cigüeñal en un motor?**
    
4. **¿Qué significa cilindrada y cómo se calcula?**
    
5. **¿Qué es el rendimiento térmico de un motor y por qué es importante?**
    

# DESCRIPCIÓN DEL CASO DE ESTUDIO

## **ESCENARIO:**

**"TransUrbe México"** es una empresa de transporte público que opera en Guadalajara, Jalisco. La compañía planea renovar su flota de **microbuses urbanos** y necesita seleccionar el motor más adecuado para sus nuevas unidades. El vehículo será utilizado para **rutas urbanas cortas** con frecuentes paradas y arranques.

## **SITUACIÓN:**

El departamento técnico ha **pre-seleccionado tres motores** de diferentes fabricantes que cumplen con los requerimientos básicos de potencia y emisiones. Todos son motores de **4 tiempos y ciclo Otto**, pero tienen **diferentes configuraciones** y características de desempeño. La empresa necesita una **recomendación técnica fundamentada** basada en análisis termodinámico.

## **REQUERIMIENTOS OPERATIVOS:**

- **Aplicación:** Microbús urbano de 20 pasajeros
- **Peso del vehículo cargado:** 4,500 kg
- **Velocidad promedio:** 25 km/h con paradas frecuentes
- **Operación diaria:** 12 horas continuas
- **Perfil de ruta:** 60% ciudad, 40% periférico
- **Combustible:** Gasolina Magna (87 octanos)

## **INFORMACIÓN DE LOS MOTORES:**

### **MOTOR A: "EcoUrban 1.8L"**

**Fabricante:** Nacional Motors  
**Tipo:** 4 cilindros en línea, 4 tiempos, SOHC

**Especificaciones técnicas:**

- **Cilindrada:** 1,800 cm³
- **Diámetro del pistón (Bore):** 82 mm
- **Carrera del pistón (Stroke):** 85 mm
- **Relación de compresión:** 9.5:1
- **Potencia máxima:** 120 HP @ 5,500 rpm
- **Torque máximo:** 165 N⋅m @ 3,800 rpm

**Datos termodinámicos (condiciones normales):**

- **Presión de admisión:** 1.0 bar
- **Presión máxima del ciclo:** 35 bar
- **Temperatura de admisión:** 25°C
- **Temperatura máxima del ciclo:** 1,800°C
- **Rendimiento térmico indicado:** 38%
- **Consumo específico:** 280 g/kWh

### **MOTOR B: "CityPower 2.0L"**

**Fabricante:** Global Engines  
**Tipo:** 4 cilindros en línea, 4 tiempos, DOHC

**Especificaciones técnicas:**

- **Cilindrada:** 2,000 cm³
- **Diámetro del pistón (Bore):** 86 mm
- **Carrera del pistón (Stroke):** 86 mm
- **Relación de compresión:** 10.2:1
- **Potencia máxima:** 140 HP @ 6,000 rpm
- **Torque máximo:** 180 N⋅m @ 4,200 rpm

**Datos termodinámicos (condiciones normales):**

- **Presión de admisión:** 1.0 bar
- **Presión máxima del ciclo:** 42 bar
- **Temperatura de admisión:** 25°C
- **Temperatura máxima del ciclo:** 1,950°C
- **Rendimiento térmico indicado:** 42%
- **Consumo específico:** 260 g/kWh

### **MOTOR C: "MaxTorque 2.2L"**

**Fabricante:** Heavy Duty Motors  
**Tipo:** 4 cilindros en línea, 4 tiempos, SOHC + Turbo

**Especificaciones técnicas:**

- **Cilindrada:** 2,200 cm³
- **Diámetro del pistón (Bore):** 88 mm
- **Carrera del pistón (Stroke):** 90 mm
- **Relación de compresión:** 8.8:1
- **Potencia máxima:** 160 HP @ 5,200 rpm
- **Torque máximo:** 220 N⋅m @ 2,800 rpm

**Datos termodinámicos (condiciones normales):**

- **Presión de admisión:** 1.5 bar (sobrealimentado)
- **Presión máxima del ciclo:** 48 bar
- **Temperatura de admisión:** 45°C (post-turbo)
- **Temperatura máxima del ciclo:** 2,100°C
- **Rendimiento térmico indicado:** 40%
- **Consumo específico:** 270 g/kWh

# DESARROLLO DEL CASO DE ESTUDIO

## **FASE 1: ANÁLISIS DE CICLOS TERMODINÁMICOS (25 puntos)**

### **1.1 Diagramas P-V para cada motor**

Para cada uno de los tres motores:

a) **Dibuja el diagrama P-V** del ciclo Otto teórico mostrando:

- Las 4 etapas del ciclo claramente identificadas
- Puntos de presión y volumen característicos
- Área del ciclo sombreada

b) **Calcula los volúmenes característicos:**

- Volumen total del cilindro (Vt)
- Volumen de la cámara de combustión (Vc)
- Volumen desplazado (Vd)

c) **Describe qué ocurre** en cada etapa del ciclo:

- Admisión (1→2)
- Compresión (2→3)
- Combustión y expansión (3→4)
- Escape (4→1)

### **1.2 Comparación de ciclos**

Compara los tres motores:

a) **Identifica diferencias** en los diagramas P-V b) **Explica el impacto** de la relación de compresión en cada ciclo c) **Analiza el efecto** del turboalimentador en el Motor C

## **FASE 2: CÁLCULOS TERMODINÁMICOS (30 puntos)**

### **2.1 Cálculo de eficiencia térmica teórica del ciclo Otto**

Para cada motor, utiliza la fórmula del ciclo Otto ideal:

**Fórmula:** ηOtto = 1 - (1/r^(γ-1))

Donde:

- r = relación de compresión
- γ = 1.4 (relación de calores específicos para aire)

**Calcular para cada motor:**

a) **Motor A (rc = 9.5:1):**

- ηOtto = 1 - (1/9.5^0.4) = ?
- Comparar con eficiencia indicada proporcionada (38%)

b) **Motor B (rc = 10.2:1):**

- ηOtto = 1 - (1/10.2^0.4) = ?
- Comparar con eficiencia indicada proporcionada (42%)

c) **Motor C (rc = 8.8:1):**

- ηOtto = 1 - (1/8.8^0.4) = ?
- Comparar con eficiencia indicada proporcionada (40%)

### **2.2 Cálculos de relaciones isentrópicas**

Para el proceso de compresión (1-2), calcula usando las relaciones isentrópicas:

**Fórmulas:**

- T₂/T₁ = r^(γ-1)
- P₂/P₁ = r^γ

**Datos iniciales (estado 1):**

- T₁ = 298 K (25°C - temperatura de admisión)
- P₁ = 1.0 bar (presión de admisión)

**Calcular para cada motor:**

a) **Temperatura al final de compresión (T₂):**

- Motor A: T₂ = 298 × 9.5^0.4 = ? K
- Motor B: T₂ = 298 × 10.2^0.4 = ? K
- Motor C: T₂ = 298 × 8.8^0.4 = ? K

b) **Presión al final de compresión (P₂):**

- Motor A: P₂ = 1.0 × 9.5^1.4 = ? bar
- Motor B: P₂ = 1.0 × 10.2^1.4 = ? bar
- Motor C: P₂ = 1.0 × 8.8^1.4 = ? bar

### **2.3 Balance de energía y transferencias de calor**

Usando las fórmulas del ciclo Otto:

**Fórmulas:**

- Q_H = m·cv·(T₃ - T₂) (calor añadido)
- Q_L = m·cv·(T₄ - T₁) (calor rechazado)
- W_neto = Q_H - Q_L (trabajo neto)

**Para análisis simplificado (m = 1 kg, cv = 0.718 kJ/kg·K):**

a) **Estimar temperatura máxima (T₃)** usando datos proporcionados:

- Motor A: T₃ = 1800°C = 2073 K
- Motor B: T₃ = 1950°C = 2223 K
- Motor C: T₃ = 2100°C = 2373 K

b) **Calcular temperatura al final de expansión (T₄):**

- T₄/T₃ = (1/r)^(γ-1)
- Motor A: T₄ = 2073 × (1/9.5)^0.4 = ? K
- Motor B: T₄ = 2223 × (1/10.2)^0.4 = ? K
- Motor C: T₄ = 2373 × (1/8.8)^0.4 = ? K

c) **Calcular transferencias de calor:**

- Q_H para cada motor
- Q_L para cada motor
- Trabajo neto teórico

### **2.4 Análisis de consumo específico**

Utilizando los datos de consumo específico proporcionados:

**Calcular:**

a) **Consumo horario de combustible** (para potencia promedio de 80 HP):

- Motor A: Consumo = (80 HP × 0.746 kW/HP × 280 g/kWh) = ? kg/h
- Motor B: Consumo = (80 HP × 0.746 kW/HP × 260 g/kWh) = ? kg/h
- Motor C: Consumo = (80 HP × 0.746 kW/HP × 270 g/kWh) = ? kg/h

b) **Costo operativo diario** (12 horas operación, gasolina $24/L):

- Densidad gasolina = 0.75 kg/L
- Costo por motor = (Consumo kg/h ÷ 0.75) × 12 h × $24/L

c) **Eficiencia real vs. teórica:**

- Comparar eficiencia calculada con datos de consumo real
- Identificar pérdidas mecánicas y térmicas

## **FASE 3: PARÁMETROS DE DESEMPEÑO (20 puntos)**

### **3.1 Cálculo de parámetros principales**

Para cada motor, calcula y analiza:

a) **Cilindrada específica:**

- Cilindrada total
- Cilindrada por cilindro
- Relación cilindrada/potencia

b) **Parámetros de potencia:**

- Potencia específica (HP/L)
- Densidad de potencia (HP/kg estimado)
- Curva de potencia vs RPM (estimada)

c) **Parámetros de torque:**

- Torque específico (N⋅m/L)
- Curva de torque vs RPM (estimada)
- Torque a bajas revoluciones (importante para uso urbano)

### **3.2 Rendimiento y eficiencia**

Evalúa para cada motor:

a) **Rendimiento térmico:**

- Rendimiento indicado
- Rendimiento efectivo estimado
- Comparación entre motores

b) **Eficiencia energética:**

- Consumo específico de combustible
- Eficiencia volumétrica estimada
- Impacto de la sobrealimentación (Motor C)

### **3.3 Adecuación para uso urbano**

Analiza qué tan adecuado es cada motor para:

a) **Arranques frecuentes** b) **Operación a bajas revoluciones** c) **Respuesta del acelerador** d) **Consumo en tráfico urbano**

## **FASE 4: COMPONENTES Y FUNCIONAMIENTO (15 puntos)**

### **4.1 Análisis de componentes principales**

Para cada motor, describe la función y características de:

a) **Cilindro:**

- Diámetro y su impacto en el desempeño
- Material y diseño
- Relación con la transferencia de calor

b) **Pistón:**

- Carrera y su efecto en el torque
- Velocidad media del pistón
- Relación con las vibraciones

c) **Cigüeñal:**

- Configuración para 4 cilindros
- Orden de encendido
- Balance dinámico

### **4.2 Sistemas auxiliares**

Analiza las diferencias en:

a) **Sistema de distribución:**

- SOHC vs DOHC
- Impacto en el rendimiento volumétrico
- Mantenimiento requerido

b) **Sistema de sobrealimentación (Motor C):**

- Funcionamiento del turbocompresor
- Ventajas y desventajas
- Impacto en el ciclo termodinámico

## **FASE 5: RECOMENDACIÓN TÉCNICA (10 puntos)**

### **5.1 Matriz de evaluación**

Crea una matriz de evaluación considerando:

|**Criterio**|**Peso (%)**|**Motor A**|**Motor B**|**Motor C**|
|---|---|---|---|---|
|Eficiencia térmica|25%||||
|Torque a bajas RPM|20%||||
|Consumo de combustible|20%||||
|Potencia específica|15%||||
|Complejidad/Mantenimiento|10%||||
|Costo operativo|10%||||
|**TOTAL**|**100%**||||

**Escala:** 1 = Deficiente, 2 = Regular, 3 = Bueno, 4 = Muy bueno, 5 = Excelente

### **5.2 Recomendación final**

Basándote en tu análisis termodinámico:

a) **Motor recomendado** y justificación técnica b) **Ventajas termodinámicas** del motor seleccionado c) **Consideraciones especiales** para la aplicación urbana d) **Impacto económico** esperado de tu recomendación

# PRODUCTOS ENTREGABLES

## **ESTRUCTURA DEL REPORTE:**

### **Datos generales al inicio del documento:**

- Nombre completo del estudiante
- Matrícula
- Nombre de la asignatura: Termodinámica Automotriz
- Nombre del caso de estudio
- Nombre del docente
- Fecha de elaboración

### **Contenido del reporte:**

### **1. Resumen Ejecutivo** (5% - 0.5 pts)

Síntesis de 200 palabras con tu recomendación técnica

### **2. Desarrollo de la Fase 1: Ciclos Termodinámicos** (25% - 2.5 pts)

- Diagramas P-V de los tres motores
- Cálculos de volúmenes característicos
- Descripción detallada de las etapas del ciclo
- Comparación entre los ciclos

### **3. Desarrollo de la Fase 2: Balances de Energía** (30% - 3.0 pts)

- Cálculos de trabajo por ciclo
- Balances de energía completos
- Análisis de temperaturas y presiones
- Evaluación de eficiencias

### **4. Desarrollo de la Fase 3: Parámetros de Desempeño** (20% - 2.0 pts)

- Cálculo de parámetros principales (cilindrada, potencia, torque)
- Análisis de rendimiento y eficiencia
- Evaluación para uso urbano

### **5. Desarrollo de la Fase 4: Componentes** (15% - 1.5 pts)

- Descripción del funcionamiento de componentes principales
- Análisis de sistemas auxiliares
- Impacto en el desempeño termodinámico

### **6. Desarrollo de la Fase 5: Recomendación** (5% - 0.5 pts)

- Matriz de evaluación completa
- Recomendación técnica justificada

## **CRITERIOS DE EVALUACIÓN**

### **Aspectos Técnicos (70 puntos):**

- **Correcta elaboración** de diagramas P-V (20 pts)
- **Precisión en cálculos** de balances de energía (25 pts)
- **Análisis de parámetros** de desempeño (15 pts)
- **Calidad de la recomendación** técnica (10 pts)

### **Aspectos Metodológicos (20 puntos):**

- **Aplicación correcta** de conceptos termodinámicos (10 pts)
- **Uso de fórmulas** y procedimientos apropiados (5 pts)
- **Proceso lógico** de análisis y comparación (5 pts)

### **Aspectos de Presentación (10 puntos):**

- **Claridad** en diagramas y gráficas (5 pts)
- **Organización** del reporte (3 pts)
- **Uso correcto** de unidades y notación (2 pts)

### **Calificación total = 100 puntos (equivalente al 60% de la Unidad 4)**

# RECURSOS DE APOYO

## **Fórmulas del ciclo Otto (extraídas de la lectura):**

- **Eficiencia térmica:** ηOtto = 1 - (1/r^(γ-1))
- **Relaciones isentrópicas:**
    - T₂/T₁ = (V₁/V₂)^(γ-1) = r^(γ-1)
    - P₂/P₁ = (V₁/V₂)^γ = r^γ
- **Transferencias de calor:**
    - Q_H = m·cv·(T₃ - T₂)
    - Q_L = m·cv·(T₄ - T₁)
- **Trabajo neto:** W_neto = Q_H - Q_L

## **Constantes termodinámicas:**

- **γ (gamma) para aire:** 1.4
- **R (constante específica del aire):** 287 J/(kg⋅K)
- **cv (calor específico a volumen constante):** 0.718 kJ/(kg⋅K)
- **cp (calor específico a presión constante):** 1.005 kJ/(kg⋅K)
- **Densidad gasolina:** 0.75 kg/L
- **Poder calorífico gasolina:** 44 MJ/kg

## **Conversiones útiles:**

- 1 HP = 0.746 kW
- 1 bar = 100 kPa = 100,000 Pa
- °C a K: K = °C + 273.15
- Eficiencia en %: η × 100

## **Fórmulas de ejercicios de la lectura:**

- **Eficiencia Carnot:** ηCarnot = 1 - (TL/TH)
- **Trabajo neto:** W_neto = η × Q_H
- **Calor rechazado:** Q_L = Q_H - W_neto

## **Valores típicos para comparación:**

- **Relaciones de compresión Otto:** 8:1 a 12:1
- **Eficiencia térmica motores gasolina:** 25-30%
- **Consumo específico típico:** 250-300 g/kWh
- **Temperatura combustión:** 1800-2200°C

---

**Nota:** Este caso de estudio está diseñado para que los estudiantes apliquen conceptos fundamentales de termodinámica en un contexto real de selección de motores, integrando teoría con aplicación práctica en la industria automotriz.