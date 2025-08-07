
---

## La Primera Ley de la Termodinámica: Un Concepto Fundamental de la Energía

### Introducción

La Termodinámica es la ciencia que estudia la **transformación de la energía** y las propiedades de las sustancias involucradas en dichos procesos. Uno de los pilares más importantes de esta disciplina es la **Primera Ley de la Termodinámica**, también conocida como el **Principio de Conservación de la Energía**. Este principio fundamental establece que **la energía no se crea ni se destruye durante un proceso; solo se transforma o cambia de forma**.

La energía se manifiesta de diversas maneras en nuestra vida cotidiana, y su comprensión es crucial para la ingeniería. Desde motores de combustión interna y sistemas de refrigeración, hasta plantas generadoras de vapor, la termodinámica permite calcular la cantidad de aire y combustible necesarios, los requisitos de enfriamiento, la potencia suministrada y el calor disipado, entre otras cosas.

Para aplicar este axioma de manera útil, es esencial identificar las diferentes formas de energía para poder cuantificarlas y realizar balances energéticos. La energía puede existir en varias formas: **térmica, mecánica, cinética, potencial, eléctrica, magnética, química y nuclear**. La suma de todas estas formas constituye la **energía total (E)** de un sistema.

### 1. La Primera Ley de la Termodinámica para Sistemas Cerrados

Un **sistema cerrado** es aquel que **no intercambia masa con sus alrededores**. Para estos sistemas, la energía puede cruzar la frontera de dos formas distintas: como **calor (Q)** o como **trabajo (W)**.

#### 1.1 Explicación de la Ecuación de la Primera Ley

La Primera Ley de la Termodinámica se puede expresar de varias maneras, dependiendo de si se analiza un ciclo o un proceso.

- **Para un ciclo termodinámico:** Cuando un sistema cerrado opera en un ciclo, regresa a su estado inicial. En este caso, la ley establece que **el calor neto agregado a un sistema es igual en magnitud al trabajo neto desarrollado por este**. Matemáticamente, esto se expresa como: **∮ dQ = ∮ dW** (La notación ∮ denota la integral alrededor de un ciclo completo). Esto implica que para un ciclo, el cambio de energía total del sistema es cero (ΔE_sistema = 0).

![[Digrama _PV_Proceso.png]]
     Figura 4.1 de "Thermodynamics Demystified - Merle C. Potter_cap4.pdf,mostrando un ciclo en un diagrama P-V 
     
- **Para un proceso (cambio de estado):** Para un proceso en el que el sistema cambia de un estado inicial (1) a un estado final (2), la Primera Ley establece que **el cambio neto de la energía total (ΔE) del sistema es igual a la diferencia entre la energía total que entra y la que sale del sistema**. La forma más general de esta ecuación para un sistema cerrado es: **Q - W = ΔE** Donde:
    
    - **Q** es el calor neto transferido _hacia_ el sistema. (Si el calor _sale_ del sistema, se considera negativo).
    - **W** es el trabajo neto realizado _por_ el sistema sobre los alrededores. (Si el trabajo es realizado _sobre_ el sistema por los alrededores, se considera negativo).
    - **ΔE** es el cambio en la energía total del sistema.


![[Pasted image 20250806154215.png]]

Figura 2-45 de "Termodinamica-Yunes A. Cengel_Cap2.pdf", mostrando un sistema con entradas y salidas de calor y trabajo, y el cambio de energía interna).)_
    

#### 1.2 Análisis del Cambio de Energía de un Sistema (ΔE)

La **energía total (E)** de un sistema se compone de varias formas de energía. En un análisis termodinámico, es útil considerar dos grupos:

- **Energías macroscópicas:** Son las que posee un sistema como un todo en relación con un marco de referencia externo. Incluyen:
    - **Energía Cinética (EC):** Asociada al movimiento del sistema. Se calcula como **EC = (m * V^2) / 2**. Por unidad de masa, **ec = V^2 / 2**.
    - **Energía Potencial (EP):** Asociada a la posición de un sistema en un campo gravitacional. Se calcula como **EP = m * g * z**. Por unidad de masa, **ep = g * z**.
