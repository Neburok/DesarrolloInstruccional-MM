# EJEMPLO METODOLÓGICO: Desarrollo Paso a Paso del Caso de Estudio


## "[[AVS_01_04|Comparación de motores para vehículo de transporte urbano]]"

---

**IMPORTANTE:** Este documento muestra el desarrollo completo paso a paso como **ejemplo metodológico** para que los estudiantes comprendan cómo abordar casos de estudio similares. Los estudiantes deben usar esta guía como referencia de método, pero resolver su propio caso con datos diferentes.

---

# DATOS GENERALES

**Nombre del estudiante:** [Ejemplo Metodológico]  
**Matrícula:** [Guía de Referencia]  
**Asignatura:** Termodinámica Automotriz  
**Caso de estudio:** Comparación de motores para vehículo de transporte urbano  
**Docente:** [Nombre del profesor]  
**Fecha de elaboración:** [Fecha actual]

---

## Resumen ejecutivo  
_(El resumen se escribe al final de la practica para resaltar lo obtenido y las recomendaciones acerca del caso de estudio)_

**Síntesis de 200 palabras:**

El presente análisis evaluó tres motores de combustión interna para aplicación en microbuses urbanos de TransUrbe México. Se analizaron el Motor A (EcoUrban 1.8L), Motor B (CityPower 2.0L) y Motor C (MaxTorque 2.2L) mediante análisis termodinámicos, cálculos de eficiencia y evaluación de parámetros de desempeño.

Los resultados muestran que el **Motor B (CityPower 2.0L)** presenta la mejor combinación de eficiencia térmica teórica (60.8%), bajo consumo específico (260 g/kWh) y adecuado torque para aplicaciones urbanas (180 N⋅m @ 4,200 rpm). Su relación de compresión de 10.2:1 ofrece un balance óptimo entre eficiencia y confiabilidad.

El análisis económico indica que el Motor B generaría ahorros operativos de $2,400 MXN mensuales comparado con el Motor A, y $1,200 MXN vs. Motor C. La configuración DOHC del Motor B proporciona mejor rendimiento volumétrico, crucial para operación urbana con paradas frecuentes.

**Recomendación:** Seleccionar el Motor B (CityPower 2.0L) por su superior eficiencia energética, menor costo operativo y mejor adaptación a las condiciones de transporte urbano de Guadalajara.

---
## Introduccion 

En el contexto del **transporte urbano moderno**, la **selección del motor adecuado** para una aplicación específica requiere un **análisis termodinámico integral** que considere parámetros como **eficiencia, potencia, consumo de combustible** y **desempeño en diferentes condiciones operativas**. La comprensión de los **ciclos termodinámicos, balances de energía** y el **funcionamiento de componentes** es fundamental para tomar decisiones técnicas informadas.

El presente caso de estudio permite al estudiante **aplicar conceptos de termodinámica** en un escenario real de selección de motores, donde deberá **analizar ciclos P-V, calcular parámetros de desempeño** y **evaluar el funcionamiento** de diferentes configuraciones de motores de combustión interna para una aplicación de transporte urbano.

## Objetivo general 

**Analizar y comparar** las características termodinámicas de diferentes motores de combustión interna para **recomendar la mejor opción** para un vehículo de transporte urbano, considerando **ciclos termodinámicos, balances de energía, parámetros de desempeño** y **funcionamiento de componentes**.

## Descripcion  del caso de estudio

###  **Escenario:**

**"TransUrbe México"** es una empresa de transporte público que opera en Guadalajara, Jalisco. La compañía planea renovar su flota de **microbuses urbanos** y necesita seleccionar el motor más adecuado para sus nuevas unidades. El vehículo será utilizado para **rutas urbanas cortas** con frecuentes paradas y arranques.

### **Situación:**

El departamento técnico ha **pre-seleccionado tres motores** de diferentes fabricantes que cumplen con los requerimientos básicos de potencia y emisiones. Todos son motores de **4 tiempos y ciclo Otto**, pero tienen **diferentes configuraciones** y características de desempeño. La empresa necesita una **recomendación técnica fundamentada** basada en análisis termodinámico.

###  **Requerimientos operativos:**

