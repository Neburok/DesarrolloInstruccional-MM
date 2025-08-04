
---

# **Introducción a la Transferencia de Calor: Conceptos Fundamentales y Mecanismos**

La ciencia de la transferencia de calor es una disciplina fundamental en la ingeniería que se ocupa de la **rapidez o razón de la transferencia de energía** como calor. A menudo se confunde con la termodinámica, pero es crucial entender su distinción.

## **1. Termodinámica vs. Transferencia de Calor**

- **Termodinámica**: Esta ciencia se enfoca en la **cantidad de transferencia de calor** que ocurre cuando un sistema pasa de un estado de equilibrio a otro. Por ejemplo, puede determinar cuánto calor debe transferirse para que el café en un termo se enfríe de 90°C a 80°C. Sin embargo, la termodinámica **no indica cuánto tiempo durará ese proceso**. Se interesa en los estados de equilibrio y los cambios entre ellos.
- **Transferencia de Calor**: A diferencia de la termodinámica, la transferencia de calor se interesa en la **rapidez o razón (por unidad de tiempo)** a la que esta energía se transfiere. Su estudio es esencial en el diseño y evaluación de equipos de ingeniería, como intercambiadores de calor, calderas, radiadores y sistemas de aire acondicionado. La transferencia de calor se ocupa de sistemas donde existe un **desequilibrio térmico**.

El requisito básico para la transferencia de calor es la presencia de una **diferencia de temperatura**. La energía siempre se transfiere del medio con **temperatura más elevada al de temperatura más baja**, y este proceso se detiene cuando ambos alcanzan la misma temperatura. Cuanto mayor sea el **gradiente de temperatura** (diferencia de temperatura por unidad de longitud), mayor será la razón de transferencia de calor.

## **2. Calor y Otras Formas de Energía**

La energía existe en diversas formas, como térmica, mecánica, cinética, potencial, eléctrica, magnética, química y nuclear, cuya suma constituye la **energía total (E)** de un sistema.

- **Energía Interna (U)**: Es la suma de todas las formas microscópicas de energía relacionadas con la estructura molecular y el grado de actividad molecular de un sistema.
    - **Energía Sensible (o calor sensible)**: La parte de la energía interna asociada con la energía cinética de las moléculas. Es proporcional a la temperatura; a mayor temperatura, mayor energía cinética y, por ende, mayor energía sensible.
    - **Energía Latente (o calor latente)**: La energía interna asociada con la fase de un sistema. Se agrega energía para vencer las fuerzas moleculares durante un cambio de fase (por ejemplo, de sólido a gas), lo que eleva la energía interna del sistema en la nueva fase.
    - **Energía Química (o de enlace)**: Energía interna asociada con los enlaces atómicos en una molécula.
    - **Energía Nuclear**: Energía interna asociada con los enlaces dentro del núcleo del átomo.

En la vida diaria, las formas sensible y latente de la energía interna a menudo se denominan simplemente "calor". Sin embargo, en termodinámica se prefiere el término **energía térmica** para evitar confusiones con la "transferencia de calor". No obstante, por convención, a la energía térmica se le llama **calor** y a su transferencia se le llama **transferencia de calor**.

- La **cantidad de calor transferido** se denota por **Q**.
- La **razón de transferencia de calor** (cantidad de calor transferido por unidad de tiempo) se denota por **Q̇** y tiene unidades de J/s o W. Si Q̇ es constante, la cantidad total de calor transferido en un intervalo de tiempo Δt es **Q = Q̇ Δt**.
- El **flujo de calor (q̇)** es la razón de transferencia de calor por unidad de área perpendicular a la dirección de transferencia, expresado como **q̇ = Q̇/A** (W/m²).

## **3. Primera Ley de la Termodinámica (Balance de Energía)**