- **Energía microscópica (Energía Interna, U):** Se relaciona con la estructura molecular del sistema y el grado de actividad molecular, siendo independiente de los marcos de referencia externos. Es la suma de las energías cinéticas y potenciales de las moléculas. La energía interna (U) puede incluir:
    - **Energía Sensible:** Energía cinética de las moléculas (traslación, rotación, vibración), directamente relacionada con la temperatura.
    - **Energía Latente:** Energía asociada a la fase de un sistema, que se manifiesta durante un cambio de fase sin alterar la composición química.
    - **Energía Química:** Asociada a los enlaces atómicos dentro de las moléculas. Se libera o absorbe durante reacciones químicas.
    - **Energía Nuclear:** Asociada a los enlaces dentro del núcleo del átomo. Se libera en reacciones de fisión o fusión.

El **cambio de energía total (ΔE)** del sistema es simplemente la diferencia entre la energía en el estado final (E2) y el inicial (E1): **ΔE = E2 - E1** Considerando las componentes, **ΔE = ΔU + ΔEC + ΔEP**.

- **Para la mayoría de los sistemas cerrados en problemas prácticos, si permanecen estacionarios (velocidad y altura de su centro de gravedad no cambian significativamente), entonces ΔEC = 0 y ΔEP = 0**. En estos casos, la Primera Ley se simplifica a: **Q - W = ΔU**. Por unidad de masa: **q - w = Δu**.

#### 1.3 Cálculos Energéticos en Sistemas Cerrados

El cálculo del trabajo (W) y el calor (Q) en sistemas cerrados depende del tipo de proceso que experimenta el sistema.

- **Trabajo de frontera móvil (W = ∫PdV):** Es el trabajo más común en sistemas cerrados, donde la frontera del sistema (ej. un pistón) se mueve.
    
    - **Proceso a volumen constante (Isocórico):** Si el volumen no cambia (dV = 0), el trabajo de frontera es **W = 0**. La primera ley se reduce a **Q = ΔU**.
    - **Proceso a presión constante (Isobárico):** El trabajo se calcula como **W = P(V2 - V1)**. La primera ley se puede expresar como **Q = ΔH** (cambio en la entalpía del sistema).
    - **Proceso a temperatura constante (Isotérmico, para un gas ideal):** Para un gas ideal, la energía interna (U) depende solo de la temperatura, por lo que **ΔU = 0** en un proceso isotérmico. Así, **Q = W**. El trabajo se calcula como **W = mRT ln(V2/V1)**.
    - **Proceso adiabático (Q = 0):** No hay transferencia de calor con los alrededores (el sistema está bien aislado). La Primera Ley se convierte en **-W = ΔU**. Para un gas ideal en un proceso cuasiestacionario, esto implica **P*V^k = constante** (donde k es la relación de calores específicos Cp/Cv).
    - **Proceso politrópico (PV^n = constante):** Es un proceso general que incluye los casos anteriores. El trabajo se calcula como **W = (P1V1 - P2V2)/(n-1)**, excepto cuando n=1 (isotérmico).
- **Trabajo de eje (Paddle-wheel work):** Ocurre por un dispositivo agitador (ej. una rueda de paletas) dentro del sistema. Este trabajo siempre es negativo (realizado _sobre_ el sistema) y debe incluirse en la ecuación general de la Primera Ley.
    
    **Ejemplos de cálculo en sistemas cerrados:**
    
    - **Ejemplo 3.1 (Compresión de aire):** Se calcula el trabajo requerido para comprimir aire en un cilindro de forma **pV^1.3 = C**. Se usa **W = (P1V1 - P2V2)/(1-n)** y se determina el cambio en energía interna (ΔU = -W) para el proceso adiabático.
    - **Ejemplo 4.2 (Ventilador en habitación aislada):** Una habitación aislada (Q=0) con un ventilador, ΔPE=ΔKE=0. La Primera Ley es **-W = ΔU**. Se calcula el trabajo de entrada del ventilador para hallar el aumento de energía interna.
    - **Ejemplo 2-10 (Enfriamiento de fluido agitado):** Un fluido en un recipiente rígido (W_frontera=0) pierde calor (Q negativo) mientras es agitado por un ventilador (W_flecha negativo). La ley es **W_flecha,entrada + Q_salida = ΔU**. Se determina la energía interna final.

