
Las máquinas térmicas se diseñan con el propósito de convertir energía tér￾mica en trabajo y su desempeño se expresa en términos de la eficiencia térmica $\eta_{ter}$, que es la relación entre el trabajo neto producido por la máquina y la entrada de calor total:
$$
	\eta_{ter} = \frac{W_{neto}}{Q_{entrada}} \qquad ó \qquad \eta_{ter} = \frac{w_{neto}}{q_{entrada}}
$$


Las máquinas térmicas operadas en un ciclo totalmente reversible, como  [[El ciclo de Carnot]],  tienen la eficiencia térmica más alta de todas las máquinas térmicas que operan entre los mismos niveles de temperatura. Es decir, nadie puede desarrollar un ciclo más eficiente que el ciclo de Carnot. 

La mayor parte de los ciclos encontrados en la práctica difieren significativamente del de Carnot, de ahí que sea inadecuado como un modelo realista. Cada ciclo ideal se relaciona con un dispositivo que produce trabajo específico y es una versión idealizada del ciclo real.

Las idealizaciones y simplificaciones empleadas comúnmente en el análisis de los ciclos de potencia, pueden resumirse del siguiente modo:
1. El ciclo no implica ninguna fricción. Por lo tanto, el fluido de trabajo no experimenta ninguna caída de presión cuando fluye en tuberías o disposi￾tivos como los intercambiadores de calor.
2. Todos los procesos de expansión y compresión ocurren en la forma de cuasiequilibrio.
3. Las tuberías que conectan a los diferentes componentes de un sistema están muy bien aisladas y la transferencia de calor a través de ellas es insignificante.

Ignorar los cambios en las energías cinética y potencial del fluido de trabajo es otra simplificación comúnmente empleada en el análisis de ciclos de potencia. Ésta es una suposición posible de relacionar porque en dispositivos que incluyen trabajo de eje, como turbinas, compresores y bombas, los términos de las energías cinética y potencial son usualmente muy pequeños respecto de los otros términos en la ecuación de la energía. 

En los diagramas P-v como en los T-s, el área encerrada por las curvas del proceso de un ciclo representa el trabajo neto producido durante el ciclo 
![[Pasted image 20250803091726.png]]
lo cual también es equivalente a la transferencia de calor neta en ese ciclo. El diagrama T-s es particularmente útil como ayuda visual en el análisis de ciclos de potencia ideales. Estos ciclos no implican cualquier irreversibilidad interna, por lo tanto el único efecto que puede cambiar la entropía del fluido de trabajo durante un proceso es la transferencia de calor.

En un diagrama T-s un proceso de adición de calor avanza en la dirección de entropía creciente, uno de rechazo de calor avanza en la dirección de entropía decreciente y uno isentrópico (internamente reversible, adiabático) avanza a entropía constante. El área bajo la curva del proceso sobre un diagrama T-s representa la transferencia de calor para ese proceso. El área bajo el proceso de adición de calor sobre un diagrama T-s es una medida geométrica del calor total suministrado durante el ciclo $q_{entrada}$, y el área bajo el proceso de rechazo de calor es una medida del calor total rechazado $q_{salida}$. La diferencia entre estos dos (el área encerrada por la curva cíclica) es la transferencia neta de calor, la cual también es el trabajo neto producido durante el ciclo. Por lo tanto, sobre un diagrama T-s, la relación entre el área encerrada por la curva cíclica y el área 
bajo la curva del proceso de adición de calor representan la eficiencia térmica del ciclo. Cualquier modificación que incremente la relación entre estas dos áreas mejorará también la eficiencia térmica del ciclo.

## EL CICLO DE CARNOT Y SU VALOR EN INGENIERÍA

