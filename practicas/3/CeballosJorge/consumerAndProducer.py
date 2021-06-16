"""
Problema productor-consumidor
Programa que ejecuta la el proceso de productor-consumidor
Las labores de cada una son las siguientes:
productor: generar un producto, almacenarlo y comenzar nuevamente;
El productor no debe añadir más productos que la capacidad del buffer
consumidor: toma  simultaneamente productos uno a uno.
el consumidor no debe intentar tomar un producto si el buffer está vacío.
"""
import time
import queue
import random
import logging
import threading

logging.basicConfig(level=logging.DEBUG, format='%(threadName)s: %(message)s',)
queue = queue.Queue(maxsize=5)

def producer():
    while True:
        if not queue.full():
            item = random.randint(1, 10)
            queue.put(item)

            logging.info(f'Nuevo elemento dentro de la cola {item}')

            time_to_sleep = random.randint(1, 3)
            time.sleep(time_to_sleep)

def consumer():
    while True:
        if not queue.empty():
            item = queue.get()
            queue.task_done()

            logging.info(f'Nuevo elemento obtenido {item}')

            time_to_sleep = random.randint(1, 3)
            time.sleep(time_to_sleep)

if __name__ == '__main__':
    thread_producer = threading.Thread(target=producer)
    thread_consumer = threading.Thread(target=consumer)

    thread_producer.start()
    thread_consumer.start()