### 2. La Primera Ley de la Termodinámica para Sistemas Abiertos (Volúmenes de Control)

Los **sistemas abiertos**, o **volúmenes de control**, son aquellos que **permiten el intercambio de masa a través de sus fronteras, además de calor y trabajo**. Son de gran interés en ingeniería, ya que la mayoría de los dispositivos operan con flujo de masa (turbinas, compresores, bombas, etc.).

#### 2.1 Explicación de la Ecuación para Sistemas Abiertos

La energía asociada al flujo de masa que entra o sale de un volumen de control incluye la energía interna, cinética y potencial de la masa, así como la **energía de flujo (Pv)**, que representa el trabajo necesario para "empujar" la masa a través de la frontera del sistema. La combinación de energía interna y energía de flujo $(U + Pv)$ se define como **Entalpía (H)** o por unidad de masa, **entalpía específic
$$(h = u + Pv)$$

La ecuación más general del balance de energía para un volumen de control es:

$$\dot Q + \sum( \dot m_{entrada} \cdot e_{entrada}) - \dot{W} - \sum(\dot m_{salida} \cdot e_{salida}) = \frac{dE_{sistema}}{dt} $$
Donde:

- **Q̇** es la tasa neta de transferencia de calor.
- **Ẇ** es la tasa neta de trabajo (potencia).
- **Σṁ_entrada * e_entrada** es la suma de las tasas de energía asociadas a los flujos de masa que entran.
- **Σṁ_salida * e_salida** es la suma de las tasas de energía asociadas a los flujos de masa que salen.
- **dE_sistema / dt** es la tasa de cambio de la energía almacenada en el volumen de control.
- La **energía por unidad de masa del fluido (e_fluido)** se expresa como: **e_fluido = h + V^2/2 + gz**

La mayoría de las aplicaciones de ingeniería implican un **flujo estacionario (steady-flow)**, donde las propiedades del sistema no cambian con el tiempo (dE_sistema/dt = 0). En este caso, para un volumen de control con una entrada y una salida, la ecuación se simplifica a: 
$$
\dot Q - \dot W = \dot m \cdot ((h_{salida} - h_{entrada}) + (V^2_{salida} - V_{entrada}^2)/2 + g(z_{salida} - z_{entrada}) ]
$$

** O, por unidad de masa: *
$$ \dot q - \dot w = (h_{salida} - h_{entrada}) + (V_{salida}^2 - V_{entrada}^2)/2 + g(z_{salida} - z_{entrada})
$$

![[Pasted image 20250806160010.png]]
 "Thermodynamics Demystified - Merle C. Potter_cap4.pdf", mostrando un volumen de control con entradas y salidas de masa, calor y trabajo).)_

#### 2.2 Aplicaciones a Dispositivos de Ingeniería

La ecuación de la Primera Ley para sistemas abiertos se simplifica aún más para dispositivos específicos:

- **Toberas y Difusores:**
    
    - **Función:** Una **tobera** aumenta la velocidad de un fluido disminuyendo su presión y área de flujo. Un **difusor** disminuye la velocidad de un fluido, aumentando su presión.
    - **Suposiciones:** Generalmente no hay trabajo (W=0) ni transferencia de calor significativa (Q=0), y los cambios de energía potencial son despreciables (ΔEP=0).
    - **Ecuación:** **h_entrada + V_entrada^2/2 = h_salida + V_salida^2/2**.
    ![[Pasted image 20250806160218.png]]
    _(Ilustración sugerida: Figura 3.1 de "Termodinamica-Manrique_cap3.pdf", mostrando esquemas de toberas).)_
    
- **Válvulas de Estrangulamiento (Throttling Devices):**
    
    - **Función:** Provocan una caída de presión significativa en un fluido, como válvulas o medios porosos.
    - **Suposiciones:** No hay trabajo (W=0), ni transferencia de calor (Q=0), ni cambios significativos en la energía cinética (ΔEC=0) o potencial (ΔEP=0).
    - **Ecuación:** **h_entrada = h_salida**. Esto significa que la entalpía del fluido se mantiene constante entre la entrada y la salida.
    
    _(Ilustración sugerida: Figura 4.4 de "Thermodynamics Demystified - Merle C. Potter_cap4.pdf", mostrando una válvula de globo o una placa de orificio).)_
    