El ciclo de Carnot se compone de cuatro procesos totalmente reversibles: adición de calor isotérmica, expansión isentrópica, rechazo de calor isotérmico y compresión isentrópica. Los diagramas P-v y T-s de un ciclo de Carnot se vuelven a graficar en la figura.
![[Pasted image 20250803092250.png]]
El ciclo de Carnot puede ser ejecutado en un sistema cerrado (un dispositivo de cilindro-émbolo) o en un sistema de flujo estacionario (usando dos turbinas y dos compresores, como se muestra en la figura), 
![[Pasted image 20250803092340.png]]
y puede emplearse gas o vapor como el fluido de trabajo. El ciclo de Carnot es el ciclo más eficiente que puede ejecutarse entre una fuente de energía térmica a temperatura TH y un sumidero a temperatura TL, y su eficien￾cia térmica se expresa como
$$
	\eta_{ter} = 1 - \frac{T_L}{T_H}
$$
 La transferencia de calor isotérmica reversible es muy difícil de lograr en la práctica porque requeriría intercambiadores de calor muy grandes y necesitaría mucho tiempo (un ciclo de potencia en una máquina común se completa en una fracción de un segundo). Por lo tanto, no es práctico construir una máquina que opere en un ciclo que se aproxima en gran medida al de Carnot.
 El verdadero valor del ciclo de Carnot reside en que es el estándar contra el cual pueden compararse ciclos reales o ideales. La eficiencia térmica de un ciclo de Carnot es una función de las temperaturas del sumidero y de la fuente, y la relación de la eficiencia térmica para este ciclo (Ec. 9-2) transmite un importante mensaje que es igualmente aplicable a ciclos ideales reales: _la 
eficiencia térmica aumenta con un incremento en la temperatura promedio a la cual se suministra calor hacia el sistema o con una disminución en la temperatura promedio a la cual el calor se rechaza del sistema._

## CICLO DE OTTO: EL CICLO IDEAL PARA LAS MÁQUINAS DE ENCENDIDO POR CHISPA

El ciclo de Otto es el ciclo ideal para las máquinas reciprocantes de encendido por chispa. Recibe ese nombre en honor a Nikolaus A. Otto, quien en 1876, en Alemania, construyó una exitosa máquina de cuatro tiempos utilizando el ciclo propuesto por el francés Beau de Rochas en 1862. En la mayoría de las máquinas de encendido por chispa el émbolo ejecuta cuatro tiempos completos (dos ciclos mecánicos) dentro del cilindro, y el cigüeñal completa dos revoluciones por cada ciclo termodinámico. Estas máquinas son llamadas máquinas de combustión interna de cuatro tiempos. Un diagrama esquemático de cada tiempo, así como el diagrama P-v para una máquina real de encendido por chispa de cuatro tiempos se presenta en la figura
![[Pasted image 20250803092813.png]]

Inicialmente, tanto la válvula de admisión como la de escape están cerradas y el émbolo se encuentra en su posición más baja (PMI). Durante la carrera de compresión, el émbolo se mueve hacia arriba y comprime la mezcla de aire y combustible. Un poco antes de que el émbolo alcance su posición más alta (PMS), la bujía produce una chispa y la mezcla se enciende, con lo cual aumenta la presión y la temperatura del sistema. Los gases de alta presión impulsan al émbolo hacia abajo, el cual a su vez obliga a rotar al cigüeñal, lo que produce una salida de trabajo útil durante la carrera de expansión o carrera de potencia. 

Al final de esta carrera, el émbolo se encuentra en su posición más baja (la terminación del primer ciclo mecánico) y el cilindro se llena con los productos de la combustión. Después el émbolo se mueve hacia arriba una vez más y evacua los gases de escape por la válvula de escape (carrera de escape), para descender por segunda vez extrayendo una mezcla fresca de aire y combustible a través de la válvula de admisión (carrera de admisión). Observe que la presión en el cilindro está un poco arriba del valor atmosférico durante la carrera de escape y un poco abajo durante la carrera de admisión.