- **Aplicación:** Microbús urbano de 20 pasajeros
- **Peso del vehículo cargado:** 4,500 kg
- **Velocidad promedio:** 25 km/h con paradas frecuentes
- **Operación diaria:** 12 horas continuas
- **Perfil de ruta:** 60% ciudad, 40% periférico
- **Combustible:** Gasolina Magna (87 octanos)
## Desarrollo de fases 
### Fase 1: Análisis de ciclos termodinámicos 

####  **Metodoloía de análisis**

#### **2.1 Diagramas P-V para cada motor**

**Paso 1:** Identificar los datos básicos de cada motor

| Motor | Cilindrada | Bore (mm) | Stroke (mm) | Relación Compresión |
| ----- | ---------- | --------- | ----------- | ------------------- |
| A     | 1,800 cm³  | 82        | 85          | 9.5:1               |
| B     | 2,000 cm³  | 86        | 86          | 10.2:1              |
| C     | 2,200 cm³  | 88        | 90          | 8.8:1               |

**Paso 2:** Calcular volúmenes característicos

**Fórmula:** V_cilindro = (π/4) × D² × L

**Motor A (ejemplo de cálculo):**

- V_desplazado = (π/4) × (82 mm)² × (85 mm) = 448.5 cm³
- V_total = V_desplazado × 4 cilindros = 1,794 cm³ ≈ 1,800 cm³ ✓
- V_cámara = V_desplazado/(rc-1) = 448.5/(9.5-1) = 52.8 cm³
- V_total_por_cilindro = V_desplazado + V_cámara = 448.5 + 52.8 = 501.3 cm³

**Motor B:**

- V_desplazado = (π/4) × (86)² × (86) = 500.0 cm³
- V_cámara = 500.0/(10.2-1) = 54.3 cm³

**Motor C:**

- V_desplazado = (π/4) × (88)² × (90) = 547.4 cm³
- V_cámara = 547.4/(8.8-1) = 70.2 cm³

**Paso 3:** Dibujar diagramas P-V

```
DIAGRAMA P-V CICLO OTTO (Ejemplo conceptual)

P (bar) ↑
        |    3 ●────● 2
        |     /      |
        |    /       |  } Combustión a V=const
        |   /        |
        |  /         |
        | /          |
        |/           |
        ●────────────● ──→ V (cm³)
        4            1
        |←── Expansión ──→|
        |←─ Compresión ──|

Estados del ciclo:
1→2: Compresión isentrópica  
2→3: Adición de calor (V=const)
3→4: Expansión isentrópica
4→1: Rechazo de calor (V=const)
```

**Paso 4:** Describir las 4 etapas del ciclo

**1→2 Compresión Isentrópica:**

- La mezcla aire-combustible se comprime desde PMI hasta PMS
- No hay intercambio de calor (Q = 0)
- Temperatura y presión aumentan según relaciones isentrópicas

**2→3 Adición de Calor (Combustión):**

- Ignición instantánea de la mezcla
- Volumen constante, presión aumenta drásticamente
- Máxima temperatura del ciclo

**3→4 Expansión Isentrópica:**

- Gases calientes empujan el pistón hacia PMI
- Generación de trabajo útil
- Temperatura y presión disminuyen

**4→1 Rechazo de Calor:**

- Escape de gases y enfriamiento
- Retorno a condiciones iniciales
- Volumen constante

### **2.2 Comparación de ciclos**

**Análisis de diferencias:**

1. **Motor A:** rc = 9.5 → Área menor en diagrama P-V → Menos trabajo por ciclo
2. **Motor B:** rc = 10.2 → Área intermedia → Balance eficiencia-confiabilidad
3. **Motor C:** rc = 8.8 + turbo → Presión inicial mayor (1.5 bar) → Modificación del ciclo básico

**Impacto del turboalimentador (Motor C):**

- Presión de admisión aumenta de 1.0 a 1.5 bar
- Temperatura de admisión sube a 45°C
- Mayor densidad de carga → Más potencia específica

---

# 3. DESARROLLO DE LA FASE 2: CÁLCULOS TERMODINÁMICOS (3.0 pts)

## **METODOLOGÍA DE CÁLCULOS:**

### **3.1 Eficiencia térmica teórica del ciclo Otto**

**Fórmula base:** ηOtto = 1 - (1/r^(γ-1))

Donde: γ = 1.4 (aire), γ-1 = 0.4

**Paso 1:** Calcular para cada motor

**Motor A (rc = 9.5):**

