from threading import Semaphore, Thread
from time import sleep 
from random import randint

#Hilo de alumno.
def alumno(id):
	preguntas_totales = randint(1,y) #Número de preguntas que tiene el alumno. 
	num_pregunta = 1 #Contador del numero de pregunta.
	cubiculo.acquire() #Entra al cubiculo.
	print("El alumno {} ha entrado al cubículo. Tiene {} pregunta(s).".format(id, preguntas_totales))
	while(num_pregunta < preguntas_totales+1):
		capacidad.acquire() #Proceso de pregunta/respuesta.
		atencion.acquire() #Guarda las preguntas que se le formulan.
		print("El alumno {} hace la pregunta {}.".format(id, num_pregunta));
		preguntas.append(id)
		preguntas.append(num_pregunta)
		atencion.release()
		pregunta.release() #Pone al tanto al asesor de que se hizo una pregunta.
		num_pregunta += 1
		sleep(0.2) #Se simula el tiempo que tarda en pensar que otra pregunta le hará al asesor.
	print("El alumno {} sale del cubiculo.".format(id))
	cubiculo.release() #Sale del cubiculo.
	
def asesor():
	while(True):
		print("El asesor espera.")
		pregunta.acquire() #Espera a que hayan hecho una pregunta.
		atencion.acquire() #Comienza a responder las preguntas.  
		alumno_id = preguntas.pop(0)
		num_pregunta = preguntas.pop(0)
		print("El asesor responde la pregunta {} del alumno {}.".format(num_pregunta,alumno_id))
		atencion.release() #Termina de responder
		capacidad.release() #Libera el proceso de pregunta/respuesta

x = int(input("Ingresar el número máximo de alumnos permitidos en el cubículo: ")) #Número máximo de alumnos en el cubículo.
y = int(input("Ingresar el número máximo de preguntas por alumno: ")) #Número máximo de preguntas por alumno.
num_alumnos = int(input("Ingrese el número de alumnos que buscan asesoría: ")) #Número total de alumnos que se simularán.
preguntas = [] #Lista que almacena la pregunta (id y numero de pregunta).

cubiculo = Semaphore(x) #Multiplex de capacidad del cubículo.
atencion = Semaphore(1) #Mutex de preguntas.
pregunta = Semaphore(0) #Indica que se ha hecho una pregunta.
capacidad = Semaphore(1) #Mutex del proceso pregunta-respuesta.


#Se inicia un hilo de asesor
t_asesor = Thread(target = asesor)
t_asesor.start()

#Se inician los hilos de alumnos
for i in range(1,num_alumnos+1):
	t_alumnos= Thread(target = alumno, args = [i])
	t_alumnos.start()