En las máquinas de dos tiempos, las cuatro funciones descritas anteriormente se ejecutan sólo en dos tiempos: el de potencia y el de compresión. En estas máquinas el cárter se sella y el movimiento hacia fuera del émbolo se emplea para presurizar ligeramente la mezcla de aire y combustible en el cárter, como se muestra en la figura. 
![[Pasted image 20250803093127.png]]
Además, las válvulas de admisión y de escape se sustituyen por aberturas en la porción inferior de la pared del cilindro. Durante la última parte de la carrera de potencia, el émbolo descubre primero el puerto de escape permitiendo que los gases de escape sean parcialmente expelidos, entonces se abre el puerto de admisión permitiendo que la mezcla fresca de aire y combustible se precipite en el interior e impulse la mayor parte de los gases de escape restantes hacia fuera del cilindro. Esta mezcla es entonces comprimida cuando el émbolo se mueve hacia arriba durante la carrera de compresión y se enciende subsecuentemente mediante una bujía.

Las principales compañías de automóviles realizan programas de investigación para motores de dos tiempos que se espera que vuelvan a aparecer en el futuro cercano.
 El análisis termodinámico de los ciclos reales de cuatro y dos tiempos antes descritos no es una tarea simple. Sin embargo, el análisis puede simplificarse de manera significativa si se utilizan las suposiciones de aire estándar, ya que el ciclo que resulta y que es parecido a las condiciones de operación reales es el ciclo de Otto ideal, el cual se compone de cuatro procesos reversibles internamente:
 
	1-2 Compresión isentrópica
	2-3 Adición de calor a volumen constante
	3-4 Expansión isentrópica
	4-1 Rechazo de calor a volumen constante

 La ejecución del ciclo de Otto en un dispositivo de émbolo y cilindro junto a un diagrama P-v se ilustra en la figura 9-13b). El diagrama T-s del ciclo de Otto se presenta en la figura 
 ![[Pasted image 20250803093844.png]]
 El ciclo de Otto se ejecuta en un sistema cerrado, y sin tomar en cuenta los cambios en las energías cinética y potencial, el balance de energía para cualquiera de los procesos se expresa, por unidad de masa, como
 $$
 (q_{entrada} – q_{salida}) + (w_{entrada} – w_{salida})  = Δu \, \text{(kJ/kg)} 
 $$
No hay trabajo involucrado durante los dos procesos de transferencia de calor porque ambos toman lugar a volumen constante
Entonces, la eficiencia térmica del ciclo de Otto ideal supuesto para el aire estándar frío. Los procesos 1-2 y 3-4 son isentrópicos, y v2 = v3 y v4= v1. Por lo tanto, la relación de la eficiencia térmica y simplificando, se obtiene
$$
	\eta_{ter.Otto} = 1- \frac{1}{r^{k-1}}
$$
donde
$$
	r = \frac{V_{max}}{V_{min}}=\frac{V_1}{V_2} = \frac{v_1}{v_2}
$$

que es la relación de compresión, y $k$ es la relación de calores específicos 
cp /cv.

 En esta ecuación se muestra que bajo las suposiciones de aire estándar frío, la eficiencia térmica de un ciclo de Otto ideal depende de la relación de compresión de la máquina y de la relación de calores específicos del fluido de trabajo. 
