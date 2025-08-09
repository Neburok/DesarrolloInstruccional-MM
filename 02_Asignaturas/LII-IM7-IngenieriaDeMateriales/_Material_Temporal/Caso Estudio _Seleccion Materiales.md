
# Caso de Estudio: Bastón Inteligente para Adultos Mayores

## Selección de Materiales usando Metodología Gráfica de Ashby

### **Contexto del Problema**

La población mundial está envejeciendo rápidamente. En México, los adultos mayores representarán el 25% de la población para 2050. Muchos requieren asistencia para caminar, pero los bastones tradicionales presentan las siguientes limitaciones:

- **Peso excesivo** que causa fatiga en uso prolongado
- **Falta de resistencia** que lleva a fracturas peligrosas
- **Diseño no ergonómico** que genera incomodidad
- **Costo elevado** que limita el acceso

### **Oportunidad de Innovación**

La startup mexicana **"AsistTech"** quiere desarrollar un bastón inteligente con las siguientes características:

- GPS integrado para localización familiar
- Sensores de caída para alertas automáticas
- **Peso mínimo** para fácil manipulación
- **Máxima resistencia** para seguridad del usuario

### **Tu Misión como Ingeniero**

Como ingeniero de producto en AsistTech, debes **seleccionar el material óptimo para el tubo principal** del bastón inteligente. El bastón debe soportar de manera segura a personas de hasta 120 kg sin pandear, siendo lo más ligero posible para facilitar su uso prolongado.

---

## **Especificaciones Técnicas**

### **Dimensiones del Bastón:**

- **Longitud ajustable:** 80-100 cm (crítica: 100 cm)
- **Diámetro exterior:** 25 mm (fijo por ergonomía)
- **Espesor de pared:** Variable de diseño

### **Condiciones de Carga:**

- **Carga máxima:** 120 kg (1,177 N)
- **Factor de seguridad:** 2.5
- **Componentes adicionales:** Electrónicos (200 g) + empuñadura (150 g)

### **Ambiente de Uso:**

- **Ubicación:** Interior/exterior urbano
- **Temperatura:** 0°C a 40°C
- **Humedad:** Hasta 80% HR
- **Vida útil objetivo:** 5 años

---

## **Análisis a Realizar**

### **Paso 1: Identificación del Modo de Falla**

- ¿Cuál es el modo de falla más crítico: **pandeo** o **fractura**?
- Justifica tu respuesta considerando las dimensiones del bastón

### **Paso 2: Análisis de Pandeo**

El bastón se modela como una **columna con carga axial**. Aplica la ecuación de pandeo de Euler:

**Carga crítica:** $P_{cr} = \frac{\pi^2 EI}{(KL)^2}$

Donde:

- **E** = Módulo elástico del material
- **I** = Momento de inercia de la sección
- **K** ≈ 1 (un extremo fijo, otro libre)
- **L** = 1.0 m

Para tubo hueco: $I \approx \frac{\pi D^3 t}{8}$

**Condición de seguridad:** $P_{cr} \geq 2.5 \times 1,177 = 2,943$ N

### **Paso 3: Obtención del Índice de Mérito**

Para **minimizar la masa** del bastón, sigue estos pasos:

1. Despeja el espesor mínimo de la condición de pandeo
2. Calcula la masa en función del espesor
3. Demuestra que el **Índice de Mérito** es: $M = \frac{E}{\rho}$

### **Paso 4: Selección Gráfica**

- Usa el diagrama **Módulo Elástico vs Densidad**
- Traza la línea de selección (pendiente = 1)
- Identifica los 3 mejores candidatos

---

## **Restricciones Simplificadas**

1. **Resistencia al pandeo** ≥ 2,943 N
2. **Costo del material** < $15 USD/kg

---

## **Materiales de Referencia**

Considera al menos estos candidatos en tu análisis:

|Material|E (GPa)|ρ (kg/m³)|Costo aprox. (USD/kg)|
|---|---|---|---|
|Fibra de Carbono (CFRP)|150|1600|$50-100|
|Bambú|20|600|$2-5|
|Aleación Al 6061-T6|70|2700|$3-5|
|Aleación Mg AZ80|45|1800|$8-12|
|PA66 reforzado (30% fibra vidrio)|10|1350|$4-6|
|Acero 1020|200|7800|$1-2|

---

## **Preguntas Guía para la Sesión**

1. ¿Por qué es más crítico el **pandeo** que la **fractura** en este bastón?
2. ¿Por qué el índice de mérito es **E/ρ** y no **σf/ρ**?
3. ¿Cuáles son los **3 materiales** con mejor índice E/ρ?
4. Considerando también el **costo**, ¿cuál recomendarías?

---

## **Actividad

### **Parte 1: Análisis del Problema** 

- Identificar modo de falla crítico
- Establecer ecuación de pandeo

### **Parte 2: Derivación del Índice** 

- Obtener M = E/ρ paso a paso
- Explicar el significado físico

### **Parte 3: Aplicación del Diagrama** 

- Usar diagrama E vs ρ
- Calcular índices para candidatos
- Ranking de materiales

### **Parte 4: Decisión Final** 

- Selección considerando costo
- Justificación de la recomendación