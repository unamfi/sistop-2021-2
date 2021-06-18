# -*- coding: utf-8 -*-
"""
@author: anita
"""
from threading import Thread, Semaphore
from time import sleep
import random

y = random.randint(1,7)
x = random.randint(2,10)

       
class alumno(Thread):
    def __init__(self, id, alumnos_cub, Sentrada = None, Spregunta = None, Srespuesta = None, Mpregunta = None):
        Thread.__init__(self)
        self.id = id
        self.alumnos_cub = alumnos_cub
        self.y_pregunta = ["Pregunta "+str(i) for i in range(y)]
        self.Sentrada = Sentrada
        self.Spregunta = Spregunta
        self.Srespuesta = Srespuesta
        self.Mpregunta = Mpregunta
        
    def preguntar(self):
        sleep(3.0)
        pregunta = self.y_pregunta.pop()
        with self.Mpregunta:
            sleep(0.5)
            print("El alumno %i hace una pregunta: %s" %(self.id, pregunta))
            self.Spregunta.release()
            print("El alumno %i está en espera de una respuesta" %(self.id))
            self.Srespuesta.acquire()
    
    def entrar(self):
        num_preguntas = len(self.y_pregunta)
        self.alumnos_cub.append(self.id)
        print("El alumno %i quiere entrar al cubículo" %(self.id))
        with self.Sentrada:
            print(("El alumno %i entró al cubículo y tiene %i preguntas \n"+"Hay %i alumnos en el cubículo")%(self.id, num_preguntas, len(self.alumnos_cub)))
            t_list = []
            for _ in range(num_preguntas):
                t = Thread(target=self.preguntar)
                t_list.append(t)
                t.start()
            for t in t_list:
                t.join()
                self.alumnos_cub.remove(self.id)
                print(("Al alumno %i ya se le respondieron todas las preguntas \n"+"Quedan %i en el cubículo")%(self.id,len(self.alumnos_cub)))
     
    def run(self):
        Thread(target=self.entrar).start()
        
class profesor(Thread):
    def __init__(self, Sentrada = None, Spregunta = None, Srespuesta = None, Mpregunta = None):
        Thread.__init__(self)
        
        self.Sentrada = Sentrada
        self.Spregunta = Spregunta
        self.Srespuesta = Srespuesta
        self.Mpregunta = Mpregunta
    
    def responder(self):
        print("El profesor está en espera de una pregunta")
        self.Spregunta.acquire()
        self.Srespuesta.release()
        print("\nEl profesor ha respondido")
        
    def inicio(self):
        print("El profesor ha despertado");
        print("El profesor empezará a responder")
        while True:
            self.responder()
    
    def run(self):
        Thread(target=self.inicio).start()
        
        
class Cubiculo():
    def __init__(self, x_sillas=x,x_alumnos=x):
        Thread.__init__(self)
        
        self.x_sillas = x_sillas     #Cantidad de sillas
        self.x_alumnos = x_alumnos   #Cantidad de alumnos
        self.alumnos_cub = []      #Alumnos en el cubículo
        
        self.Sentrada = Semaphore(x_sillas)
        self.Spregunta = Semaphore(0)
        self.Srespuesta = Semaphore(0)
        self.Mpregunta = Semaphore(1)
        
        self.alumnos = [alumno(id = i, alumnos_cub = self.alumnos_cub, Sentrada = self.Sentrada,Spregunta = self.Spregunta,Srespuesta = self.Srespuesta,Mpregunta=self.Mpregunta)for i in range(x_alumnos)]
                                       
        self.profesor = profesor(Sentrada = self.Sentrada,Spregunta = self.Spregunta,Srespuesta = self.Srespuesta,Mpregunta=self.Mpregunta)                      
        
    def asesoria(self):
        print("El profesor está tomando una siesta ya que el cubículo está vacío")
        self.profesor.start()
        for alumno in self.alumnos:
            sleep(0.5)
            alumno.start()

def main():
    Cubiculo().asesoria()
    
main()