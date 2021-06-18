# Tarea 1 (Documentación)

### El problema que decidieron resolver

El problema que escogí fue el problema 1, sobre gatos y ratones.

> "Tengo k gatos (y desafortunadamente, l ratones) en su casa. Le sirvo la comida a mis gatos en m platos. Gatos y ratones han llegado a un acuerdo para repartirse el tiempo y comida — Pero tienen que convencerme de que están haciendo su trabajo."

> - Los gatos pueden comer de sus m platos de comida. 
> - Los ratones pueden comer de esos mismos platos siempre y cuando no sean vistos. 
> - Si un gato ve a un ratón comiendo, se lo debe comer (para mantener su reputación). 
> - Los platos están puestos uno junto al otro.
    > - Sólo un animal puede comer de cada plato a la vez. 
    > - Si un gato está comiendo y un ratón comienza a comer de otro plato, el gato lo ve (y se lo come).
    > - Por acuerdo de caballeros, los gatos no se van a acercar a los platos mientras hay ratones comiendo.

> - Importante: ¡Hay que evitar la inanición!


### El lenguaje y entorno en que lo desarrollaron.

Para ejecutar el programa debe estar instalado Python ^3.
Dependiendo del binario de Python en la máquina, ejecuta desde el directorio del archivo:

```shell
py cats_and_mice.py
```

Puede variar los valores de k, l, m del enunciado del problema modificando los valores en el código. 

Podrás ver mensajes de la ejecución del programa en salida estándar. 
Termina con Ctrl + C ó Ctrl + Pause (en Windows)

### La estrategia de sincronización (mecanismo / patrón) que les funcionó

El patron es una versión similar al patrón apagador, y además se hace uso de un torniquete, similar pero no igual al problema del lector-escritores para evitar la inanición. Además se hace uso de varios mutex(es).

### Explicación de la implementación

Se consideran 4 acciones:
- Gato entra a zona de platos
- Gato deja zona de platos
- Ratón entra a zona de platos
- Ratón deja zona de platos

Cuando un gato quiere entrar a zona de platos, se debe:
- Esperar a que los gatos puedan entrar. (Por ejemplo, si hay ratones esperar a que se vayan). En este mismo paso se hace que los ratones no puedan entrar.
- Agregar al gato a la zona de platos.

Cuando un gato quiere irse de la zona de platos, se debe:
- Esperar a que los gatos puedan salir. (Por ejemplo, si hay ratones no queremos que los gatos se vayan sin comer ratones). En este mismo paso se hace que los ratones no puedan salir.
- Quitar al gato de la zona de platos.

Cuando un ratón quiere entrar a zona de platos, se debe:
* Si es ratón es el primero en entrar:
    - Esperar a que todos los gatos que se están yendo se vayan de la zona de platos / Al mismo paso marcar que los gatos ya no puedan irse.
    - Esperar a que todos los gatos que están entrando, ingresen de la zona de platos / Al mismo paso marcar que los gatos ya no puedan entrar.
* Si hay gatos en la zona de platos:
    - Marcar que el ratón fue capturado, porque entró cuando había gatos.
- Agregar al ratón a la zona de platos.

Cuando un ratón quiere irse de la zona de platos, se debe:
- Quitar al ratón de la zona de platos
* Si el ratón es último en irse:
    - marcar que los gatos ya puedan entrar.
    - marcar que los gatos ya puedan irse.

Para evitar la inanición, la estrategia que se sigue es poner un torniquete. Cuando un gato se "forma" para entrar a la zona de platos, no se deja que más ratones entren a la zona de platos. Así, sólo cabe esperar a que todos los ratones salgan de la zona de platos o sean devorados por los gatos en la zona de platos.

De esta forma, se asegura que los gatos puedan entrar a la zona de platos y los ratones no la "monopolicen".

### Si están implementando alguno de los refinamientos

Evitar la inanición? O se consideraba parte importante del ejercicio?

### Espacio para mejoras

Con la implementación actual, un gato/raton puede "formarse" para el mismo plato de comida aún cuando hay otros platos de comida vacíos. No debe ser muy difícil corregir esta situación.