La primera ley de la termodinámica, también conocida como el **principio de conservación de la energía**, establece que la energía no se crea ni se destruye, solo cambia de forma. Para cualquier sistema que experimenta un proceso, el **cambio neto en la energía total del sistema es igual a la diferencia entre la energía total que entra y la que sale**.

- **Eent - Esal = ΔEsistema**
- En forma de razones (por unidad de tiempo): **Ėent - Ėsal = dEsistema/dt**.
- Para sistemas en **estado estacionario**, donde el estado del sistema no cambia con el tiempo (ΔEsistema = 0), el balance de energía se reduce a **Ėent = Ėsal**.

En el análisis de transferencia de calor, el interés se centra en la energía térmica. Si se considera la conversión de otras energías (nuclear, química, mecánica, eléctrica) en energía térmica como **generación de calor (Egen)**, el balance de energía puede expresarse como:

- **Qent - Qsal + Egen = ΔEtérmica,sistema**.

**Aplicación del balance de energía:**

- **Sistemas cerrados (masa fija)**: Para la mayoría de los sistemas prácticos, la energía total se reduce a la energía interna (U). Si el sistema es estacionario y solo hay transferencia de calor sin interacción de trabajo, el balance se simplifica a **Q = mc_v ΔT**.
- **Sistemas de flujo estacionario**: Muchos aparatos de ingeniería (calentadores de agua, radiadores de automóviles) involucran flujo de masa. En condiciones estacionarias, el contenido total de energía del volumen de control permanece constante (ΔE_VC = 0). Si los cambios en las energías cinética y potencial son despreciables y no hay interacción de trabajo, el balance de energía se reduce a **Q̇ = ṁ Δh = ṁ c_p ΔT**.
    - El **gasto de masa (ṁ)** es la cantidad de masa que fluye por unidad de tiempo. Para flujo unidimensional en un tubo, **ṁ = ρVA_c** (kg/s).
    - La **entalpía (h)** es una combinación de energía interna (u) y energía de flujo (Pv), útil para el análisis de fluidos en movimiento: **h = u + Pv**.
- **Balance de energía en la superficie**: Una superficie no contiene volumen ni masa, por lo tanto, no almacena energía ni genera calor. Para una superficie, el balance de energía es **Ėent = Ėsal**. Esto es válido tanto para condiciones estacionarias como transitorias.

## **4. Mecanismos Básicos de Transferencia de Calor**

El calor se puede transferir de tres modos diferentes: **conducción, convección y radiación**. Todos requieren una diferencia de temperatura y siempre ocurren del medio de mayor temperatura al de menor temperatura.

### **A. Conducción**

La conducción es la **transferencia de energía de las partículas más energéticas de una sustancia a las adyacentes menos energéticas**, como resultado de la interacción entre ellas.

- **¿Dónde ocurre?**: Puede tener lugar en sólidos, líquidos o gases.
    - En **gases y líquidos**, se debe a las colisiones y la difusión de moléculas durante su movimiento aleatorio.
    - En **sólidos**, se debe a la combinación de vibraciones de las moléculas en una retícula cristalina y al transporte de energía por parte de los electrones libres.
- **Factores que influyen**: La razón de la conducción de calor depende de la configuración geométrica, el espesor del medio, el material y la diferencia de temperatura.
- **Ley de Fourier de la Conducción del Calor**: La razón de la conducción de calor a través de una capa plana es proporcional a la diferencia de temperatura y al área de transferencia, e inversamente proporcional al espesor.
    - **Q̇_cond = -kA (dT/dx)** (W).
    - Donde:
        - **k** es la **conductividad térmica** del material (W/m·°C o W/m·K).
        - **A** es el área de transferencia de calor, siempre normal a la dirección de transferencia.
        - **dT/dx** es el gradiente de temperatura. El signo negativo asegura que la transferencia de calor en la dirección x positiva sea una cantidad positiva, ya que el calor fluye en la dirección de la temperatura decreciente.
