# Actividad de Desarrollo (AD): Ciclos Termodinámicos de Potencia

## AD.04.01.01 - Lectura: Ciclos Termodinámicos Fundamentales

### Contenido

1. Introducción
2. Desarrollo
   - 2.1 Fundamentos de los ciclos de potencia
   - 2.2 El ciclo de Carnot: el límite teórico de eficiencia
   - 2.3 El ciclo de Otto: motores de encendido por chispa
   - 2.4 El ciclo Diesel: motores de encendido por compresión
   - 2.5 Comparación de ciclos y parámetros de rendimiento
3. Ejercicios de reforzamiento
4. Conclusión
5. Bibliografía

---

## 1. Introducción

Los **ciclos termodinámicos de potencia** constituyen la base fundamental para comprender el funcionamiento de las **máquinas térmicas** que convierten **energía térmica** en **trabajo mecánico**. Estos ciclos son secuencias ordenadas de **procesos termodinámicos** que el **fluido de trabajo** experimenta de manera cíclica para generar trabajo útil.

En el contexto de la **ingeniería automotriz**, el estudio de estos ciclos es esencial para el **diseño**, **análisis** y **optimización** de **motores de combustión interna**. Los **ciclos ideales** nos proporcionan **modelos teóricos** que, aunque no son perfectamente realizables en la práctica, nos permiten establecer **límites de rendimiento** y comprender los **principios físicos** que gobiernan el funcionamiento de los motores reales.

Según Çengel y Boles (2015), las **máquinas térmicas** se diseñan con el propósito de convertir **energía térmica** en trabajo, y su desempeño se expresa en términos de la **eficiencia térmica** (ηₜₑᵣ), que representa la relación entre el **trabajo neto producido** y la **entrada total de calor**.

En esta lectura estudiaremos los **ciclos fundamentales**: **Carnot**, **Otto** y **Diesel**, analizando sus características, aplicaciones y limitaciones para proporcionar una base sólida en el análisis de **sistemas de potencia automotrices**.

---

## 2. Desarrollo

### 2.1 Fundamentos de los ciclos de potencia

Las **máquinas térmicas** son dispositivos cíclicos donde el **fluido de trabajo** regresa a su estado inicial al final de cada ciclo. Durante una parte del ciclo, el fluido realiza trabajo, y durante otra, se hace trabajo sobre el fluido. La diferencia entre estos dos trabajos constituye el **trabajo neto** que entrega la máquina térmica (Moran et al., 2018).

La **eficiencia térmica** de cualquier máquina térmica se define como:

$$\eta_{tér} = \frac{W_{neto}}{Q_{entrada}} \quad \text{o} \quad \eta_{tér} = \frac{w_{neto}}{q_{entrada}}$$

Donde:
- **W_{neto}**: Trabajo neto producido por ciclo (kJ)
- **Q_{entrada}**: Calor total suministrado por ciclo (kJ)
- **w_{neto}**, **q_{entrada}**: Valores específicos por unidad de masa (kJ/kg)

#### **Idealizaciones para ciclos de potencia**

Para el análisis de **ciclos de potencia ideales**, se emplean las siguientes **simplificaciones**:

1. **Ausencia de fricción**: El fluido de trabajo no experimenta caídas de presión cuando fluye por tuberías o intercambiadores de calor.
2. **Procesos de cuasiequilibrio**: Todos los procesos de expansión y compresión ocurren de manera **cuasiestática**.
3. **Sistemas adiabáticos**: Las tuberías que conectan los componentes están perfectamente aisladas.
4. **Desprecio de energías cinética y potencial**: Los cambios en estas energías son insignificantes comparados con los términos de trabajo y calor.

#### **Diagramas termodinámicos**

En los **diagramas P-v** y **T-s**, el **área encerrada** por las curvas del proceso representa el **trabajo neto producido** durante el ciclo, que también equivale a la **transferencia neta de calor**. El **diagrama T-s** es particularmente útil, ya que:

- El **área bajo la curva** del proceso representa la **transferencia de calor** para ese proceso específico.
- Un **proceso de adición de calor** avanza en dirección de **entropía creciente**.
- Un **proceso de rechazo de calor** avanza en dirección de **entropía decreciente**.
- Un **proceso isentrópico** (adiabático reversible) avanza a **entropía constante**.

