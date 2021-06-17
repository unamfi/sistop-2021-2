import threading
import random
import time
import random

def alumno(id):
	while True:
		#El multiplex cubiculo permite que solo 6 alumnos entren al cúbiculo
		cubiculo.acquire()
		#Generamos el número de dudas desde 1 hasta 3 usando la funcion randint 
		dudas = random.randint(1,4)
		#mutex alumno protege al arreglo de alumnos con dudas
		mutex_alumnos.acquire()
		#Se agrega el alumno al arreglo de alumnos con dudas
		alumnos_con_dudas.append(id)
		print("Hola soy %d, tengo %d dudas y estoy entrando al salon... Hay %d alumnos en el salon" %(id,dudas,len(alumnos_con_dudas)))
		#Condicion de que hay mínimo un alumno con dudas
		if len(alumnos_con_dudas)==1: 
			print("Despertando profesor")
			#Señal para despertar al asesor
			despertar_asesor.release()
		mutex_alumnos.release()
		while dudas !=0:
			#Se espera la señal de que el asesor pueda responder mi duda
			responder.acquire()
			#Una vez contestada se resta el número de dudas
			dudas = dudas - 1
			print("Hola soy %d y me quedan %d " %(id,dudas))
			if dudas==0:
				#Si el alumno ya no tiene dudas, se elimina del arreglo y avisa que está saliendo del cúbiculo
				alumnos_con_dudas.remove(id)
				print("Soy %d y estoy saliendo del salon... Hay %d alumnos en el salon" %(id,len(alumnos_con_dudas)))
				break;
			#Debe esperar a que se les responda a los demás alumnos 
			time.sleep(len(alumnos_con_dudas))
		#Sale del cubiculo y deja libre un lugar
		cubiculo.release()
		break;

def asesor():
	while True:
		#Esperamos la señal de que hay un alumno con dudas esperando 
		despertar_asesor.acquire()
		print("Respondiendo dudas")
		#Enviamos la señal de que puede responder una duda 
		responder.release()
		while len(alumnos_con_dudas)!=0:
			#Tiempo que se tarda en responder una duda
			time.sleep(1)
			print("Respondi una pregunta")
			#Enviamos la señal de que puede responder otra duda
			responder.release()
		print("No hay alumnos, me voy a dormir")

#Multiplex de maximo de alumnos en el salor
cubiculo = threading.Semaphore(6) 
#Mutex para proteger al arreglo alumnos_con_dudas
mutex_alumnos = threading.Semaphore(1)
#Señal para avisar que el asesor puede responder una duda
despertar_asesor = threading.Semaphore(0)
#Arreglo de alumnos con dudas
responder = threading.Semaphore(0)
#Señal para despertar al asesor
alumnos_con_dudas = []
#Número máximo de alumnos 
num_alumnos = 12

threading.Thread(target=asesor).start()
for alumno_id in range(num_alumnos):
    threading.Thread(target=alumno, args=[alumno_id]).start()
