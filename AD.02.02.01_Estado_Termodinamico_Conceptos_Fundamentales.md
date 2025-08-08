# AD.02.02.01 - Estado Termodinámico: Conceptos Fundamentales

**Asignatura:** Termodinámica  
**Carrera:** Ingeniería en Alimentos  
**Unidad:** 2 - Propiedades de las sustancias puras  
**Tema:** 2 - Definición del estado termodinámico  

---

## B) Contenido

El presente documento aborda los **conceptos fundamentales del estado termodinámico** de las sustancias, con énfasis en su aplicación en la industria alimentaria. Se desarrollan los principios teóricos necesarios para comprender cómo las **variables termodinámicas** definen completamente el estado de un sistema, proporcionando las bases conceptuales para el análisis de procesos térmicos en alimentos.

**Objetivos de aprendizaje:**
- Explicar el concepto de **estado termodinámico** de las sustancias
- Comprender la relación entre **variables termodinámicas** en sustancias puras
- Identificar las **propiedades termodinámicas** relevantes en procesos alimentarios
- Aplicar los conceptos teóricos en situaciones prácticas de la industria alimentaria

---

## C) Introducción

En la industria alimentaria, el control y comprensión de las **condiciones termodinámicas** es esencial para garantizar la calidad, seguridad y eficiencia de los procesos. Desde la **pasteurización** de la leche hasta la **liofilización** de café, cada proceso involucra cambios en el **estado termodinámico** de las sustancias.

El **estado termodinámico** de una sustancia se refiere a su condición física y química en un momento específico, definida completamente por un conjunto de **propiedades termodinámicas** medibles. Esta comprensión permite a los ingenieros en alimentos diseñar, optimizar y controlar procesos térmicos de manera efectiva.

Consideremos el proceso de **esterilización** de conservas alimentarias: para garantizar la eliminación de microorganismos patógenos, es fundamental conocer exactamente el estado del vapor de agua utilizado. ¿Se encuentra en estado **saturado** o **sobrecalentado**? ¿Cuál es su **temperatura** y **presión**? Estas preguntas solo pueden responderse mediante una comprensión sólida del concepto de estado termodinámico.

---

## D) Desarrollo

### 4.1 Concepto de Estado Termodinámico

El **estado termodinámico** de un sistema se define como la condición física específica en la que se encuentra una sustancia en un momento determinado. Esta condición queda completamente caracterizada por el conjunto de **propiedades termodinámicas** que posee el sistema.

**Definición formal:**
> Un **estado termodinámico** es una condición macroscópica específica de un sistema, definida por los valores de sus propiedades termodinámicas independientes.

Para comprender este concepto, consideremos el ejemplo del agua utilizada en un proceso de **blanqueado** de vegetales:

- **Estado inicial:** Agua líquida a $T_1 = 20°C$ y $P_1 = 1 \text{ atm}$
- **Estado final:** Vapor de agua a $T_2 = 100°C$ y $P_2 = 1 \text{ atm}$

Cada uno de estos estados representa una **condición termodinámica** específica y completamente definida.

### 4.2 Propiedades Termodinámicas

Las **propiedades termodinámicas** son características medibles de un sistema que definen su estado. Se clasifican en dos categorías principales:

#### 4.2.1 Propiedades Intensivas

Las **propiedades intensivas** son independientes de la cantidad de masa del sistema. Estas propiedades son uniformes en todo el sistema en equilibrio.

**Principales propiedades intensivas:**

- **Temperatura ($T$):** Medida de la energía cinética promedio de las moléculas
  - Unidades: $K$, $°C$, $°F$
  - En alimentos: temperatura de **cocción**, **refrigeración**, **congelación**

- **Presión ($P$):** Fuerza por unidad de área ejercida por el fluido
  - Unidades: $Pa$, $bar$, $atm$, $psi$
  - En alimentos: presión en **autoclaves**, **evaporadores**, sistemas de **envasado al vacío**

- **Densidad ($\rho$):** Masa por unidad de volumen
  - Unidades: $kg/m^3$, $g/cm^3$
  - En alimentos: densidad de **jugos concentrados**, **aceites**, **miel**

#### 4.2.2 Propiedades Extensivas