![Diagramas P-v y T-s genéricos](../../../Apuntes/Pasted%20image%2020250803091726.png)
**FIGURA 1: Diagramas P-v y T-s genéricos**
*Los diagramas muestran un ciclo termodinámico genérico donde el área encerrada representa el trabajo neto producido.*

### 2.2 El ciclo de Carnot: el límite teórico de eficiencia

El **ciclo de Carnot**, propuesto en 1824 por el ingeniero francés **Sadi Carnot**, representa el **ciclo termodinámico ideal** más eficiente posible entre dos **reservorios térmicos** a temperaturas constantes. Este ciclo establece el **límite teórico superior** de eficiencia para cualquier **máquina térmica** que opere entre las mismas temperaturas, constituyendo el **estándar de referencia** contra el cual se comparan todos los ciclos reales (Çengel & Boles, 2015).

La **máquina térmica de Carnot** es completamente **reversible**, lo que significa que todos sus procesos pueden invertirse sin dejar rastro en los alrededores. Esta característica la convierte en la máquina térmica más eficiente teóricamente posible.

#### **Procesos del ciclo de Carnot**

El **ciclo de Carnot** consta de cuatro **procesos reversibles**:

##### **Proceso 1-2: Expansión Isotérmica Reversible**
El **fluido de trabajo** se encuentra inicialmente a temperatura **T_H** en contacto con una **fuente térmica** de alta temperatura. El gas se expande lentamente realizando **trabajo** sobre los alrededores mientras mantiene su temperatura constante. La **transferencia de calor** ocurre de manera **reversible** debido a que la diferencia de temperatura entre el gas y la fuente nunca excede una cantidad infinitesimal.

**Ecuación del calor absorbido:**
$$Q_H = T_H \Delta S_{12}$$

##### **Proceso 2-3: Expansión Adiabática Reversible**
Se elimina la fuente térmica y se aísla el sistema. El fluido continúa expandiéndose sin **intercambio de calor** (**proceso adiabático**), realizando trabajo mientras su temperatura disminuye de **T_H** a **T_L**. Al ser un **proceso de cuasiequilibrio** sin fricción, es completamente **reversible**.

**Relación temperatura-volumen:**
$$T_2 V_2^{\gamma-1} = T_3 V_3^{\gamma-1}$$

##### **Proceso 3-4: Compresión Isotérmica Reversible**
El sistema se pone en contacto con un **sumidero térmico** a temperatura **T_L**. Una fuerza externa comprime el gas mientras este **cede calor** al sumidero, manteniendo su temperatura constante en **T_L**. La **transferencia de calor** es **reversible** por las mismas razones del proceso 1-2.

**Ecuación del calor cedido:**
$$Q_L = T_L \Delta S_{34}$$

##### **Proceso 4-1: Compresión Adiabática Reversible**
Se retira el sumidero térmico y se aísla nuevamente el sistema. El gas se comprime **adiabáticamente** hasta retornar a su estado inicial, aumentando su temperatura de **T_L** a **T_H**.

**Relación temperatura-volumen:**
$$T_4 V_4^{\gamma-1} = T_1 V_1^{\gamma-1}$$

#### **Eficiencia del Ciclo de Carnot**

La **eficiencia térmica** de cualquier máquina térmica se define como:

$$\eta_{tér} = \frac{W_{neto}}{Q_{entrada}} = 1 - \frac{Q_L}{Q_H}$$

Para **máquinas térmicas reversibles**, la relación de transferencias de calor puede reemplazarse por la relación de **temperaturas absolutas**:

$$\left(\frac{Q_H}{Q_L}\right)_{rev} = \frac{T_H}{T_L}$$

Por lo tanto, la **eficiencia del ciclo de Carnot** se expresa como:

$$\eta_{Carnot} = \eta_{tér,rev} = 1 - \frac{T_L}{T_H}$$

Donde:
- **T_L**: Temperatura absoluta del **sumidero térmico** (K)
- **T_H**: Temperatura absoluta de la **fuente térmica** (K)

Esta ecuación representa la **máxima eficiencia teórica** para cualquier máquina térmica operando entre los mismos límites de temperatura.

![[Pasted image 20250803092250.png]]

**FIGURA 2: Ciclo de Carnot en diagramas P-v y T-s**
*El diagrama P-v muestra los cuatro procesos del ciclo de Carnot con transferencias de calor, mientras que el diagrama T-s rectangular ilustra claramente los procesos isotérmicos (horizontales) e isentrópicos (verticales).*