```
ηOtto = 1 - (1/9.5^0.4)
     = 1 - (1/2.512)
     = 1 - 0.398
     = 0.602 = 60.2%
```

**Motor B (rc = 10.2):**

```
ηOtto = 1 - (1/10.2^0.4)
     = 1 - (1/2.553)
     = 1 - 0.392
     = 0.608 = 60.8%
```

**Motor C (rc = 8.8):**

```
ηOtto = 1 - (1/8.8^0.4)
     = 1 - (1/2.454)
     = 1 - 0.407
     = 0.593 = 59.3%
```

**Paso 2:** Comparar con eficiencias reales

|Motor|η Teórica|η Real (dada)|Diferencia|
|---|---|---|---|
|A|60.2%|38%|-22.2%|
|B|60.8%|42%|-18.8%|
|C|59.3%|40%|-19.3%|

**Análisis:** Las diferencias representan pérdidas por fricción, transferencia de calor, combustión incompleta y otros factores reales.

### **3.2 Relaciones isentrópicas**

**Fórmulas:**

- T₂/T₁ = r^(γ-1) = r^0.4
- P₂/P₁ = r^γ = r^1.4

**Condiciones iniciales:**

- T₁ = 298 K (25°C)
- P₁ = 1.0 bar

**Paso 1:** Temperatura al final de compresión

**Motor A:**

```
T₂ = T₁ × r^0.4 = 298 × 9.5^0.4 = 298 × 2.512 = 749 K = 476°C
```

**Motor B:**

```
T₂ = 298 × 10.2^0.4 = 298 × 2.553 = 761 K = 488°C
```

**Motor C:**

```
T₂ = 298 × 8.8^0.4 = 298 × 2.454 = 731 K = 458°C
```

**Paso 2:** Presión al final de compresión

**Motor A:**

```
P₂ = P₁ × r^1.4 = 1.0 × 9.5^1.4 = 1.0 × 23.9 = 23.9 bar
```

**Motor B:**

```
P₂ = 1.0 × 10.2^1.4 = 1.0 × 26.0 = 26.0 bar
```

**Motor C:**

```
P₂ = 1.5 × 8.8^1.4 = 1.5 × 21.6 = 32.4 bar
(Nota: P₁ = 1.5 bar por turboalimentación)
```

### **3.3 Balance de energía**

**Datos para cálculo (por kg de aire):**

- cv = 0.718 kJ/(kg⋅K)

**Paso 1:** Temperaturas máximas (dadas)

- Motor A: T₃ = 1800°C = 2073 K
- Motor B: T₃ = 1950°C = 2223 K
- Motor C: T₃ = 2100°C = 2373 K

**Paso 2:** Temperatura al final de expansión **Fórmula:** T₄ = T₃ × (1/r)^0.4

**Motor A:**

```
T₄ = 2073 × (1/9.5)^0.4 = 2073 × 0.398 = 825 K = 552°C
```

**Motor B:**

```
T₄ = 2223 × (1/10.2)^0.4 = 2223 × 0.392 = 871 K = 598°C
```

**Motor C:**

```
T₄ = 2373 × (1/8.8)^0.4 = 2373 × 0.407 = 966 K = 693°C
```

**Paso 3:** Transferencias de calor

**Calor añadido:** Q_H = cv × (T₃ - T₂)

**Motor A:**

```
Q_H = 0.718 × (2073 - 749) = 0.718 × 1324 = 951 kJ/kg
```

**Motor B:**

```
Q_H = 0.718 × (2223 - 761) = 0.718 × 1462 = 1050 kJ/kg
```

**Motor C:**

```
Q_H = 0.718 × (2373 - 731) = 0.718 × 1642 = 1179 kJ/kg
```

**Calor rechazado:** Q_L = cv × (T₄ - T₁)

**Motor A:**

```
Q_L = 0.718 × (825 - 298) = 0.718 × 527 = 378 kJ/kg
```

**Motor B:**

```
Q_L = 0.718 × (871 - 298) = 0.718 × 573 = 411 kJ/kg
```

**Motor C:**

```
Q_L = 0.718 × (966 - 298) = 0.718 × 668 = 480 kJ/kg
```

**Trabajo neto:** W_neto = Q_H - Q_L

