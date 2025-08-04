# ER.04.01.01 Práctica Modular: Análisis Térmico Integral de un Motor Automotriz

## Información General

**Duración:** 3 horas  
**Modalidad:** Presencial - Laboratorio  
**Tipo:** Evaluación de Recuperación (ER)  
**Competencia:** Analizar el comportamiento termodinámico y térmico de sistemas automotrices mediante cálculos y mediciones experimentales

## Objetivos

### Objetivo General
Realizar un análisis térmico integral de un sistema motor-refrigeración, integrando los principios de ciclos termodinámicos y transferencia de calor para evaluar eficiencia y gestión térmica.

### Objetivos Específicos
1. **Analizar** el ciclo termodinámico teórico del motor y calcular parámetros de rendimiento
2. **Medir** temperaturas en diferentes componentes del sistema térmico
3. **Calcular** transferencias de calor por los tres mecanismos fundamentales
4. **Evaluar** la eficiencia real vs teórica del sistema
5. **Proponer** mejoras para optimización térmica

## Estructura Modular (3 Horas)

### **MÓDULO 1: Análisis Teórico del Ciclo (45 min)**
#### Actividades:
- Identificación de parámetros del motor de prueba
- Cálculo del ciclo Otto ideal
- Determinación de eficiencia teórica
- Análisis de estados termodinámicos

### **MÓDULO 2: Mediciones Experimentales (90 min)**
#### Actividades:
- Instrumentación del sistema (termopares, manómetros)
- Medición de temperaturas en régimen estacionario
- Registro de presiones y flujos
- Medición de potencia desarrollada

### **MÓDULO 3: Análisis de Transferencia de Calor (60 min)**
#### Actividades:
- Cálculo de conducción en componentes
- Análisis de convección en radiador
- Evaluación de radiación en múltiple de escape
- Balance térmico del sistema

### **MÓDULO 4: Evaluación y Propuestas (25 min)**
#### Actividades:
- Comparación teórico vs experimental
- Identificación de pérdidas térmicas
- Propuestas de mejora
- Presentación de resultados

---

## Material y Equipo Requerido

### **Motor de Prueba**
- Motor monocilíndrico 4 tiempos (125-200 cc)
- Sistema de enfriamiento por agua
- Instrumentación básica (tacómetro, manómetros)
- Dinamómetro o carga eléctrica

### **Instrumentos de Medición**
- **Termómetros digitales** con sondas (6 unidades)
- **Manómetros** para presión de admisión y aceite
- **Medidor de flujo** de combustible
- **Cronómetro** digital
- **Balanza** de precisión (para combustible)
- **Multímetro** (para mediciones eléctricas)

### **Materiales Complementarios**
- **Termómetro infrarrojo** (para medición sin contacto)
- **Calculadora científica** o laptop
- **Hojas de registro de datos**
- **Graficas y tablas** de propiedades termodinámicas

---

## Desarrollo de la Práctica

### **MÓDULO 1: Análisis Teórico del Ciclo (45 min)**

#### **Actividad 1.1: Caracterización del Motor (15 min)**

Los estudiantes deben identificar y registrar:

**Datos del Motor:**
- Cilindrada: _____ cm³
- Relación de compresión: r = _____
- Diámetro del pistón: _____ mm
- Carrera: _____ mm
- RPM de operación: _____ rpm

**Condiciones Ambientales:**
- Temperatura ambiente: T₁ = _____ °C
- Presión atmosférica: P₁ = _____ kPa
- Humedad relativa: _____ %

#### **Actividad 1.2: Cálculo del Ciclo Otto Ideal (20 min)**

**Paso 1:** Determinar la eficiencia térmica teórica
$$\eta_{Otto} = 1 - \frac{1}{r^{\gamma-1}}$$

**Donde:** r = relación de compresión, γ = 1.4 (aire)

**Paso 2:** Calcular temperaturas y presiones en cada estado
- **Estado 1 (admisión):** T₁ = T_ambiente, P₁ = P_atmosférica
- **Estado 2 (final compresión):** $T_2 = T_1 \times r^{\gamma-1}$, $P_2 = P_1 \times r^{\gamma}$
- **Estado 3 (final combustión):** Calculado con calor agregado
- **Estado 4 (final expansión):** Usando relaciones isentrópicas

**Paso 3:** Determinar trabajo específico teórico
$$w_{neto} = c_v(T_3 - T_2) - c_v(T_4 - T_1)$$

#### **Actividad 1.3: Predicciones Teóricas (10 min)**