#### **Principios de Carnot**

Los **principios de Carnot** establecen dos conclusiones fundamentales:

1. **La eficiencia de una máquina térmica irreversible es siempre menor que la eficiencia de una máquina reversible** que opera entre los mismos reservorios.
2. **Las eficiencias de todas las máquinas térmicas reversibles** que operan entre los mismos reservorios son **idénticas**.

Estos principios pueden expresarse matemáticamente como:

$$\eta_{tér} \begin{cases}
< \eta_{tér,rev} & \text{(máquina irreversible)} \\
= \eta_{tér,rev} & \text{(máquina reversible)} \\
> \eta_{tér,rev} & \text{(máquina imposible)}
\end{cases}$$

#### **Valor práctico del ciclo de Carnot**

Aunque el **ciclo de Carnot** no es realizable prácticamente debido a que los **procesos isotérmicos reversibles** requieren transferencias de calor infinitamente lentas, su verdadero valor reside en:

1. **Establecer el límite teórico** de eficiencia
2. **Proporcionar una referencia** para evaluar ciclos reales
3. **Demostrar** que la eficiencia aumenta con el incremento en **T_H** o la disminución en **T_L**

### 2.3 El ciclo de Otto: motores de encendido por chispa

El **ciclo de Otto**, nombrado en honor a **Nikolaus A. Otto** quien construyó exitosamente una máquina de cuatro tiempos en 1876, constituye el **modelo termodinámico ideal** para los **motores de encendido por chispa** (motores de gasolina). Este ciclo representa una **versión idealizada** del funcionamiento real de los **motores de combustión interna** de cuatro tiempos.

#### **Funcionamiento del motor de cuatro tiempos**

En los **motores reales**, el pistón ejecuta cuatro carreras completas (dos ciclos mecánicos) dentro del cilindro, mientras el cigüeñal completa dos revoluciones por cada **ciclo termodinámico**. Las cuatro carreras son:

1. **Carrera de admisión**: Entrada de la mezcla aire-combustible
2. **Carrera de compresión**: Compresión de la mezcla
3. **Carrera de potencia**: Combustión y expansión de gases
4. **Carrera de escape**: Expulsión de gases de combustión

![Motor de cuatro tiempos y ciclos Otto](../../../Apuntes/Pasted%20image%2020250803092813.png)
**FIGURA 3: Motor de cuatro tiempos y ciclos Otto real e ideal**
*La figura superior muestra el diagrama P-V real de un motor de cuatro tiempos con las cuatro carreras del pistón. La figura inferior presenta el ciclo Otto ideal con sus cuatro procesos termodinámicos y la representación esquemática de cada etapa.*

#### **Procesos del ciclo de Otto ideal**

El **ciclo de Otto ideal** se compone de cuatro **procesos internamente reversibles**:

##### **Proceso 1-2: Compresión Isentrópica**
La mezcla **aire-combustible** se comprime **adiabáticamente** desde el **punto muerto inferior** (**PMI**) hasta el **punto muerto superior** (**PMS**). Durante este proceso, tanto la **temperatura** como la **presión** aumentan significativamente sin intercambio de calor con los alrededores.

**Relación de compresión:**
$$r = \frac{V_1}{V_2} = \frac{V_{máx}}{V_{mín}}$$

Para un **proceso isentrópico** (adiabático reversible) en un **gas ideal**, las relaciones entre propiedades están gobernadas por el **índice adiabático** o **relación de calores específicos** (**γ**):

$$\gamma = \frac{c_p}{c_v}$$

Donde:
- **c_p**: Calor específico a **presión constante** (kJ/kg·K)
- **c_v**: Calor específico a **volumen constante** (kJ/kg·K)
- **γ ≈ 1.4** para aire a temperatura ambiente

**Relaciones isentrópicas:**
$$\frac{T_2}{T_1} = \left(\frac{V_1}{V_2}\right)^{\gamma-1} = r^{\gamma-1}$$
$$\frac{P_2}{P_1} = \left(\frac{V_1}{V_2}\right)^{\gamma} = r^{\gamma}$$

##### **Proceso 2-3: Adición de Calor a Volumen Constante**
Este proceso simula la **combustión instantánea** de la mezcla. Se añade calor (**Q_H**) al sistema manteniendo el **volumen constante**, lo que produce un aumento drástico de **presión** y **temperatura**. En la realidad, esto corresponde al momento de la **ignición por chispa**.