|Motor|Q_H (kJ/kg)|Q_L (kJ/kg)|W_neto (kJ/kg)|η_calculada|
|---|---|---|---|---|
|A|951|378|573|60.2%|
|B|1050|411|639|60.9%|
|C|1179|480|699|59.3%|

### **3.4 Análisis de consumo específico**

**Paso 1:** Consumo horario a 80 HP promedio

**Fórmula:** Consumo = Potencia × Factor_conversión × Consumo_específico

**Motor A:**

```
Consumo = 80 HP × 0.746 kW/HP × 280 g/kWh = 16.7 kg/h
```

**Motor B:**

```
Consumo = 80 HP × 0.746 kW/HP × 260 g/kWh = 15.5 kg/h
```

**Motor C:**

```
Consumo = 80 HP × 0.746 kW/HP × 270 g/kWh = 16.1 kg/h
```

**Paso 2:** Costo operativo diario

**Datos:** 12 horas operación, gasolina $24/L, densidad 0.75 kg/L

**Motor A:**

```
Litros/día = 16.7 kg/h × 12 h ÷ 0.75 kg/L = 267 L/día
Costo/día = 267 L × $24/L = $6,408 MXN/día
```

**Motor B:**

```
Litros/día = 15.5 × 12 ÷ 0.75 = 248 L/día  
Costo/día = 248 × $24 = $5,952 MXN/día
```

**Motor C:**

```
Litros/día = 16.1 × 12 ÷ 0.75 = 257 L/día
Costo/día = 257 × $24 = $6,168 MXN/día
```

**Resumen económico:**

|Motor|Consumo (L/día)|Costo/día|Ahorro vs A|Ahorro vs C|
|---|---|---|---|---|
|A|267|$6,408|-|-$240|
|B|248|$5,952|$456|$216|
|C|257|$6,168|$240|-|

---

# 4. DESARROLLO DE LA FASE 3: PARÁMETROS DE DESEMPEÑO (2.0 pts)

## **METODOLOGÍA DE ANÁLISIS:**

### **4.1 Cálculo de parámetros principales**

**Paso 1:** Potencia específica (HP/L)

|Motor|Potencia (HP)|Cilindrada (L)|Potencia específica|
|---|---|---|---|
|A|120|1.8|66.7 HP/L|
|B|140|2.0|70.0 HP/L|
|C|160|2.2|72.7 HP/L|

**Análisis:** Motor C tiene mayor potencia específica gracias al turboalimentador.

**Paso 2:** Torque específico (N⋅m/L)

|Motor|Torque (N⋅m)|Cilindrada (L)|Torque específico|
|---|---|---|---|
|A|165|1.8|91.7 N⋅m/L|
|B|180|2.0|90.0 N⋅m/L|
|C|220|2.2|100.0 N⋅m/L|

### **4.2 Análisis para uso urbano**

**Evaluación de factores críticos:**

**Torque a bajas RPM:**

- Motor A: 165 N⋅m @ 3,800 rpm (intermedio)
- Motor B: 180 N⋅m @ 4,200 rpm (adecuado)
- Motor C: 220 N⋅m @ 2,800 rpm (excelente)

**Respuesta del acelerador:**

- Motor A: SOHC → Respuesta moderada
- Motor B: DOHC → Mejor respuesta
- Motor C: Turbo → Respuesta rápida pero con lag

**Consumo urbano estimado:** Basado en cálculos previos, el Motor B ofrece el mejor balance.

---

# 5. DESARROLLO DE LA FASE 4: COMPONENTES Y FUNCIONAMIENTO (1.5 pts)

## **METODOLOGÍA DE ANÁLISIS:**

### **5.1 Análisis de componentes principales**

**Cilindro:**

- **Diámetro y carrera:** Motor C tiene mayor diámetro (88mm) → Mayor área de pistón → Mayor fuerza
- **Relación carrera/diámetro:** Motor B (86/86=1.0) → Diseño cuadrado balanceado

**Pistón:**

- **Velocidad media:** Vm = 2 × Carrera × RPM / 60
- Motor A: Vm = 2 × 85 × 5500 / 60 = 15.6 m/s
- Motor B: Vm = 2 × 86 × 6000 / 60 = 17.2 m/s
- Motor C: Vm = 2 × 90 × 5200 / 60 = 15.6 m/s

**Cigüeñal:**

