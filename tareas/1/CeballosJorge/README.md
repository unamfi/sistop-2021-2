# Santa Claus y sus regalos 🎁🎄
## Herramientas empleadas para elaboración del código 🔨
- Lenguaje: Python
- Editor de texto: Visual Studio Code y VIM

El problema a resolver fue el de Santa Claus  el cual consiste en que Papa Noel deba salir a repartir regalos. Para ello, necesita de los renos para poder moverse a lo largo del mundo y a los elfos para envolver los regalos de los niños. En este caso se definieron 3 funciones. Dichas funciones son las siguientes:
- Reigndeer 𐂂
- Papa Noel 🎅
- Elves 🧝🏻

## Características 🤔
El hilo jefe es el de Papa Noel  y el hilo de Elves y Reigndeer son los secundarios.
Total de hilos :

- PapaNoel: 1
- Elves:  300
- Reigndeer: 10

## Funcionamiento 💻

El programa consiste en que el hilo de Santa debe de iniciarse cada vez que sea requerido para ayudar. Si no es requerido dicho hilo se suelta  y es avisado a través de los elfos y renos para que puedan ser ayudados.

Se emplearon 1 semáforo cada función y 1 mutex en los renos y los elfos (3 semáforos y 2 mutex en total). Los mutex se emplearon para llevar un control de renos en vacaciones y de elfos que están a cargo del trabajo.

La función de elfo  se encarga de determinar cuantos trabajadores estan laborando en los regalos y adquirir mas elfos para trabajar.En el dado caso de que se junten los elfos , el semaforo se suelta (release()) y se avisa a santa.

La función del reno determina los segundos totales en el que un reno se encuentra de vacaciones mediante un tiempo empleando un número aleatorio de la paquetería  de random. Cuando se encuentra el número requerido de renos para que pueda Santa laborar se suelta el semaforo (release) y posteriormente se le avisa a papa noel.

La función PapaNoel se encarga de despertar y ayudar a los otros dos dependiendo del estado de los demás semaforos.