- **Bombas, Compresores y Turbinas:**
    
    - **Función:** Una **bomba** transfiere energía mecánica a un líquido, aumentando su presión. Un **compresor** realiza lo mismo para un gas. Una **turbina** extrae trabajo de un fluido a medida que este expande y su presión disminuye.
    - **Suposiciones:** Generalmente la transferencia de calor es despreciable (Q=0), y los cambios en la energía cinética y potencial suelen ser insignificantes (ΔEC=0, ΔEP=0).
    - **Ecuación:** **Ẇ = ṁ * (h_entrada - h_salida)**.
        - Para turbinas, **Ẇ** es positivo (trabajo producido).
        - Para bombas/compresores, **Ẇ** es negativo (trabajo consumido).
    - Para líquidos, si los cambios en energía interna son despreciables, la ecuación de trabajo se simplifica a **Ẇ = ṁ * (P_entrada - P_salida) / ρ**.
    
    _(Ilustración sugerida: Figura 3.2 de "Termodinamica-Manrique_cap3.pdf", mostrando el esquema de una turbina, y Figura 2-61 de "Termodinamica-Yunes A. Cengel_Cap2.pdf", mostrando el conjunto bomba-motor).)_
    
- **Intercambiadores de Calor:**
    
    - **Función:** Transfieren energía térmica de un fluido a otro (o a los alrededores) sin mezcla directa de los fluidos.
    - **Suposiciones:** No hay trabajo (W=0), ni cambios significativos en la energía cinética (ΔEC=0) o potencial (ΔEP=0).
    - **Ecuación (para el sistema combinado sin pérdidas de calor al exterior):** **Σ(ṁ_entrada * h_entrada) = Σ(ṁ_salida * h_salida)**.
        - Si se analiza un solo fluido en el intercambiador: **Q̇ = ṁ * (h_salida - h_entrada)**.
    
    _(Ilustración sugerida: Figura 4.5 de "Thermodynamics Demystified - Merle C. Potter_cap4.pdf", mostrando un intercambiador de calor de dos fluidos).)_
    
    **Ejemplos de cálculo en sistemas abiertos:**
    
    - **Ejemplo 3.6 (Compresión de aire en compresor):** Se estima la potencia requerida por un compresor utilizando la ecuación **W = - ∫vdp** y la relación **pv^1.4 = C**. Se observa que el trabajo es negativo porque es consumido.
    - **Ejemplo 3.14 (Potencia de turbina):** Se calcula la potencia desarrollada por una turbina de vapor usando **W = m(h1 - h2)**, despreciando cambios en energía cinética y potencial.
    - **Ejemplo 3.16 (Potencia de compresor):** Se calcula la potencia requerida por un compresor de aire considerando cambios de entalpía y energía cinética, usando **-W = h2 - h1 + V2^2/2**.
    - **Ejemplo 2-16 (Generación de potencia hidráulica):** Se calcula la energía mecánica del agua y las eficiencias de la turbina y del conjunto turbina-generador en una planta hidroeléctrica.

### 3. Variables de Cantidad de Calor y Transferencia de Calor en un Sistema Termodinámico

#### 3.1 Definición de Calor y Convenciones

El **calor (Q)** se define como la **forma de energía que se transfiere entre dos sistemas (o entre un sistema y sus alrededores) debido a una diferencia de temperatura**. Es crucial entender que el calor es energía en transición; solo se reconoce cuando cruza la frontera del sistema. Una vez que el calor ha sido transferido, se convierte en parte de la energía interna del sistema receptor.

- **Convención de signos:**
    
    - El **calor suministrado a un sistema es positivo (+Q)**.
    - El **calor cedido o disipado por un sistema a sus alrededores es negativo (-Q)**.
- Un **proceso adiabático** es aquel durante el cual **no hay transferencia de calor (Q = 0)**. Esto puede deberse a que el sistema está bien aislado o a que el sistema y sus alrededores están a la misma temperatura.
    
