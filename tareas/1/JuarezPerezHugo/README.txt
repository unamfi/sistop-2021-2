Juárez Pérez Hugo

Problema: 
De Gatos y Ratones.
Tengo (k=4) gatos (y desafortunadamente, (l=2) ratones) en su casa.
Le sirvo la comida a mis gatos en (m=2) platos.
Gatos y ratones han llegado a un acuerdo para repartirse el tiempo
y comida — Pero tienen que convencerme de que están haciendo
su trabajo.

Estrategia:
Decidí implementar semaforos, con el patron apagador y señalización. O lo más parecido a estos dos patrones. 
Ya que los gato son quienes revisan si hay ratones, el apagador se encuentra en el comportamiento de los gatos. No se especificaba
las cantidades de gatos,ratones y platos así que las deje arbitrariamente definidas en el codigo. 
Decidir utilizar C++ (Me gusta la mala vida), con Visual Studio 2019, ya que el compilador de microsoft MVSC es el unico en 
Windows hasta la fecha que tiene implementados los nuevos semaforos de C++20. Aun así el codigo esta escrtio con solo funciones
de la biblioteca estandar, asi que no deberia haber problema en compilar en otro entorno.

*Para compilar asegurarse de utilizar -std=c++20 o -std=c++latest

Dudas:
No supe como implementar a los gatos y ratones como clases para que asi cada objeto tuviera su proprio hilo, como tampoco
investigue mucho de como hacer que un hilo mate a otro los gatos solamente arañan a los ratones que no cumplieron el acuerdo en vez
de ser ingeridos. 