- **Conductividad Térmica (k)**: Es una medida de la capacidad de un material para conducir calor.
    - Un **valor elevado de k** indica un buen conductor de calor (ej. cobre, plata). Estos también suelen ser buenos conductores eléctricos.
    - Un **valor bajo de k** indica un mal conductor o un aislante (ej. caucho, madera, aire).
    - Los **gases puros** tienen baja conductividad térmica; aumenta con la temperatura y disminuye con la masa molar.
    - Las **conductividades térmicas de los líquidos** suelen estar entre las de los sólidos y los gases, y a menudo decrecen al aumentar la temperatura (el agua es una excepción notable).
    - En **sólidos**, las conductividades térmicas de los metales puros son elevadas debido a los electrones libres. Las **aleaciones metálicas** suelen tener conductividades térmicas mucho más bajas que los metales que las componen.
    - La conductividad térmica de los materiales **varía con la temperatura**, aunque a menudo se evalúa a una temperatura promedio y se considera constante para simplificar los cálculos.
    - Un material se considera **isotrópico** si tiene propiedades uniformes en todas las direcciones.
- **Difusividad Térmica (α)**: Representa cuán rápido se difunde el calor a través de un material.
    - **α = k / (ρc_p)** (m²/s).
    - Donde **ρc_p** es la **capacidad calorífica** (energía que almacena un material por unidad de volumen).
    - Una **alta difusividad térmica** indica una rápida propagación del calor.

### **B. Convección**

La convección es el modo de transferencia de energía entre una **superficie sólida y el líquido o gas adyacente que está en movimiento**, e incluye los efectos combinados de la **conducción y el movimiento del fluido**. Cuanto más rápido se mueve el fluido, mayor es la transferencia de calor por convección.

- **Tipos de Convección**:
    - **Convección Forzada**: El fluido es forzado a fluir sobre la superficie por medios externos, como un ventilador, una bomba o el viento.
    - **Convección Natural (o Libre)**: El movimiento del fluido es causado por fuerzas de empuje inducidas por diferencias de densidad, las cuales son resultado de variaciones de temperatura dentro del fluido.
- **Convección con Cambio de Fase**: Procesos como la ebullición o la condensación también se consideran convección debido al movimiento del fluido inducido durante el cambio de fase (ej. burbujas de vapor subiendo).
- **Ley de Newton del Enfriamiento**: La razón de la transferencia de calor por convección es proporcional a la diferencia de temperatura.
    - **Q̇_conv = h A_s (T_s - T_∞)** (W).
    - Donde:
        - **h** es el **coeficiente de transferencia de calor por convección** (W/m²·°C o W/m²·K). No es una propiedad del fluido, sino un parámetro experimental que depende de la geometría de la superficie, la naturaleza y velocidad del movimiento del fluido, y sus propiedades.
        - **A_s** es el área superficial a través de la cual ocurre la transferencia de calor por convección.
        - **T_s** es la temperatura de la superficie.
        - **T_∞** es la temperatura del fluido suficientemente alejado de la superficie.

### **C. Radiación**

La radiación es la **energía emitida por la materia en forma de ondas electromagnéticas (o fotones)**, resultado de cambios en las configuraciones electrónicas de átomos o moléculas.

- **No requiere un medio**: A diferencia de la conducción y la convección, la radiación puede transferir calor a través del vacío y es el modo más rápido de transferencia (a la velocidad de la luz). Un ejemplo es la energía del Sol que llega a la Tierra.
- **Radiación Térmica**: Es la forma de radiación emitida por los cuerpos debido a su temperatura. Todos los cuerpos a una temperatura superior al cero absoluto emiten radiación térmica.
- **Ley de Stefan-Boltzmann**: Expresa la razón máxima de radiación que puede emitirse desde una superficie a una temperatura termodinámica T_s (en K o R).
    - **Q̇_emitida,máx = σ A_s T_s^4** (W).
    - Donde **σ** es la **constante de Stefan-Boltzmann** (5.67 × 10⁻⁸ W/m²·K⁴).
    - La superficie idealizada que emite radiación a esta razón máxima se llama **cuerpo negro**.