Las **propiedades extensivas** dependen de la cantidad de masa del sistema. Son proporcionales al tamaño del sistema.

**Principales propiedades extensivas:**

- **Masa ($m$):** Cantidad de materia en el sistema
  - Unidades: $kg$, $g$
  
- **Volumen ($V$):** Espacio ocupado por el sistema
  - Unidades: $m^3$, $L$
  
- **Energía interna ($U$):** Energía total contenida en el sistema
  - Unidades: $J$, $kJ$

**Propiedades específicas:** Las propiedades extensivas pueden expresarse por unidad de masa, convirtiéndose en **propiedades intensivas específicas**:

- **Volumen específico:** $v = \frac{V}{m}$ $(m^3/kg)$
- **Energía interna específica:** $u = \frac{U}{m}$ $(J/kg)$

### 4.3 Postulado del Estado

El **postulado del estado** es un principio fundamental que establece:

> **Para una sustancia pura en equilibrio, el estado termodinámico queda completamente determinado por el conocimiento de dos propiedades termodinámicas intensivas independientes.**

**Implicaciones del postulado:**

1. **Dos propiedades independientes** son suficientes para definir completamente el estado
2. Una vez conocidas estas dos propiedades, **todas las demás propiedades** están determinadas
3. Las propiedades deben ser **independientes** (no relacionadas por ecuaciones)

**Ejemplo en procesamiento de alimentos:**

En un **evaporador** de jugo de naranja:
- Si conocemos $T = 65°C$ y $P = 0.2 \text{ bar}$ del vapor
- Automáticamente quedan determinados: densidad ($\rho$), volumen específico ($v$), entalpía ($h$), entropía ($s$)

### 4.4 Variables de Estado en Sustancias Puras

Para **sustancias puras**, las combinaciones más comunes de variables independientes son:

#### 4.4.1 Combinación Presión-Temperatura ($P, T$)

- **Aplicación:** Sistemas en **equilibrio de fases**
- **Limitación:** No válida en la **región bifásica** (coexistencia de fases)
- **Uso en alimentos:** Control de **esterilización**, **pasteurización**

**Ejemplo:** En la **esterilización** de conservas a $T = 121°C$, la presión del vapor saturado está automáticamente determinada como $P = 2.03 \text{ bar}$.

#### 4.4.2 Combinación Presión-Volumen específico ($P, v$)

- **Aplicación:** Análisis de **procesos de compresión** y **expansión**
- **Ventaja:** Válida en **todas las regiones**, incluida la bifásica
- **Uso en alimentos:** Diseño de **compresores** en refrigeración

#### 4.4.3 Combinación Temperatura-Volumen específico ($T, v$)

- **Aplicación:** Análisis de **procesos a presión constante**
- **Uso en alimentos:** **Secado** por aire caliente, **horneado**

### 4.5 Relación entre Variables Termodinámicas

Las **variables termodinámicas** no son independientes entre sí; están relacionadas por **ecuaciones de estado** y **relaciones termodinámicas**. La comprensión de estas relaciones es fundamental para el análisis de procesos.

#### 4.5.1 Ecuación de Estado

Una **ecuación de estado** es una relación funcional entre las propiedades termodinámicas de una sustancia:

$$f(P, v, T) = 0$$

**Ecuación de estado del gas ideal:**
$$PV = nRT \quad \text{o} \quad Pv = RT$$

Donde:
- $P$: Presión $(Pa)$
- $v$: Volumen específico $(m^3/kg)$
- $R$: Constante específica del gas $(J/kg \cdot K)$
- $T$: Temperatura absoluta $(K)$

**Aplicación en alimentos:** La ecuación del gas ideal es útil para analizar el comportamiento de **gases de combustión** en hornos, **aire** en sistemas de **secado**, y **vapor sobrecalentado** a baja presión.

#### 4.5.2 Relaciones Termodinámicas Fundamentales

Las **propiedades termodinámicas** están interconectadas por relaciones matemáticas específicas:

**Relación densidad-volumen específico:**
$$\rho = \frac{1}{v}$$

**Relación para mezclas bifásicas:**
$$v = v_f + x \cdot v_{fg}$$

Donde:
- $v_f$: Volumen específico del **líquido saturado**
- $v_{fg}$: Diferencia de volumen específico entre **vapor y líquido saturado**
- $x$: **Calidad** o fracción de vapor

