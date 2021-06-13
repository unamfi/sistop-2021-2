#!/usr/bin/python3
from threading import Semaphore, Thread
from time import sleep
from random import random

num_hilos = 10
cuenta = 0
mutex = Semaphore(1)
barrera = Semaphore(0)


def vida_del_hilo(id):
    global cuenta
    print('El hilo %d entra...' % id)

    mutex.acquire()
    cuenta = cuenta + 1

    if cuenta == num_hilos:
        barrera.release()
        print('Se abre la barrera!')
    mutex.release()

    sleep(random())

    barrera.acquire()
    barrera.release()

    print('El hilo %d terminó su procesamiento.' % id)

for i in range(20):
    Thread(target=vida_del_hilo, args=[i]).start()
