from threading import Semaphore, Thread
from random import randint
from time import sleep

int elfos = 0 
int reno = 0 
semaphore santaSem = 0
semaphore renoSem = 0
semaphore elfTex = 1
semaphore mutex = 1

#Definir santa
def santa():
    
while(true){
    wait(papaSem);
    wait(mutex);
        if (reno >= 9)
            prepararTrineo();
            print ("han llegado {} renos")
            signal(renoSem,9);
            reno -= 9;
        else (if elfos == 3)
            ayudarElfos();
            print ("santa ha ayudado {} de 3 elfos")
    signal(mutex);
}

#Definir reno
def reno ():
while (true){
    wait(mutex);
        reno += 1;
        if (reno == 9)
            signal(papaSem);
    signal(mutex)
    wait(renoSem);
    obtenerRienda();
}

#Definir elfos
def elfo ():
while(true){
    wait(elfTex);
    wait(mutex);
        elfos += 1;
        if (elfos ==3)
            signal(papaSem)
        else
            signal(elfTex);
        signal(mutex);
        obtenerAyuda();
        wait(mutex);
            elfos -= 1;
            if (elfos == 0)
                signal(elfTex);
        signal(mutex);       
}