### 4.6 Aplicaciones en la Industria Alimentaria

#### 4.6.1 Control de Procesos Térmicos

En la **pasteurización HTST** (High Temperature Short Time) de leche:

- **Estado inicial:** Leche líquida a $T_1 = 4°C$, $P_1 = 1 \text{ atm}$
- **Estado de proceso:** Leche calentada a $T_2 = 72°C$, $P_2 = 1.2 \text{ atm}$
- **Estado final:** Leche pasteurizada a $T_3 = 4°C$, $P_3 = 1 \text{ atm}$

Cada cambio de estado debe controlarse precisamente para garantizar la **eficacia microbiológica** y preservar las **propiedades nutricionales**.

#### 4.6.2 Diseño de Equipos de Refrigeración

En un sistema de **refrigeración** por compresión de vapor:

- **Estado 1:** Refrigerante vapor saturado a baja presión
- **Estado 2:** Refrigerante vapor sobrecalentado a alta presión
- **Estado 3:** Refrigerante líquido saturado a alta presión  
- **Estado 4:** Refrigerante mezcla bifásica a baja presión

El conocimiento preciso de cada **estado termodinámico** permite calcular la **capacidad de refrigeración** y la **eficiencia energética** del sistema.

#### 4.6.3 Optimización de Procesos de Secado

En el **secado por aspersión** de café instantáneo:

- **Aire de entrada:** $T = 180°C$, humedad relativa baja
- **Aire de salida:** $T = 80°C$, humedad relativa alta
- **Producto:** Transición de **solución líquida** a **polvo seco**

El control del **estado termodinámico** del aire permite optimizar la **velocidad de secado** y la **calidad del producto final**.

---

## E) Ejercicios de Reforzamiento

### Ejercicio 1: Identificación de Propiedades
**Enunciado:** Clasifique las siguientes propiedades como intensivas (I) o extensivas (E):

a) Temperatura de un horno industrial
b) Volumen de un tanque de almacenamiento
c) Densidad del aceite de oliva
d) Masa total de azúcar en un silo
e) Presión en una línea de vapor
f) Energía interna de un lote de mermelada

**Respuesta:**
a) Intensiva (I) - La temperatura es independiente de la cantidad de material
b) Extensiva (E) - El volumen depende del tamaño del sistema
c) Intensiva (I) - La densidad es independiente de la cantidad
d) Extensiva (E) - La masa depende de la cantidad de azúcar
e) Intensiva (I) - La presión es independiente de la cantidad de vapor
f) Extensiva (E) - La energía interna depende de la cantidad de mermelada

### Ejercicio 2: Postulado del Estado
**Enunciado:** En un proceso de esterilización, el vapor de agua se encuentra a $T = 115°C$ y $P = 1.7 \text{ bar}$. 

a) ¿Es suficiente esta información para determinar completamente el estado del vapor?
b) ¿Qué otras propiedades quedan automáticamente determinadas?
c) Si el vapor fuera una mezcla bifásica, ¿seguiría siendo válida la información dada?

**Respuesta:**
a) **Sí**, es suficiente. Según el postulado del estado, dos propiedades intensivas independientes (T y P) determinan completamente el estado de una sustancia pura.

b) Quedan determinadas automáticamente:
   - Volumen específico ($v$)
   - Densidad ($\rho$)
   - Entalpía específica ($h$)
   - Entropía específica ($s$)
   - Energía interna específica ($u$)

c) **No**, en la región bifásica, presión y temperatura **no son independientes**. Para una mezcla bifásica se necesitaría conocer la **calidad** (x) además de T o P.

### Ejercicio 3: Ecuación de Estado del Gas Ideal
**Enunciado:** El aire utilizado en un sistema de secado se comporta como gas ideal. Si tiene una temperatura de $T = 80°C$ y una presión de $P = 1.2 \text{ bar}$, calcule:

a) El volumen específico del aire
b) La densidad del aire

**Datos:** $R_{aire} = 287 \text{ J/kg·K}$

**Solución:**
a) Usando la ecuación del gas ideal: $Pv = RT$