**Calor añadido:**
$$Q_H = m c_v (T_3 - T_2)$$

**A volumen constante:**
$$\frac{P_3}{P_2} = \frac{T_3}{T_2}$$

##### **Proceso 3-4: Expansión Isentrópica**
Los **gases calientes** a alta presión se expanden **adiabáticamente**, empujando el pistón desde el **PMS** hacia el **PMI**. Este es el **proceso de potencia** donde se genera el **trabajo útil** del motor. Durante la expansión, tanto la **temperatura** como la **presión** disminuyen.

**Relaciones isentrópicas:**
$$\frac{T_4}{T_3} = \left(\frac{V_3}{V_4}\right)^{\gamma-1} = \left(\frac{1}{r}\right)^{\gamma-1}$$
$$\frac{P_4}{P_3} = \left(\frac{V_3}{V_4}\right)^{\gamma} = \left(\frac{1}{r}\right)^{\gamma}$$

##### **Proceso 4-1: Rechazo de Calor a Volumen Constante**
Este proceso simula la **expulsión de gases de escape** y el **enfriamiento** del cilindro. Se rechaza calor (**Q_L**) hacia el ambiente a **volumen constante**, representando la caída instantánea de presión cuando se abren las válvulas de escape.

**Calor rechazado:**
$$Q_L = m c_v (T_4 - T_1)$$

![Ciclo de Otto en diagrama T-s](../../../Apuntes/Pasted%20image%2020250803093844.png)
**FIGURA 4: Ciclo de Otto ideal en diagrama T-s**
*El diagrama T-s del ciclo Otto muestra claramente los procesos isocóricos (líneas verticales) para la adición y rechazo de calor, y los procesos isentrópicos (líneas horizontales) para la compresión y expansión.*

#### **Eficiencia del Ciclo de Otto**

Para un **sistema cerrado** bajo las **suposiciones de aire estándar frío**, la **eficiencia térmica** del ciclo de Otto se deriva del **balance de energía**:

$$\eta_{Otto} = \frac{W_{neto}}{Q_H} = 1 - \frac{Q_L}{Q_H}$$

Aplicando las **relaciones isentrópicas** y las propiedades de los procesos isocóricos:

$$\frac{Q_L}{Q_H} = \frac{m c_v (T_4 - T_1)}{m c_v (T_3 - T_2)} = \frac{T_4 - T_1}{T_3 - T_2}$$

Utilizando las relaciones de temperatura para procesos isentrópicos y considerando que **v₂ = v₃** y **v₄ = v₁**, se obtiene:

$$\eta_{Otto} = 1 - \frac{1}{r^{\gamma-1}}$$

Donde:
- **r**: **Relación de compresión** (V₁/V₂)
- **γ**: **Relación de calores específicos** (cₚ/cᵥ ≈ 1.4 para aire)

#### **Factores que Afectan la Eficiencia**

##### **1. Relación de Compresión (r)**

La eficiencia **aumenta** con la **relación de compresión**. Sin embargo, existe un **límite práctico** debido al fenómeno de **autoignición** o **detonación** (engine knock). Cuando la **relación de compresión** es muy alta, la temperatura de la mezcla puede exceder la **temperatura de autoignición** del combustible, causando:

- **Combustión prematura** e incontrolada
- **Ruido audible** (cascabeleo del motor)
- **Daños potenciales** al motor
- **Pérdida de eficiencia** y potencia

Las **relaciones de compresión típicas** para motores de gasolina varían entre **8:1 y 12:1**.

##### **2. Relación de Calores Específicos (γ)**

Para una **relación de compresión dada**, la eficiencia aumenta con **γ**. Los **gases monoatómicos** (como argón o helio, γ ≈ 1.667) proporcionan mayor eficiencia que los **gases poliatómicos**. En motores reales:

- **Aire**: γ ≈ 1.4
- **CO₂**: γ ≈ 1.3  
- **Productos de combustión**: γ < 1.4

Esto explica parcialmente por qué los **motores reales** tienen **eficiencias menores** que el ciclo ideal.

![Eficiencia del ciclo Otto vs relación de compresión](../../../Apuntes/Pasted%20image%2020250803100148.png)
**FIGURA 5: Eficiencia del ciclo Otto vs relación de compresión**
*La gráfica muestra cómo la eficiencia térmica del ciclo Otto aumenta con la relación de compresión, pero se nivela a valores altos. La zona sombreada indica las relaciones de compresión típicas para motores de gasolina (8:1 a 12:1) limitadas por la detonación.*