La eficiencia térmica del ciclo de Otto ideal aumenta tanto con la relación de compresión como con la relación de calores específicos. Esto también es cierto para las máquinas de combustión interna reales de encendido por chispa. Una gráfica de la eficiencia térmica contra la relación de compresión se presenta en la figura 
![[Pasted image 20250803100148.png]]
para k  1.4, el cual es el valor de la relación de calores específicos del aire a temperatura ambiente. Para una relación de compresión dada, la eficiencia térmica de una máquina real de encendido por chispa será menor que la de un ciclo de Otto ideal debido a irreversibilidades como la fricción y a otros factores, como la combustión incompleta.
En la figura 9-17 es posible ver que la curva de la eficiencia térmica está 
más inclinada a relaciones de compresión bajas, pero se nivela a partir de 
un valor de relación de compresión aproximadamente de 8. Por consiguiente, el aumento en la eficiencia térmica con la relación de compresión no es tan pronunciado en relaciones de compresión elevadas. Asimismo, cuando se emplean altas relaciones de compresión, la temperatura de la mezcla de aire y combustible se eleva por encima de la temperatura de autoencendido del combustible (temperatura a la que el combustible se enciende sin la ayuda de una chispa) durante el proceso de combustión, con lo que causa un temprano y rápido quemado del combustible en algún punto o puntos delanteros de la frente de la flama, seguido por una combustión casi instantánea del gas remanente. Este encendido prematuro del combustible, denominado autoencendido, produce un ruido audible que recibe el nombre de golpeteo del motor o cascabeleo. El autoencendido en las máquinas de encendido por chispa no puede tolerarse debido a que perjudica el desempeño y puede dañar la máquina. El requerimiento de que el autoencendido no deba permitirse impone un límite superior en las relaciones de compresión que pueden usarse en las máquinas de combustión interna de encendido por chispa.
 Las mejoras en la eficiencia térmica de máquinas de gasolina mediante el uso de relaciones de compresión más altas (hasta aproximadamente 12) sin que se enfrenten problemas de autoencendido, ha sido posible usando mezclas de gasolina que tienen buenas características de antidetonante, como la gasolina mezclada con tetraetilo de plomo. El tetraetilo de plomo se ha agregado a la gasolina desde 1920 debido a que es el método más económico para elevar el índice de octano u octanaje, que es una medida de la resistencia de un combustible al golpeteo del motor. Sin embargo, la gasolina con plomo tiene un efecto colateral muy indeseable: forma compuestos durante el proceso de combustión que contaminan el ambiente y son muy peligrosos para la salud. En un esfuerzo por combatir la contaminación del aire, a mediados de la década de 1970, el gobierno de Estados Unidos adoptó una política que originó la discontinuación eventual de la gasolina con plomo. Imposibilitados de emplear plomo, las refinadoras desarrollaron técnicas más elaboradas para mejorar las características antidetonantes de la gasolina. La mayor parte de los automóviles fabricados a partir de 1975 se han diseñado para usar gasolina sin plomo, y las relaciones de compresión se han reducido para evitar el 
golpeteo del motor. La disponibilidad de combustibles de alto octano hizo posible elevar nuevamente las proporciones de compresión en los años recientes. También, gracias a mejoras en otras áreas (reducción en el peso total del automóvil, diseño aerodinámico mejorado, etc.) los automóviles actuales ofrecen una mejor economía de combustible y en consecuencia permiten recorrer más kilómetros por litro de combustible. Esto es un ejemplo de cómo las decisiones de ingeniería implican compromisos, y la eficiencia es únicamente una de las consideraciones en el diseño final.

 El segundo parámetro que afecta la eficiencia térmica de un ciclo de Otto ideal es la relación de calores específicos k. Para una relación de compresión dada, un ciclo de Otto ideal que emplea un gas monoatómico (como argón o helio, k  1.667) como fluido de trabajo tendrá la eficiencia térmica más alta. 
La relación de calores específicos k, y por lo tanto la eficiencia térmica de un ciclo de Otto ideal, disminuye cuando las moléculas del fluido de trabajo son más grandes (Fig. 9-18). A temperatura ambiente, este valor es de 1.4 para el aire, de 1.3 para el dióxido de carbono y de 1.2 para el etano. El fluido de trabajo en máquinas reales contiene moléculas más grandes, como dióxido de carbono, y la relación de calores específicos disminuye con la temperatura, la cual es una de las razones por las que los ciclos reales tienen eficiencias térmicas más bajas que el ciclo de Otto ideal. La eficiencia térmica de máquinas reales de encendido por chispa varía de aproximadamente 25 a 30 por ciento.

## Ejemplo
---

### **EJEMPLO 9-2 El ciclo de Otto ideal**

**Problema:** Un ciclo de Otto ideal tiene una **relación de compresión de 8**. Al inicio del proceso de compresión, el aire está a **100 kPa y 17 °C**. Se transfieren **800 kJ/kg de calor a volumen constante** hacia el aire durante el proceso de adición de calor. Tomando en cuenta la variación de los calores específicos del aire con la temperatura, determine: a) La temperatura y presión máximas que ocurren durante el ciclo. b) La salida de trabajo neto. c) La eficiencia térmica. d) La presión media efectiva en el ciclo.

