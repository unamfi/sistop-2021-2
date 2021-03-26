#!/usr/bin/python3

from signal import *


def manejador(señal, frame):
    print('Recibí la señal %d...' % señal)
    print('... ¡Y no me morí!')

def paso_tu_tiempo(señal, frame):
    print('... Tiempo terminado. ¡Cháu!')
    exit(0)

signal(SIGINT, manejador)

signal(SIGALRM, paso_tu_tiempo)
alarm(5)

while True:
    pass