##### **3. Efectos de la Temperatura**

La **eficiencia real** disminuye con el aumento de temperatura debido a:
- **Disociación** de productos de combustión
- **Variación** de calores específicos con la temperatura
- **Transferencia de calor** hacia las paredes del cilindro

### 2.4 El ciclo Diesel: motores de encendido por compresión

El **ciclo Diesel**, también conocido como **ciclo de presión constante**, representa el **modelo termodinámico ideal** para los **motores de encendido por compresión**. La diferencia fundamental con el **ciclo de Otto** radica en que la **adición de calor** (proceso de combustión) ocurre a **presión constante** en lugar de **volumen constante**.

En los **motores diésel reales**, el **combustible** se inyecta directamente en el **aire comprimido** a alta temperatura, produciendo **autoignición** sin necesidad de **sistema de encendido** externo. Este proceso de **combustión controlada** se aproxima mejor mediante un **proceso isobárico** (presión constante).

**[FIGURA 6: Sistema de inyección diésel y autoignición]**
*Descripción:* Diagrama esquemático de un motor diésel mostrando el sistema de inyección directa de combustible, la cámara de combustión con aire comprimido caliente, el proceso de autoignición y la formación del frente de llama. Incluir temperaturas típicas (500-700°C) y presiones de inyección (200-2000 bar) para contextualizar el proceso físico.

#### **Procesos del ciclo Diesel ideal**

El **ciclo Diesel ideal** consta de cuatro procesos:

##### **Proceso 1-2: Compresión Isentrópica**
El **aire** (sin combustible) se comprime **adiabáticamente** desde el **PMI** hasta el **PMS**. Las **relaciones de compresión** en motores diésel son **significativamente mayores** que en motores Otto (típicamente **14:1 a 25:1**), lo que permite alcanzar **temperaturas** suficientes para la **autoignición** del combustible (≈ 500-700°C).

**Relaciones isentrópicas:**
$$\frac{T_2}{T_1} = r^{\gamma-1}, \quad \frac{P_2}{P_1} = r^{\gamma}$$

##### **Proceso 2-3: Adición de Calor a Presión Constante**
Este proceso simula la **inyección y combustión** del combustible. Se añade calor (**Q_H**) al sistema manteniendo la **presión constante** mientras el **volumen aumenta**. La **duración controlada** de este proceso permite una **combustión más gradual** comparada con el ciclo Otto.

**Calor añadido:**
$$Q_H = m c_p (T_3 - T_2)$$

**Relación de corte:**
$$r_c = \frac{V_3}{V_2}$$

**A presión constante:**
$$\frac{T_3}{T_2} = \frac{V_3}{V_2} = r_c$$

##### **Proceso 3-4: Expansión Isentrópica**
Los **gases de combustión** se expanden **adiabáticamente**, generando el **trabajo de potencia**. La **expansión** continúa hasta que el pistón alcanza el **PMI**.

**Relación isentrópica:**
$$\frac{T_4}{T_3} = \left(\frac{V_3}{V_4}\right)^{\gamma-1}$$

##### **Proceso 4-1: Rechazo de Calor a Volumen Constante**
Simula la **expulsión** de gases de escape y **enfriamiento** del cilindro. El calor (**Q_L**) se rechaza a **volumen constante**.

**Calor rechazado:**
$$Q_L = m c_v (T_4 - T_1)$$

**[FIGURA 7: Ciclo Diesel ideal en diagramas P-v y T-s]**
![[Pasted image 20250803164159.png]]
![[Pasted image 20250803164237.png]]
*Descripción:* Dos diagramas del ciclo Diesel ideal: (a) Diagrama P-v mostrando los cuatro procesos (1-2 compresión isentrópica, 2-3 adición de calor isobárica, 3-4 expansión isentrópica, 4-1 rechazo de calor isocórico) con las relaciones r (compresión) y r_c (corte) claramente marcadas; (b) Diagrama T-s correspondiente mostrando la diferencia clave con el ciclo Otto en el proceso de adición de calor a presión constante.

#### **Eficiencia del Ciclo Diesel**

La **eficiencia térmica** del **ciclo Diesel** bajo **suposiciones de aire estándar frío** se expresa como:

$$\eta_{Diesel} = 1 - \frac{1}{r^{\gamma-1}} \left[ \frac{r_c^{\gamma} - 1}{\gamma (r_c - 1)} \right]$$

Donde:
- **r**: **Relación de compresión** (V₁/V₂)
- **r_c**: **Relación de corte** (V₃/V₂)
- **γ**: **Relación de calores específicos**

#### **Características del Ciclo Diesel**

##### **Ventajas:**
- **Mayor eficiencia térmica** debido a altas relaciones de compresión
- **Menor consumo de combustible** por unidad de trabajo
- **Combustible menos refinado** (menor costo)
- **Mayor durabilidad** del motor
- **Mayor torque** a bajas revoluciones

##### **Desventajas:**
- **Mayor peso** y **costo inicial** del motor
- **Mayores emisiones** de NOₓ y partículas
- **Mayor ruido** y **vibración**
- **Menor potencia específica** (potencia/peso)
- **Arranque más difícil** en frío

### 2.5 Comparación de ciclos y parámetros de rendimiento

La **comparación** entre los **ciclos termodinámicos ideales** nos permite comprender las **diferencias fundamentales** en el **diseño**, **operación** y **rendimiento** de los diferentes tipos de **motores de combustión interna**.

#### **Tabla Comparativa de Ciclos**

| **Característica** | **Ciclo de Otto** | **Ciclo Diesel** | **Ciclo de Carnot** |
|:---|:---|:---|:---|
| **Tipo de Motor** | Encendido por chispa | Encendido por compresión | Teórico ideal |
| **Combustible** | Gasolina, GLP | Diésel, biodiésel | Cualquier fluido |
| **Ignición** | Bujía de encendido | Autoignición | N/A |
| **Adición de Calor** | Volumen constante | Presión constante | Temperatura constante |
| **Relación de Compresión** | 8:1 a 12:1 | 14:1 a 25:1 | Variable |
| **Eficiencia Típica** | 25-30% | 35-45% | η = 1 - T_L/T_H |
| **Aplicaciones** | Automóviles, motocicletas | Camiones, barcos, generadores | Referencia teórica |
| **Ventajas** | Menor peso, menor ruido | Mayor eficiencia, menor consumo | Máxima eficiencia teórica |
| **Desventajas** | Menor eficiencia | Mayor peso, más ruido | Irrealizable prácticamente |

**[FIGURA 8: Comparación de ciclos Otto, Diesel y Carnot]**
*Descripción:* Diagrama P-v que superponga los tres ciclos ideales operando entre los mismos límites de volumen y con condiciones similares. Mostrar claramente las diferencias en los procesos de adición de calor (isocórico para Otto, isobárico para Diesel, isotérmico para Carnot) y las áreas encerradas que representan el trabajo neto de cada ciclo. Incluir una tabla pequeña con las eficiencias típicas de cada ciclo.

#### **Comparación Otto vs Diesel**

Para la misma **relación de compresión**, el **ciclo Otto** es **más eficiente** que el **ciclo Diesel**. Sin embargo, los **motores diésel** operan con **relaciones de compresión mucho mayores**, lo que les permite alcanzar **eficiencias superiores** en la práctica.

**Análisis matemático:**
- Para **r = 18** y **r_c = 2** (Diesel): η ≈ 63%
- Para **r = 18** (Otto): η ≈ 69%
- Para **r = 9** (Otto típico): η ≈ 58%

#### **Parámetros de Rendimiento en Motores**

##### **1. Potencia (P)**

Representa la **tasa** de realización de **trabajo**:

$$P = \frac{W_{neto}}{\Delta t}$$

##### **2. Cilindrada (V_d)**

**Volumen total** desplazado por todos los pistones:

$$V_d = \frac{\pi D^2}{4} L \times N_{cilindros}$$

Donde:
- **D**: Diámetro del cilindro (bore)
- **L**: Carrera del pistón (stroke)

##### **3. Presión Media Efectiva (PME)**

Presión **constante hipotética** que produciría el mismo **trabajo neto**:

$$PME = \frac{W_{neto}}{V_{desplazado}}$$

##### **4. Eficiencias del Motor**

- **Eficiencia Térmica**: η_tér = W_neto/Q_entrada
- **Eficiencia Mecánica**: η_mec = W_eje/W_indicado  
- **Eficiencia Volumétrica**: η_vol = V_aire_real/V_teórico
- **Eficiencia Global**: η_global = η_tér × η_mec × η_vol