**Solución:** Se considera un ciclo de Otto ideal. Se determinarán la temperatura y presión máximas, la salida de trabajo neto, la eficiencia térmica y la presión media efectiva en el ciclo.

**Suposiciones:**

1. Las suposiciones de aire estándar son aplicables.
2. Los cambios de energías cinética y potencial son insignificantes.
3. Será considerada la variación de los calores específicos debido a la temperatura.

**Análisis:** El diagrama P-v para el ciclo de Otto ideal se muestra en la figura 9-19. El aire contenido en el cilindro forma un sistema cerrado.

**a) La temperatura y presión máximas en un ciclo de Otto ocurren al final del proceso de adición de calor a volumen constante (estado 3)**. Primero, necesitamos determinar la temperatura y presión del aire al final del proceso isentrópico de compresión (estado 2), usando los datos de la tabla A-17:

- **Estado 1:**
    
    - T1 = 17 °C + 273 = 290 K
    - P1 = 100 kPa
    - u1 = 206.91 kJ/kg (obtenido de tabla A-17 para T1=290K)
    - vr1 = 676.1 (obtenido de tabla A-17 para T1=290K)
- **Proceso 1-2 (Compresión isentrópica de un gas ideal):**
    
    - Relación de compresión (r) = V1/V2 = 8
    - Para el proceso isentrópico, V2/V1 = vr2/vr1.
    - Entonces, vr2 = vr1 / r = 676.1 / 8 = 84.51.
    - De la tabla A-17, para vr2 = 84.51, **T2 ≈ 652.4 K** y **u2 = 475.11 kJ/kg**.
    - P2 = P1 * (T2/T1) * (V1/V2) = 100 kPa * (652.4 K / 290 K) * 8 = **1799.7 kPa ≈ 1.7997 MPa**.
- **Proceso 2-3 (Adición de calor a volumen constante):**
    
    - qentrada = 800 kJ/kg
    - qentrada = u3 - u2
    - u3 = u2 + qentrada = 475.11 kJ/kg + 800 kJ/kg = 1275.11 kJ/kg.
    - De la tabla A-17, para u3 = 1275.11 kJ/kg, **T3 ≈ 1575.1 K** (que es la temperatura máxima).
    - Como el proceso es a volumen constante (V2 = V3), podemos encontrar P3 usando la ley de los gases ideales: P3/T3 = P2/T2.
    - P3 = P2 * (T3/T2) = 1799.7 kPa * (1575.1 K / 652.4 K) = **4345 kPa ≈ 4.345 MPa** (que es la presión máxima).

**b) La salida de trabajo neto para el ciclo se determina al encontrar la transferencia neta de calor, que es equivalente al trabajo neto realizado durante el ciclo**. Necesitamos encontrar la energía interna del aire en el estado 4:

- **Proceso 3-4 (Expansión isentrópica de un gas ideal):**
    
    - V4 = V1 y V3 = V2. Por lo tanto, V4/V3 = V1/V2 = r = 8.
    - Para el proceso isentrópico, vr4/vr3 = V4/V3.
    - De la tabla A-17, para T3 = 1575.1 K, vr3 ≈ 6.108.
    - vr4 = r * vr3 = 8 * 6.108 = 48.864.
    - De la tabla A-17, para vr4 = 48.864, **T4 ≈ 795.6 K** y **u4 = 588.74 kJ/kg**.
- **Proceso 4-1 (Rechazo de calor a volumen constante):**
    
    - qsalida = u4 - u1
    - qsalida = 588.74 kJ/kg - 206.91 kJ/kg = **381.83 kJ/kg**.

Por lo tanto, el trabajo neto (wneto) es:

- **wneto = qneto = qentrada - qsalida = 800 kJ/kg - 381.83 kJ/kg = 418.17 kJ/kg**.