- Configuración 4 cilindros en línea
- Orden de encendido: 1-3-4-2 (típico)
- Balance dinámico mejor en motores cuadrados (Motor B)

### **5.2 Sistemas auxiliares**

**SOHC vs DOHC:**

- Motor A y C: SOHC → 2 válvulas/cilindro → Menor costo
- Motor B: DOHC → 4 válvulas/cilindro → Mejor llenado

**Turboalimentación (Motor C):**

- Ventajas: Mayor potencia específica, mejor torque
- Desventajas: Complejidad, lag de respuesta, mayor temperatura

---

# 6. DESARROLLO DE LA FASE 5: RECOMENDACIÓN TÉCNICA (0.5 pts)

## **METODOLOGÍA DE DECISIÓN:**

### **6.1 Matriz de evaluación**

|**Criterio**|**Peso (%)**|**Motor A**|**Motor B**|**Motor C**|
|---|---|---|---|---|
|Eficiencia térmica|25%|3 (60.2%)|5 (60.8%)|4 (59.3%)|
|Torque a bajas RPM|20%|3 (3800 rpm)|4 (4200 rpm)|5 (2800 rpm)|
|Consumo de combustible|20%|2 (280 g/kWh)|5 (260 g/kWh)|4 (270 g/kWh)|
|Potencia específica|15%|3 (66.7 HP/L)|4 (70.0 HP/L)|5 (72.7 HP/L)|
|Complejidad/Mantenimiento|10%|5 (SOHC simple)|4 (DOHC moderado)|2 (Turbo complejo)|
|Costo operativo|10%|2 ($6,408/día)|5 ($5,952/día)|4 ($6,168/día)|

**Cálculo de puntajes ponderados:**

**Motor A:** (3×25 + 3×20 + 2×20 + 3×15 + 5×10 + 2×10) = 290/100 = **2.90**

**Motor B:** (5×25 + 4×20 + 5×20 + 4×15 + 4×10 + 5×10) = 430/100 = **4.30**

**Motor C:** (4×25 + 5×20 + 4×20 + 5×15 + 2×10 + 4×10) = 395/100 = **3.95**

### **6.2 Recomendación final**

**MOTOR RECOMENDADO: Motor B (CityPower 2.0L)**

**Justificación técnica:**

1. **Mayor eficiencia térmica:** 60.8% teórica, 42% real
2. **Mejor consumo específico:** 260 g/kWh vs. 280 (A) y 270 (C)
3. **Balance óptimo:** Potencia adecuada (140 HP) para aplicación urbana
4. **Configuración DOHC:** Mejor rendimiento volumétrico
5. **Menor costo operativo:** $456/día de ahorro vs. Motor A

**Beneficios esperados:**

- Ahorro anual: $166,440 MXN vs. Motor A
- Menor mantenimiento que Motor C (sin turbo)
- Emisiones menores por mejor eficiencia
- Mejor respuesta en tráfico urbano

**Consideraciones especiales:**

- Implementar programa de mantenimiento preventivo
- Capacitar operadores en manejo eficiente
- Monitorear consumo real vs. proyectado

---

# CONCLUSIONES METODOLÓGICAS PARA ESTUDIANTES

## **PROCESO SISTEMÁTICO APLICADO:**

### **1. Análisis de datos (Organización)**

- Tabular información técnica
- Identificar parámetros clave
- Establecer criterios de comparación

### **2. Cálculos termodinámicos (Aplicación teórica)**

- Usar fórmulas específicas de la materia
- Verificar resultados con datos reales
- Analizar diferencias teórico vs. real

### **3. Evaluación multicriterio (Análisis integral)**

- Definir criterios relevantes para la aplicación
- Asignar pesos según importancia
- Cuantificar evaluación objetivamente

### **4. Recomendación fundamentada (Síntesis)**

- Basar decisión en análisis técnico
- Considerar aspectos económicos
- Incluir plan de implementación

**LECCIONES CLAVE:**

- Siempre verificar cálculos con múltiples métodos
- Considerar limitaciones de modelos teóricos
- Documentar assumptions y restricciones
- Presentar resultados de forma clara y ejecutiva

---

**NOTA IMPORTANTE:** Este ejemplo metodológico muestra el proceso completo de análisis. Los estudiantes deben aplicar la misma metodología a sus propios casos con datos diferentes, siguiendo cada paso sistemáticamente.