- Las unidades de calor en el Sistema Internacional son el **joule (J)** o el **kilojoule (kJ)**.
    
- La **tasa de transferencia de calor (Q̇)** es la cantidad de calor transferida por unidad de tiempo, y sus unidades son kJ/s o kW.
    
- El **calor por unidad de masa (q)** se define como **q = Q/m**.
    
    _(Ilustración sugerida: Figura 2-14 de "Termodinamica-Yunes A. Cengel_Cap2.pdf", mostrando la transferencia de calor debido a una diferencia de temperatura).)_
    

#### 3.2 Mecanismos de Transferencia de Calor

El calor se puede transferir a través de tres mecanismos básicos:

- **Conducción:**
    
    - **Descripción:** Es la transferencia de energía entre partículas adyacentes de una sustancia, de las más energéticas a las menos energéticas, debido a sus interacciones. Ocurre en sólidos, líquidos y gases.
    - **Ley de Fourier de Conducción de Calor:** La tasa de conducción de calor (Q̇_cond) es proporcional al área (A) y al gradiente de temperatura (dT/dx), e inversamente proporcional al espesor. **Q̇_cond = -kt * A * (dT/dx)** Donde **kt** es la **conductividad térmica** del material, una medida de su capacidad para conducir calor.
    
    _(Ilustración sugerida: Figura 2-71 de "Termodinamica-Yunes A. Cengel_Cap2.pdf", mostrando la conducción de calor a través de la pared de una lata).)_
    
- **Convección:**
    
    - **Descripción:** Es la transferencia de energía entre una superficie sólida y un fluido adyacente en movimiento. Implica una combinación de conducción y el movimiento macroscópico del fluido.
    - **Tipos:** Puede ser **convección forzada** (movimiento inducido por medios externos, como un ventilador) o **convección natural (o libre)** (movimiento causado por fuerzas de flotación debido a diferencias de densidad por variación de temperatura).
    - **Ley de Enfriamiento de Newton:** La tasa de transferencia de calor por convección (Q̇_conv) se determina como: **Q̇_conv = h * A * (T_s - T_f)** Donde **h** es el **coeficiente de transferencia de calor por convección** (determinado experimentalmente), **A** es el área superficial, **T_s** es la temperatura de la superficie y **T_f** es la temperatura del fluido lejos de la superficie.
    
    _(Ilustración sugerida: Figura 2-72 de "Termodinamica-Yunes A. Cengel_Cap2.pdf", mostrando la transferencia de calor por convección desde una superficie caliente).)_
    
- **Radiación:**
    
    - **Descripción:** Es la energía emitida por la materia en forma de ondas electromagnéticas (fotones) debido a cambios en las configuraciones electrónicas de los átomos o moléculas. A diferencia de la conducción y la convección, la radiación no requiere la presencia de un medio para la transferencia de energía y es el modo más rápido.
    - **Ley de Stefan-Boltzmann:** La tasa máxima de radiación emitida por una superficie a una temperatura absoluta (T_s) se da por: **Q̇_emitida,máx = σ * A * T_s^4** Donde **σ** es la **constante de Stefan-Boltzmann** (5.67 × 10^-8 W/m^2·K^4) y **A** es el área superficial. Una superficie ideal que emite a esta tasa máxima se llama **cuerpo negro**.
    - Para superficies reales, la radiación emitida es menor y se calcula como: **Q̇_emitida = ε * σ * A * T_s^4** Donde **ε** es la **emisividad** de la superficie (valor entre 0 y 1).
    - La **transferencia neta de calor por radiación** entre un cuerpo pequeño a temperatura T_s y un recinto mucho más grande a temperatura T_alrededores es: **Q̇_rad = ε * σ * A * (T_s^4 - T_alrededores^4)**
    
    _(Ilustración sugerida: Figura 2-74 de "Termodinamica-Yunes A. Cengel_Cap2.pdf", mostrando la transferencia de calor por radiación sin un medio).)_
    

---

Este material didáctico cubre los puntos solicitados de manera organizada, didáctica y con apoyo directo de las fuentes, incluyendo ecuaciones y sugerencias de ilustraciones para una mejor comprensión.