- **Emisividad (ε)**: La radiación emitida por las superficies reales es menor que la de un cuerpo negro a la misma temperatura. La emisividad (0 ≤ ε ≤ 1) es una medida de cuán cerca está una superficie de ser un cuerpo negro (para un cuerpo negro, ε = 1).
    - **Q̇_emitida = ε A_s T_s^4** (W).
- **Absortividad (α)**: Es la fracción de la energía de radiación incidente sobre una superficie que es absorbida por ella (0 ≤ α ≤ 1). Un cuerpo negro es un absorbente perfecto (α = 1).
- **Ley de Kirchhoff de la Radiación**: Establece que la emisividad y la absortividad de una superficie a una temperatura y longitud de onda dadas son iguales.
- **Radiación Neta**: La diferencia entre la radiación emitida por la superficie y la radiación absorbida. Si una superficie de emisividad ε y área A_s a temperatura T_s está rodeada por una superficie mucho más grande a temperatura T_alred, la razón neta de transferencia de calor por radiación es:
    - **Q̇_rad = ε A_s (T_s^4 - T_alred^4)** (W).
    - Es importante usar **temperaturas termodinámicas (absolutas)** en los cálculos de radiación.
- **Coeficiente Combinado de Transferencia de Calor (h_combinado)**: Se define para incluir los efectos tanto de la convección como de la radiación, especialmente cuando la radiación es significativa (ej. en convección natural), permitiendo expresar la razón total de transferencia de calor como **Q̇_total = h_combinado A_s (T_s - T_∞)**.

## **5. Mecanismos Simultáneos de Transferencia de Calor**

Aunque existen tres mecanismos, no siempre los tres pueden ocurrir simultáneamente en un mismo medio.

- **Sólidos Opacos**: Solo ocurre **conducción**. Sin embargo, en sus superficies expuestas a un fluido o a otras superficies, puede haber convección y/o radiación.
- **Sólidos Semitransparentes**: Pueden comprender **conducción y radiación**.
- **Fluidios Estáticos (sin movimiento masivo)**: La transferencia de calor es por **conducción y, posiblemente, por radiación**.
    - Los gases son prácticamente transparentes a la radiación (actúan como el vacío).
    - Los líquidos suelen ser fuertes absorbentes de radiación.
- **Fluidios en Movimiento**: La transferencia de calor es por **convección y radiación**. La convección puede verse como una combinación de conducción y movimiento de fluido.
- **Vacío**: La transferencia de calor solo ocurre por **radiación**, ya que la conducción y la convección requieren de un medio material.

## **6. Aplicaciones Comunes**

La transferencia de calor es omnipresente en la ingeniería y la vida cotidiana. Algunos ejemplos incluyen:

- Diseño de aparatos domésticos como sistemas de calefacción y aire acondicionado, refrigeradores, calentadores de agua, y dispositivos electrónicos (computadoras, TV).
- Determinación del espesor óptimo de aislamiento en casas y tuberías.
- Radiadores de automóviles y colectores solares.
- El propio cuerpo humano, que emite calor constantemente, y nuestra comodidad está ligada a esta razón de rechazo de calor, controlada por la vestimenta.

Comprender estos conceptos y mecanismos es crucial para resolver problemas prácticos y diseñar sistemas eficientes en diversas áreas de la ingeniería.


## **Ejercicios Resueltos**
### **Ejercicio 1: Transferencia de Calor por Conducción**

**Problema:** Una ventana de vidrio tiene **1.5 m de alto, 0.8 m de ancho y un espesor de 0.5 cm**. Si las temperaturas de sus superficies interior y exterior son de **20°C y 5°C**, respectivamente, y la conductividad térmica del vidrio es **0.78 W/m·°C**, determine la razón de la pérdida de calor a través de esta ventana en estado estacionario.

