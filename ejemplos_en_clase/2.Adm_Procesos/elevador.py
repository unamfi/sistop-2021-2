#!/usr/bin/python3

from threading import Semaphore, Thread
from time import sleep
from random import random, choice
from termcolor import cprint, colored

freq_elev = 1              # Frecuencia (en segundos) de avance del elevador)
freq_alum = 0.1            # Frecuencia (en segundos) de llegada de un nuevo alumno
demora_puerta = 0.01       # ¡Mi solución es mala! Tuve que agregar
                           # una demora a la puerta para obligar a que
                           # se "pase el turno"
                           #
carga_max = 5              # ¿Cuántos alumnos caben en el elevador?
multiplex = Semaphore(carga_max) # Asegura que no entren más de los que caben
pisos = [0,1,2,3,4]        # Lista de pisos definidos

mut_colas = Semaphore(1)   # Un semáforo por cola para que el elevador despierte a los hilos
                           # conforme va pasando por los pisos
colas = {}                 # Listas de alumnos formados en cada uno de los pisos
puerta = Semaphore(1)      # Uso exclusivo de la "puerta" (para controlar cuántos hay dentro)
a_bordo = {}               # Lista de hilos que están a bordo, separados por piso destino


# Las colas de espera por el elevador y de espera para bajar del
# elevador: Una cola por cada piso. Para subir al elevador, cada cola
# tiene un semáforo relacionado.
for i in pisos:
    colas[i] = {'num': 0, 'sem': Semaphore(0)}
    a_bordo[i] = []

def elevador():
    '''El elevador es el único hilo que se mantiene vivo durante toda la
    vida del sistema. Sube y baja por los pisos esperando encontrar
    alumnos (¡qué poca eficiencia energética!), y va despertando a los
    alumnos que hagan falta

    '''
    piso_actual = 0
    direccion = True # True = ↑, False = ↓
    while True:

        # Primero: Avanza al piso que le toca
        piso_prev = piso_actual
        sleep(freq_elev)

        # Registra los topes: Cambia de dirección al llegar al final
        # del recorrido
        if (direccion and piso_actual >= pisos[-1]) or (not direccion and piso_actual <= pisos[0]):
            direccion = not direccion

        # Avanza en la dirección correspondiente
        if direccion:
            piso_actual += 1
        else:
            piso_actual -= 1
        cprint('E: %d ⇒ %d' % (piso_prev, piso_actual), 'yellow')

        # Muestro el estado global del sistema sólo cuando piso==0 (para no saturar)
        if piso_actual == 0:
            estado_global()

        # Antes de entrar, deje salir: ¿Alquien tiene que bajar?
        puerta.acquire()
        while len(a_bordo[piso_actual]) > 0:
            # Sacamos al alumno de la cola destino, y lo despertamos gentilmente
            alum = a_bordo[piso_actual].pop()
            alum.release()

        # Si hay alumnos formado en la cola, despierta a los que pueda
        mut_colas.acquire()
        cprint('   %d alumnos formados, %d a bordo' % (colas[piso_actual]['num'], carga_total()), 'yellow')
        while carga_total() < carga_max and colas[piso_actual]['num'] > 0:
            colas[piso_actual]['sem'].release()
            colas[piso_actual]['num'] -= 1
            sleep(demora_puerta)
            if carga_total() > carga_max:
                cprint('Algo anda mal, muy mal. Carga total == %d' % carga_total(), 'yellow', 'on_red')
                sleep(1)
        puerta.release()
        mut_colas.release()

def alumno(num):
    '''Representa a cada uno de los alumnos. Elige un piso origen y
    destino al azar, se forma en la cola que le toca y se
    duerme. Cuando lo despiertan, sube al elevador, y se vuelve a
    dormir. Y cuando vuelve a despertar, ¡señal que ya llegó!

    '''
    desde = choice(pisos)
    hacia = choice(pisos)
    cprint('A%d: %d ⇒ %d' % (num, desde, hacia), 'green')
    if desde == hacia:
        cprint('A%d: Estoy donde quiero estar :-P' % (num), 'green')
        return True # Nada que hacer!

    # Se "apunta" en la cola que le corresponde y espera al elevador
    mut_colas.acquire()
    cprint('   A%d: A la cola %d (somos %d)' % (num, desde, colas[desde]['num']), 'green')
    colas[desde]['num'] += 1
    mut_colas.release()
    colas[desde]['sem'].acquire()

    # El elevador está aquí. Sube.
    cprint('   A%d. Tomo elevador %d → %d' % (num, desde, hacia), 'green')
    subir_elevador(num, hacia)

    # Llegamos a nuestro destino. Baja.
    cprint('   A%d. ¡Gracias elevador! 😉' % num, 'green')
    multiplex.release()

def subir_elevador(num, dest):
    '''Para subirse al elevador, un alumno agrega a la cola
    correspondiente un semáforo, y se duerme esperando a su llegada.

    '''
    multiplex.acquire()
    mi_dest = Semaphore(0)
    cprint('¡Pásele %d!' % (num), 'cyan')
    puerta.acquire()
    a_bordo[dest].append(mi_dest)
    puerta.release()
    mi_dest.acquire()

def carga_total():
    '''Reporta la carga total que tiene el elevador en un momento dado.

    Para dar resultados consistentes, se asume que el invocador tiene
    al mutex puerta.

    '''
    tot = 0
    for i in pisos:
        tot += len(a_bordo[i])
    return tot

def espera_total():
    '''Reporta el total de alumnos en espera por el elevador.

    Para dar resultados consistentes, se asume que el invocador tiene
    al mutex puerta.

    '''
    tot = 0
    for i in pisos:
        tot += colas[i]['num']
    return tot

def estado_global():
    '''
    Reporta el estado global del sistema: Cuántos alumnos están formados en cada cola
    '''
    puerta.acquire()
    carga = carga_total()
    espera = espera_total()

    cprint('===== Estado global del sistema: =====', 'white', 'on_blue')
    cprint('%d esperando por el elevador:' % (espera), 'green', 'on_blue')
    cprint("\t".join('  %d: %d' % (i, colas[i]['num']) for i in pisos), 'green', 'on_blue')
    cprint('A bordo (quedan %d lugares):' % (carga_max - carga), 'yellow', 'on_blue')
    cprint("\t".join('  %d: %d' % (i, len(a_bordo[i])) for i in pisos), 'yellow', 'on_blue')
    puerta.release()

Thread(target=elevador).start()

num = 0
while True:
    num += 1
    Thread(target=alumno, args=[num]).start()
    sleep(freq_alum)