Calcular para las condiciones de operación:
- **Potencia teórica** esperada
- **Consumo específico** teórico de combustible
- **Temperaturas** esperadas en diferentes puntos

### **MÓDULO 2: Mediciones Experimentales (90 min)**

#### **Actividad 2.1: Preparación e Instrumentación (20 min)**

**Instalación de Sensores:**
1. **Termosensor 1:** Temperatura de admisión (después del filtro)
2. **Termosensor 2:** Temperatura de escape (múltiple)
3. **Termosensor 3:** Temperatura del refrigerante (entrada radiador)
4. **Termosensor 4:** Temperatura del refrigerante (salida radiador)
5. **Termosensor 5:** Temperatura de la culata
6. **Termosensor 6:** Temperatura ambiente

**Verificación de Instrumentos:**
- Calibración de termómetros
- Verificación de manómetros
- Preparación de cronómetros

#### **Actividad 2.2: Operación en Régimen Estacionario (40 min)**

**Procedimiento de Arranque:**
1. Verificar niveles (aceite, combustible, refrigerante)
2. Arranque del motor a ralentí
3. Calentamiento hasta temperatura operativa (5-10 min)
4. Establecimiento de carga constante

**Toma de Datos (Cada 5 minutos durante 30 minutos):**

| Tiempo | T₁ | T₂ | T₃ | T₄ | T₅ | T₆ | RPM | P_admisión | Observaciones |
|--------|----|----|----|----|----|----|-----|------------|---------------|
| 0 min  |    |    |    |    |    |    |     |            |               |
| 5 min  |    |    |    |    |    |    |     |            |               |
| 10 min |    |    |    |    |    |    |     |            |               |
| 15 min |    |    |    |    |    |    |     |            |               |
| 20 min |    |    |    |    |    |    |     |            |               |
| 25 min |    |    |    |    |    |    |     |            |               |
| 30 min |    |    |    |    |    |    |     |            |               |

#### **Actividad 2.3: Medición de Potencia y Consumo (30 min)**

**Medición de Potencia (Método de Carga Eléctrica):**
- Conectar carga resistiva controlable
- Medir corriente y voltaje
- Calcular potencia eléctrica generada
- Considerar eficiencia del generador

**Medición de Consumo de Combustible:**
1. Llenar tanque hasta rebose
2. Operar por tiempo determinado (15 min)
3. Volver a llenar midiendo combustible agregado
4. Calcular consumo por unidad de tiempo

### **MÓDULO 3: Análisis de Transferencia de Calor (60 min)**

#### **Actividad 3.1: Conducción en la Culata (15 min)**

**Medición:**
- Temperatura superficie interna (T_escape): _____ °C
- Temperatura superficie externa (T_ambiente): _____ °C
- Espesor efectivo de pared: e = 8 mm (típico)
- Área estimada de transferencia: A = 0.01 m² (típico)

**Cálculo:**
$$\dot{Q}_{conducción} = \frac{k_{hierro} \times A \times (T_{escape} - T_{ambiente})}{e}$$

**Donde:** k_hierro = 52 W/m·K

#### **Actividad 3.2: Convección en el Radiador (20 min)**

**Datos Medidos:**
- Temperatura entrada radiador: T_entrada = _____ °C
- Temperatura salida radiador: T_salida = _____ °C
- Temperatura aire ambiente: T_ambiente = _____ °C
- Área superficial radiador: A_radiador = 0.5 m² (estimado)

**Cálculo de Transferencia por Convección:**
$$\dot{Q}_{convección} = h \times A_{radiador} \times (T_{promedio} - T_{ambiente})$$

**Donde:**
- T_promedio = (T_entrada + T_salida)/2
- h = 50 W/m²·K (convección natural + ventilación)

#### **Actividad 3.3: Radiación del Múltiple de Escape (15 min)**

**Medición con Termómetro Infrarrojo:**
- Temperatura superficie múltiple: T_múltiple = _____ °C
- Temperatura ambiente: T_ambiente = _____ °C
- Área superficial estimada: A_múltiple = 0.05 m²
- Emisividad acero: ε = 0.7

**Cálculo:**
$$\dot{Q}_{radiación} = ε \times σ \times A_{múltiple} \times (T_{múltiple}^4 - T_{ambiente}^4)$$

**Conversión a Kelvin:** T(K) = T(°C) + 273.15

#### **Actividad 3.4: Balance Térmico Global (10 min)**

**Energía de Entrada:**
- Potencia calorífica del combustible: $\dot{Q}_{combustible} = \dot{m}_{combustible} \times PCI$
- PCI gasolina ≈ 44,000 kJ/kg