**[FIGURA 9: Parámetros de rendimiento del motor]**
*Descripción:* Diagrama conceptual que muestre las diferentes eficiencias de un motor real: (a) Flujo de energía desde el combustible hasta la potencia útil en el eje, mostrando las pérdidas en cada etapa; (b) Gráfica de barras comparando las eficiencias típicas (térmica ~30%, mecánica ~85%, volumétrica ~80%, global ~20%) para un motor Otto; (c) Definición gráfica de PME mostrando cómo una presión constante equivalente produciría el mismo trabajo que el ciclo completo.

---

## 3. Ejercicios de Reforzamiento

### **Ejercicio 1: Ciclo de Carnot**

**Problema:** Una máquina térmica de Carnot opera entre una fuente térmica a 800 K y un sumidero a 300 K. Si recibe 1000 kJ de calor por ciclo, determine:
a) La eficiencia térmica del ciclo
b) El trabajo neto producido por ciclo  
c) El calor rechazado al sumidero

**Solución:**

a) **Eficiencia térmica:**
$$\eta_{Carnot} = 1 - \frac{T_L}{T_H} = 1 - \frac{300\text{ K}}{800\text{ K}} = 0.625 = 62.5\%$$

b) **Trabajo neto:**
$$W_{neto} = \eta_{Carnot} \times Q_H = 0.625 \times 1000\text{ kJ} = 625\text{ kJ}$$

c) **Calor rechazado:**
$$Q_L = Q_H - W_{neto} = 1000\text{ kJ} - 625\text{ kJ} = 375\text{ kJ}$$

### **Ejercicio 2: Ciclo de Otto**

**Problema:** Un motor que opera según el ciclo de Otto tiene una relación de compresión de 10:1. Si γ = 1.4, determine:
a) La eficiencia térmica ideal del ciclo
b) Compare con un motor de relación de compresión 8:1

**Solución:**

a) **Para r = 10:**
$$\eta_{Otto} = 1 - \frac{1}{r^{\gamma-1}} = 1 - \frac{1}{10^{1.4-1}} = 1 - \frac{1}{10^{0.4}} = 1 - 0.398 = 60.2\%$$

b) **Para r = 8:**
$$\eta_{Otto} = 1 - \frac{1}{8^{0.4}} = 1 - 0.435 = 56.5\%$$

**Conclusión:** El aumento de la relación de compresión de 8:1 a 10:1 mejora la eficiencia en 3.7 puntos porcentuales.

### **Ejercicio 3: Comparación Otto vs Diesel**

**Problema:** Compare la eficiencia de un ciclo Otto (r = 9) con un ciclo Diesel (r = 18, r_c = 2) para γ = 1.4.

**Solución:**

**Ciclo Otto:**
$$\eta_{Otto} = 1 - \frac{1}{9^{0.4}} = 1 - 0.426 = 57.4\%$$

**Ciclo Diesel:**
$$\eta_{Diesel} = 1 - \frac{1}{18^{0.4}} \left[ \frac{2^{1.4} - 1}{1.4(2-1)} \right] = 1 - 0.315 \times 1.171 = 63.1\%$$

**Conclusión:** El ciclo Diesel muestra mayor eficiencia debido a su mayor relación de compresión.

### **Ejercicio 4: Análisis de PME**

**Problema:** Un motor de 2.0 L de cilindrada produce 150 kW de potencia a 6000 RPM. Determine la presión media efectiva.

**Solución:**

**Trabajo por ciclo:**
$$W_{ciclo} = \frac{P \times 60 \times 2}{N \times n_{cil}} = \frac{150,000 \text{ W} \times 60 \times 2}{6000 \times 4} = 750 \text{ J}$$

**PME:**
$$PME = \frac{W_{ciclo}}{V_d} = \frac{750 \text{ J}}{0.002 \text{ m}^3} = 375,000 \text{ Pa} = 375 \text{ kPa}$$

### **Ejercicio 5: Mejora de eficiencia**

**Problema:** Un motor Otto con r = 8 opera entre 300 K y 2000 K. Compare su eficiencia con:
a) El límite teórico de Carnot
b) Un motor Otto con r = 12

**Solución:**

a) **Límite de Carnot:**
$$\eta_{Carnot} = 1 - \frac{300}{2000} = 0.85 = 85\%$$

