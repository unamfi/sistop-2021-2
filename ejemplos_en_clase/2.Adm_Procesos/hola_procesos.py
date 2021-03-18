#!/usr/bin/python3





from os import fork
from time import sleep

mi_nombre = "Primer programa que maneja procesos"
ultimo_en_entrar = None
contador = 0

def aumenta_contador(id):
    global contador, ultimo_en_entrar
    sleep(0.1)
    ultimo_en_entrar = id
    print("Voy entrando a mi función contador. Mi ID es ", id)
    contador = contador + 1
    print("Y el contador ahora es: ", contador)
    print('El último en entrar fue: ', ultimo_en_entrar)


for i in range(5):
    pid = fork()
    if pid == 0:
        aumenta_contador(i)
        exit(0)
    else:
        # Proceso padre. No hace nada.
        pass

sleep(1)
exit(0)