**Energía de Salida:**
- Trabajo útil: $\dot{W}_{útil}$ (medido)
- Calor al refrigerante: $\dot{Q}_{refrigerante}$
- Calor por escape: $\dot{Q}_{escape}$
- Radiación: $\dot{Q}_{radiación}$

**Verificación del Balance:**
$$\dot{Q}_{entrada} = \dot{W}_{útil} + \dot{Q}_{perdidas}$$

### **MÓDULO 4: Evaluación y Propuestas (25 min)**

#### **Actividad 4.1: Análisis Comparativo (10 min)**

**Tabla de Comparación:**

| Parámetro | Teórico | Experimental | Diferencia (%) |
|-----------|---------|--------------|----------------|
| Eficiencia térmica | _____ % | _____ % | _____ % |
| Potencia específica | _____ kW/L | _____ kW/L | _____ % |
| Temperatura máxima | _____ °C | _____ °C | _____ % |
| Consumo específico | _____ g/kWh | _____ g/kWh | _____ % |

#### **Actividad 4.2: Identificación de Pérdidas (10 min)**

**Análisis de Pérdidas Térmicas:**
1. **Pérdidas por escape:** _____ % de la energía total
2. **Pérdidas al refrigerante:** _____ % de la energía total
3. **Pérdidas por radiación:** _____ % de la energía total
4. **Pérdidas mecánicas:** _____ % de la energía total

#### **Actividad 4.3: Propuestas de Mejora (5 min)**

**Propuestas Técnicas:**
1. **Para mejorar eficiencia:**
   - Aumentar relación de compresión
   - Mejorar aislamiento térmico
   - Optimizar tiempo de encendido

2. **Para mejorar gestión térmica:**
   - Incrementar área del radiador
   - Mejorar flujo de aire
   - Usar materiales de mayor conductividad

3. **Para reducir emisiones:**
   - Optimizar mezcla aire-combustible
   - Mejorar sistema de escape
   - Implementar recirculación EGR

---

## Formato de Reporte

### **Sección 1: Datos y Cálculos Teóricos**
- Parámetros del motor
- Cálculos del ciclo Otto
- Predicciones teóricas

### **Sección 2: Resultados Experimentales**
- Tablas de mediciones
- Gráficas de temperatura vs tiempo
- Cálculos de potencia y consumo

### **Sección 3: Análisis de Transferencia de Calor**
- Cálculos de conducción, convección y radiación
- Balance térmico global
- Distribución de pérdidas

### **Sección 4: Análisis y Conclusiones**
- Comparación teórico vs experimental
- Análisis de eficiencia
- Propuestas de mejora justificadas

---

## Criterios de Evaluación

| Criterio | Peso | Descripción |
|----------|------|-------------|
| **Cálculos Teóricos** | 25% | Correcta aplicación de ecuaciones de ciclos termodinámicos |
| **Mediciones Experimentales** | 20% | Precisión y sistematización en la toma de datos |
| **Análisis de Transferencia** | 25% | Correcta aplicación de leyes de transferencia de calor |
| **Balance Térmico** | 15% | Coherencia en el análisis energético global |
| **Análisis Crítico** | 10% | Calidad del análisis comparativo y propuestas |
| **Presentación** | 5% | Claridad y organización del reporte |

## Recursos de Apoyo

### **Ecuaciones Clave**

**Ciclo Otto:**
- $\eta = 1 - \frac{1}{r^{\gamma-1}}$
- $T_2 = T_1 \times r^{\gamma-1}$
- $P_2 = P_1 \times r^{\gamma}$

**Transferencia de Calor:**
- Conducción: $\dot{Q} = \frac{kA\Delta T}{L}$
- Convección: $\dot{Q} = hA(T_s - T_\infty)$
- Radiación: $\dot{Q} = εσA(T_s^4 - T_{ambiente}^4)$

### **Propiedades Útiles**
- γ (aire) = 1.4
- k (hierro fundido) = 52 W/m·K
- σ = 5.67 × 10⁻⁸ W/m²·K⁴
- PCI gasolina ≈ 44,000 kJ/kg

## Medidas de Seguridad

1. **Uso obligatorio** de equipo de protección personal
2. **Ventilación adecuada** para gases de escape
3. **Extintor** cerca del área de trabajo
4. **Supervisión constante** durante operación del motor
5. **Procedimiento de parada** de emergencia claramente definido

---

*Esta práctica integra de manera efectiva los conceptos teóricos de ciclos termodinámicos y transferencia de calor con mediciones experimentales factibles en un laboratorio universitario estándar.*