**c) La eficiencia térmica del ciclo se determina a partir de su definición:**

- ηtér = wneto / qentrada
- ηtér = 418.17 kJ/kg / 800 kJ/kg = **0.523 o 52.3%**.

Bajo las suposiciones de aire estándar frío (valores de calores específicos constantes a temperatura ambiente), la eficiencia térmica sería (Ec. 9-8):

- ηtér,Otto = 1 - 1 / r^(k-1) = 1 - 1 / 8^(1.4-1) = **0.565 o 56.5%**.
    - _Comentario:_ Este valor es considerablemente diferente del obtenido antes, lo que indica que debe tenerse cuidado al utilizar las suposiciones de aire estándar frío.

**d) La presión media efectiva (PME) se determina por su definición, a partir de la ecuación 9-4:**

- PME = wneto / (vmax - vmin)
- Sabemos que v1 = vmax y v2 = vmin. Además, v1 / v2 = r.
- v1 = R * T1 / P1 (usando la constante de gas para el aire R = 0.287 kPa·m³/kg·K, de la tabla A-2)
- v1 = (0.287 kPa·m³/kg·K * 290 K) / 100 kPa = 0.832 m³/kg.
- PME = wneto / (v1 - v1/r) = wneto / (v1 * (1 - 1/r))
- PME = 418.17 kJ/kg / (0.832 m³/kg * (1 - 1/8)) = **574 kPa**.

**Comentario:** Observe que una presión constante de 574 kPa durante la carrera de potencia producirá la misma salida de trabajo neto que el ciclo completo.

---


l**EJEMPLO 9-3 El ciclo Diesel ideal**

**Problema:** Un ciclo Diesel ideal con aire como fluido de trabajo tiene una **relación de compresión de 18** y una **relación de corte de admisión de 2**. Al principio del proceso de compresión el fluido de trabajo está a **14.7 psia, 80 °F y 117 pulg³**. Utilice las suposiciones de aire estándar frío y determine:

a) La temperatura y presión del aire al final de cada proceso. b) La salida de trabajo neto y la eficiencia térmica. c) La presión media efectiva.

**Solución:** Se tiene un ciclo Diesel ideal. Se determinará la temperatura y la presión al final de cada proceso, la salida de trabajo neto y la eficiencia térmica, así como la presión media efectiva.

**Suposiciones:**

1. Las suposiciones de aire estándar frío son aplicables, por lo tanto, puede suponerse que el aire tiene calores específicos constantes a temperatura ambiente.

2. Los cambios de energía cinética y potencial son insignificantes.

**Propiedades:** La constante de gas del aire es R = 0.3704 psia · pie³/lbm · R, mientras que sus otras propiedades a temperatura ambiente son cp = 0.240 Btu/lbm · R, cV = 0.171 Btu/lbm · R y k = 1.4 (Tabla A-2Ea)

.

**Análisis:** El diagrama P-V del ciclo Diesel ideal se muestra en la figura 9-24

. Se observa que el aire contenido en el cilindro forma un sistema cerrado.

**a) Los valores de la temperatura y la presión al final de cada proceso pueden determinarse si se utilizan las relaciones isentrópicas de gas ideal para los procesos 1-2 y 3-4.** Pero primero determine los volúmenes al final de cada proceso a partir de las definiciones de la relación de compresión y de la relación de corte de admisión:

• **Estado 1:**

    ◦ P1 = 14.7 psia

    ◦ T1 = 80 °F + 460 = **540 R**

    ◦ V1 = 117 pulg³

• **V2:**

    ◦ Relación de compresión (r) = V1/V2 = 18

    ◦ V2 = V1 / r = 117 pulg³ / 18 = **6.5 pulg³**

• **V3:**

    ◦ Relación de corte de admisión (rc) = V3/V2 = 2

    ◦ V3 = rc * V2 = 2 * 6.5 pulg³ = **13 pulg³**

• **V4:**

    ◦ V4 = V1 = **117 pulg³** (proceso 4-1 a volumen constante)