**Objetivo:** Determinar la razón de pérdida de calor por conducción a través de una pared plana.

**Suposiciones:**

- Existen condiciones de **estado estacionario**, lo que significa que la temperatura no cambia con el tiempo.
- Se pueden usar **propiedades constantes** para el vidrio.
- La transferencia de calor es **unidimensional** a través del espesor del vidrio.

**Propiedades:**

- Conductividad térmica del vidrio, **k = 0.78 W/m·°C**.

**Análisis:** La conducción es la transferencia de energía de las partículas más energéticas a las adyacentes menos energéticas por interacción. La razón de la conducción de calor a través de una capa plana (como una ventana) es proporcional a la diferencia de temperatura y al área de transferencia, e inversamente proporcional al espesor. Esto se describe mediante la **Ley de Fourier de la Conducción del Calor**.

Primero, calculamos el área de transferencia de calor (A) y convertimos el espesor a metros:

- Área de la ventana (A) = alto × ancho = 1.5 m × 0.8 m = **1.2 m²**.
- Espesor del vidrio (L) = 0.5 cm = **0.005 m**.

Ahora, aplicamos la fórmula para la razón de conducción del calor a través de una capa plana: **Q̇_cond = kA (T_1 - T_2) / L**

Donde:

- k = 0.78 W/m·°C
- A = 1.2 m²
- T_1 = 20°C
- T_2 = 5°C
- L = 0.005 m

Sustituyendo los valores: Q̇_cond = (0.78 W/m·°C) * (1.2 m²) * (20°C - 5°C) / (0.005 m) Q̇_cond = (0.78 * 1.2 * 15) / 0.005 W Q̇_cond = 14.04 / 0.005 W **Q̇_cond = 2808 W**

**Discusión:** La ventana está perdiendo **2808 W** de calor. Este ejemplo ilustra cómo la Ley de Fourier permite cuantificar la transferencia de energía a través de un material sólido debido a una diferencia de temperatura. Un mayor espesor del material o una menor conductividad térmica (es decir, un buen aislante) reducirían esta pérdida de calor.

---

### **Ejercicio 2: Transferencia de Calor por Convección**

**Problema:** Una persona está de pie en una habitación donde la temperatura del aire es de **22°C**. Si el área superficial expuesta de la persona es de **1.7 m²** y su temperatura superficial promedio es de **30°C**, determine la razón de transferencia de calor por convección de la persona al aire. Considere un coeficiente de transferencia de calor por convección de **6 W/m²·°C**. Descarte cualquier transferencia de calor por radiación para este cálculo.

**Objetivo:** Calcular la razón de transferencia de calor por convección entre una superficie sólida y un fluido en movimiento.

**Suposiciones:**

- Existen condiciones de **estado estacionario**.
- La transferencia de calor por **radiación es despreciable**.
- El coeficiente de transferencia de calor por convección (h) se considera **constante**.

**Propiedades:**

- Temperatura superficial de la persona (T_s) = 30°C.
- Temperatura del aire ambiente (T_∞) = 22°C.
- Área superficial expuesta (A_s) = 1.7 m².
- Coeficiente de transferencia de calor por convección (h) = 6 W/m²·°C.

**Análisis:** La convección es la transferencia de energía entre una superficie sólida y un fluido adyacente que está en movimiento. El movimiento del fluido puede ser forzado (por un ventilador o bomba) o natural (por diferencias de densidad debido a variaciones de temperatura). En este caso, el movimiento del aire alrededor de la persona se consideraría convección natural. La razón de la transferencia de calor por convección se expresa mediante la **Ley de Newton del Enfriamiento**.

Aplicamos la fórmula: **Q̇_conv = h * A_s * (T_s - T_∞)**

Donde:

- h = 6 W/m²·°C
- A_s = 1.7 m²
- T_s = 30°C
- T_∞ = 22°C