Convirtiendo unidades:
- $T = 80°C + 273.15 = 353.15 \text{ K}$
- $P = 1.2 \text{ bar} = 120,000 \text{ Pa}$

$$v = \frac{RT}{P} = \frac{287 \times 353.15}{120,000} = \frac{101,354}{120,000} = 0.845 \text{ m}^3/\text{kg}$$

b) La densidad es el inverso del volumen específico:
$$\rho = \frac{1}{v} = \frac{1}{0.845} = 1.18 \text{ kg/m}^3$$

### Ejercicio 4: Aplicación en Refrigeración
**Enunciado:** En un evaporador de un sistema de refrigeración, el refrigerante R-134a se encuentra como mezcla bifásica a $T = -10°C$. Si el volumen específico de la mezcla es $v = 0.05 \text{ m}^3/\text{kg}$, determine:

a) La presión del refrigerante
b) La calidad de la mezcla

**Datos** (a $T = -10°C$):
- $P_{sat} = 2.01 \text{ bar}$
- $v_f = 0.0008 \text{ m}^3/\text{kg}$ (líquido saturado)
- $v_g = 0.0993 \text{ m}^3/\text{kg}$ (vapor saturado)

**Solución:**
a) En la región bifásica, la **presión es la presión de saturación** a la temperatura dada:
$$P = P_{sat} = 2.01 \text{ bar}$$

b) Para encontrar la calidad, usamos:
$$v = v_f + x(v_g - v_f)$$
$$0.05 = 0.0008 + x(0.0993 - 0.0008)$$
$$0.05 = 0.0008 + x(0.0985)$$
$$x = \frac{0.05 - 0.0008}{0.0985} = \frac{0.0492}{0.0985} = 0.499$$

La **calidad** de la mezcla es $x = 49.9\%$

---

## F) Conclusión

El **estado termodinámico** representa un concepto fundamental en el análisis de sistemas térmicos aplicados a la industria alimentaria. La comprensión profunda de este concepto permite a los ingenieros en alimentos:

1. **Caracterizar completamente** las condiciones de operación en procesos térmicos
2. **Predecir el comportamiento** de las sustancias bajo diferentes condiciones
3. **Optimizar procesos** como pasteurización, esterilización, secado y refrigeración
4. **Diseñar equipos** más eficientes y seguros

El **postulado del estado** simplifica significativamente el análisis termodinámico al establecer que solo **dos propiedades independientes** son necesarias para determinar completamente el estado de una sustancia pura. Esta simplicidad conceptual contrasta con la complejidad de los fenómenos físicos involucrados.

Las **relaciones entre variables termodinámicas** proporcionan las herramientas matemáticas necesarias para el análisis cuantitativo de procesos. La correcta aplicación de **ecuaciones de estado** y **relaciones termodinámicas** permite realizar cálculos precisos para el diseño y operación de equipos industriales.

En el contexto de la **ingeniería de alimentos**, el dominio de estos conceptos es esencial para garantizar la **calidad**, **seguridad** y **eficiencia energética** de los procesos de transformación y conservación de alimentos. La aplicación sistemática de los principios del estado termodinámico contribuye al desarrollo de tecnologías alimentarias más sostenibles y eficientes.

---

## G) Bibliografía

Çengel, Y. A., & Boles, M. A. (2019). *Termodinámica* (8ª ed.). McGraw-Hill Interamericana. 

Himmelblau, D. M., & Riggs, J. B. (2012). *Principios básicos y cálculos en ingeniería química* (8ª ed.). Pearson Educación.

Moran, M. J., Shapiro, H. N., Boettner, D. D., & Bailey, M. B. (2018). *Fundamentals of engineering thermodynamics* (9ª ed.). John Wiley & Sons.

Singh, R. P., & Heldman, D. R. (2014). *Introduction to food engineering* (5ª ed.). Academic Press.

Smith, J. M., Van Ness, H. C., Abbott, M. M., & Swihart, M. T. (2017). *Introduction to chemical engineering thermodynamics* (8ª ed.). McGraw-Hill Education.

Toledo, R. T., Singh, R. K., & Kong, F. (2018). *Fundamentals of food process engineering* (4ª ed.). Springer.

Wankat, P. C. (2016). *Separation process engineering: Includes mass transfer analysis* (4ª ed.). Pearson Education.