• **Proceso 1-2 (Compresión isentrópica de un gas ideal, calores específicos constantes):**

    ◦ T2 = T1 * (V1/V2)^(k-1) = 540 R * (18)^(1.4-1) = **1716 R**

    ◦ P2 = P1 * (V1/V2)^k = 14.7 psia * (18)^1.4 = **841 psia**

• **Proceso 2-3 (Adición de calor a un gas ideal a presión constante):**

    ◦ P3 = P2 = **841 psia**

    ◦ T3 = T2 * (V3/V2) (como P2V2/T2 = P3V3/T3 y P2=P3) = 1716 R * (13 pulg³ / 6.5 pulg³) = 1716 R * 2 = **3432 R**

• **Proceso 3-4 (Expansión isentrópica de un gas ideal, calores específicos constantes):**

    ◦ T4 = T3 * (V3/V4)^(k-1) = 3432 R * (13 pulg³ / 117 pulg³)^(1.4-1) = 3432 R * (1/9)^0.4 = **1425 R**

    ◦ P4 = P3 * (V3/V4)^k = 841 psia * (13 pulg³ / 117 pulg³)^1.4 = 841 psia * (1/9)^1.4 = **38.8 psia**

**b) El trabajo neto para un ciclo es equivalente a la transferencia de calor neta.**

Primero es necesario calcular la masa del aire:

• m = (P1 * V1) / (R * T1)

• m = (14.7 psia * 117 pulg³) / (0.3704 psia·pie³/lbm·R * 540 R) * (1 pie³ / 1728 pulg³) = **0.00498 lbm**

El proceso 2-3 es de adición de calor a presión constante, para el cual el trabajo de frontera y Δu pueden combinarse para formar Δh. Por lo tanto:

• Qentrada = m * cp * (T3 - T2)

• Qentrada = 0.00498 lbm * 0.240 Btu/lbm·R * (3432 - 1716) R = **2.051 Btu**

El proceso 4-1 es de rechazo de calor a volumen constante (no incluye interacciones de trabajo) y la cantidad de calor rechazado es:

• Qsalida = m * cV * (T4 - T1)

• Qsalida = 0.00498 lbm * 0.171 Btu/lbm·R * (1425 - 540) R = **0.754 Btu**

Por lo tanto, el trabajo neto (Wneto) es:

• Wneto = Qentrada - Qsalida = 2.051 Btu - 0.754 Btu = **1.297 Btu**

Entonces, la eficiencia térmica (ηtér) es:

• ηtér = Wneto / Qentrada = 1.297 Btu / 2.051 Btu = **0.632 o 63.2%**

La eficiencia térmica de este ciclo Diesel bajo las suposiciones de aire estándar frío podría determinarse también de la ecuación 9-12

:

• ηtér,Diesel = 1 - (1 / r^(k-1)) * [(rc^k - 1) / (k * (rc - 1))]

• ηtér,Diesel = 1 - (1 / 18^(1.4-1)) * [(2^1.4 - 1) / (1.4 * (2 - 1))] = 1 - (1 / 18^0.4) * [(2.639 - 1) / (1.4 * 1)] = 1 - (1 / 3.176) * (1.639 / 1.4) = 1 - 0.3148 * 1.1707 = 1 - 0.3685 = **0.6315 o 63.2%** (coincide con el cálculo anterior).

**c) La presión media efectiva (PME) se determina a partir de su definición, de la ecuación 9-4:**

• PME = Wneto / (Vmáx - Vmín) = Wneto / (V1 - V2)

• PME = 1.297 Btu / (117 - 6.5) pulg³ * (778.17 lbf·pie / 1 Btu) * (1 pie / 12 pulg)

• PME = 1.297 Btu / (110.5 pulg³) * (778.17 lbf·pie / 1 Btu) * (1 pie / 12 pulg) = **110 psia**

**Comentario:** Observe que una presión constante de 110 psia durante la carrera de potencia produciría la misma salida de trabajo neto que el ciclo Diesel completo.