Sustituyendo los valores: Q̇_conv = (6 W/m²·°C) * (1.7 m²) * (30°C - 22°C) Q̇_conv = 6 * 1.7 * 8 W **Q̇_conv = 81.6 W**

**Discusión:** La persona está perdiendo **81.6 W** de calor al aire por convección. Este valor es una aproximación, ya que en la realidad, la persona también perdería calor por radiación, pero el ejercicio se enfoca solo en la convección para simplificar y didacticismo. La velocidad del movimiento del fluido (aire en este caso) influye directamente en el coeficiente de transferencia de calor por convección (h); un aire más rápido aumentaría la transferencia de calor.

---

### **Ejercicio 3: Transferencia de Calor por Radiación**

**Problema:** Un pequeño objeto esférico negro (con una emisividad de **ε = 1**, un cuerpo negro ideal) con un área superficial de **0.1 m²** está a una temperatura de **150°C**. Este objeto está completamente rodeado por superficies que se encuentran a una temperatura uniforme de **25°C**. Determine la razón neta de transferencia de calor por radiación del objeto a sus alrededores.

**Objetivo:** Calcular la razón neta de transferencia de calor por radiación entre una superficie y sus alrededores.

**Suposiciones:**

- Existen condiciones de **estado estacionario**.
- El objeto se comporta como un **cuerpo negro ideal** (ε = 1).
- Las superficies circundantes son **mucho más grandes** que el objeto y se comportan como un cuerpo negro.
- El medio entre el objeto y las superficies circundantes (por ejemplo, aire) **no interfiere con la radiación** (actúa como el vacío).

**Propiedades:**

- Temperatura del objeto (T_s) = 150°C.
- Temperatura de los alrededores (T_alred) = 25°C.
- Área superficial del objeto (A_s) = 0.1 m².
- Emisividad del objeto (ε) = 1 (para un cuerpo negro).
- Constante de Stefan-Boltzmann (σ) = 5.67 × 10⁻⁸ W/m²·K⁴.

**Análisis:** La radiación es la energía emitida por la materia en forma de ondas electromagnéticas. A diferencia de la conducción y la convección, la radiación **no requiere de un medio material** para transferir calor y es el modo más rápido de transferencia. Todos los cuerpos a una temperatura superior al cero absoluto emiten radiación térmica.

Para calcular la razón neta de transferencia de calor por radiación, es crucial usar **temperaturas absolutas (Kelvin)**.

- Convertimos T_s a Kelvin: T_s (K) = 150°C + 273.15 = 423.15 K.
- Convertimos T_alred a Kelvin: T_alred (K) = 25°C + 273.15 = 298.15 K.

Aplicamos la fórmula para la razón neta de transferencia de calor por radiación entre una superficie y un entorno mucho más grande: **Q̇_rad = ε * A_s * σ * (T_s⁴ - T_alred⁴)**

Donde:

- ε = 1
- A_s = 0.1 m²
- σ = 5.67 × 10⁻⁸ W/m²·K⁴
- T_s = 423.15 K
- T_alred = 298.15 K

Sustituyendo los valores: Q̇_rad = 1 * (0.1 m²) * (5.67 × 10⁻⁸ W/m²·K⁴) * [(423.15 K)⁴ - (298.15 K)⁴] Q̇_rad = 0.1 * 5.67 × 10⁻⁸ * (3200770630.06 - 789230670.06) W Q̇_rad = 0.1 * 5.67 × 10⁻⁸ * (2411539960) W Q̇_rad = 0.0567 * 2411539960 * 10⁻⁸ W **Q̇_rad ≈ 136.6 W**

**Discusión:** El objeto está perdiendo aproximadamente **136.6 W** de calor por radiación a sus alrededores. La radiación es particularmente significativa cuando las temperaturas son elevadas, ya que la razón de transferencia depende de la diferencia de las temperaturas elevadas a la cuarta potencia. Este ejemplo demuestra la efectividad de la radiación como mecanismo de transferencia de calor, incluso sin un medio material.