**Otto r = 8:**
$$\eta_{Otto} = 1 - \frac{1}{8^{0.4}} = 56.5\%$$

b) **Otto r = 12:**
$$\eta_{Otto} = 1 - \frac{1}{12^{0.4}} = 63.0\%$$

**Conclusión:** Existe un potencial significativo de mejora (28.5 puntos porcentuales) respecto al límite de Carnot.

**[FIGURA 10: Gráficas de los ejercicios resueltos]**
*Descripción:* Conjunto de gráficas que ilustren los resultados de los ejercicios: (a) Diagrama de barras mostrando la distribución de energía en el ciclo de Carnot del Ejercicio 1 (Q_H, W_neto, Q_L); (b) Curva de eficiencia vs relación de compresión del Ejercicio 2 marcando los puntos r=8 y r=10; (c) Comparación de eficiencias Otto vs Diesel del Ejercicio 3 en diagrama de barras; (d) Diagrama PME del Ejercicio 4 mostrando el área equivalente en el diagrama P-V.

---

## 4. Conclusión

Los **ciclos termodinámicos de potencia** estudiados constituyen la **base teórica fundamental** para comprender el funcionamiento de las **máquinas térmicas** utilizadas en **aplicaciones automotrices**. Aunque representan **idealizaciones** de los procesos reales, proporcionan **herramientas analíticas** esenciales para:

1. **Establecer límites teóricos** de rendimiento y eficiencia
2. **Analizar** el comportamiento de **motores reales**
3. **Identificar oportunidades** de mejora en el diseño
4. **Comparar** diferentes **tecnologías** de motores

El **ciclo de Carnot** establece el **límite teórico superior** de eficiencia, sirviendo como **referencia** para evaluar el potencial de mejora de los ciclos reales. Los **ciclos de Otto y Diesel** representan los **fundamentos** de los motores de **encendido por chispa** y **encendido por compresión**, respectivamente.

La **comprensión profunda** de estos conceptos es **crucial** para el **ingeniero automotriz** moderno, especialmente en el contexto actual de **transición energética** y **búsqueda de mayor eficiencia** en los **sistemas de propulsión vehicular**.

Los **principios termodinámicos** aquí estudiados también son aplicables al **análisis** de **tecnologías emergentes** como **motores híbridos**, **celdas de combustible** y **sistemas de recuperación de energía**, consolidando su relevancia en el **futuro** de la **ingeniería automotriz**.

Las **diferencias clave** entre los ciclos estudiados pueden resumirse en:

- **Carnot**: Máxima eficiencia teórica, irrealizable prácticamente
- **Otto**: Ideal para aplicaciones de alta velocidad y bajo peso
- **Diesel**: Superior para aplicaciones de alta eficiencia y torque

El **análisis comparativo** demuestra que, aunque los **motores reales** operan con eficiencias significativamente menores que los **ciclos ideales**, el estudio de estos últimos proporciona **directrices claras** para la **mejora continua** del **rendimiento energético** en la **industria automotriz**.

---

## 5. Bibliografía

Çengel, Y. A., & Boles, M. A. (2015). *Termodinámica* (8ª ed.). McGraw-Hill Education.

Moran, M. J., Shapiro, H. N., Boettner, D. D., & Bailey, M. B. (2018). *Fundamentals of engineering thermodynamics* (9th ed.). John Wiley & Sons.

Payri, F., & Desantes, J. M. (Coords.). (2011). *Motores de combustión interna alternativos*. Editorial de la Universidad Politécnica de Valencia.

Heywood, J. B. (2018). *Internal combustion engine fundamentals* (2nd ed.). McGraw-Hill Education.

Ferguson, C. R., & Kirkpatrick, A. T. (2016). *Internal combustion engines: Applied thermosciences* (3rd ed.). John Wiley & Sons.

Brunetti, F. (2012). *Motores de combustión interna* (2ª ed.). Editorial Dossat.

Pulkrabek, W. W. (2014). *Engineering fundamentals of the internal combustion engine* (2nd ed.). Pearson.

Stone, R. (2012). *Introduction to internal combustion engines* (4th ed.). Palgrave Macmillan.

Turns, S. R. (2012). *Thermal-fluid sciences: An integrated approach*. Cambridge University Press.

Borman, G. L., & Ragland, K. W. (1998). *Combustion engineering*. McGraw-Hill Education.