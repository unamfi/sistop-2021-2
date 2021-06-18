# from time import sleep
from threading import Thread, Semaphore
from random import randint, choice

number_of_cats = 2
number_of_mice = 200
number_of_bowls = 15

mice_in_eating_zone = []
cats_in_eating_zone = []

mice_in_eating_zone_access = Semaphore(1)
cats_in_eating_zone_access = Semaphore(1)

permission_to_bowls = [Semaphore(1) for _ in range(number_of_bowls)]

permission_to_leave_for_cats = Semaphore(1)
permission_to_enter_for_cats = Semaphore(1)

permission_to_queue_up_for_bowl_zone = Semaphore(1)

def cat(id):

    while True:

        permission_to_queue_up_for_bowl_zone.acquire()

        permission_to_enter_for_cats.acquire()
        cats_in_eating_zone_access.acquire()
        cats_in_eating_zone.append(id)
        print(f'Gato {id} está entrando a zona de platos')
        cats_in_eating_zone_access.release()
        permission_to_enter_for_cats.release()

        permission_to_queue_up_for_bowl_zone.release()

        bowl_choice_index = randint(0, number_of_bowls - 1)
        permission_to_bowl = permission_to_bowls[bowl_choice_index]
        permission_to_bowl.acquire()
        print(f'Gato {id} está comiendo de plato {bowl_choice_index}')
        print(f'Gato {id} terminó de comer de plato {bowl_choice_index}')
        permission_to_bowl.release()

        permission_to_leave_for_cats.acquire()
        cats_in_eating_zone_access.acquire()
        cats_in_eating_zone.remove(id)
        print(f'Gato {id} está dejando la zona de platos')
        cats_in_eating_zone_access.release()
        permission_to_leave_for_cats.release()


def mouse(id):

    caught_by_cat = False
    predator_cat = None

    while not caught_by_cat and not predator_cat:

        permission_to_queue_up_for_bowl_zone.acquire()
        permission_to_queue_up_for_bowl_zone.release()

        mice_in_eating_zone_access.acquire()
        if len(mice_in_eating_zone) == 0:
            permission_to_enter_for_cats.acquire()
            permission_to_leave_for_cats.acquire()
        cats_in_eating_zone_access.acquire()
        if len(cats_in_eating_zone) > 0:
            caught_by_cat = True
            predator_cat = choice(cats_in_eating_zone)
        cats_in_eating_zone_access.release()
        mice_in_eating_zone.append(id)
        print(f'Ratón {id} está entrando a zona de platos')
        mice_in_eating_zone_access.release()

        bowl_choice_index = randint(0, number_of_bowls - 1)
        permission_to_bowl = permission_to_bowls[bowl_choice_index]
        permission_to_bowl.acquire()
        print(f'Ratón {id} está comiendo de plato {bowl_choice_index}')
        print(f'Ratón {id} terminó de comer de plato {bowl_choice_index}')
        permission_to_bowl.release()

        mice_in_eating_zone_access.acquire()
        mice_in_eating_zone.remove(id)
        if caught_by_cat:
            print(f'Ratón {id} murió a garras de Gato {predator_cat}')                                                       
        else:
            print(f'Ratón {id} está dejando la zona de platos')
        if len(mice_in_eating_zone) == 0:
            permission_to_enter_for_cats.release()
            permission_to_leave_for_cats.release()
        mice_in_eating_zone_access.release()


    
## Cuando hilos ratones empiezan primero
## Nótese que no hay inanición

for id in range(number_of_mice):
    Thread(target = mouse, args = [id]).start()

for id in range(number_of_cats):
    Thread(target = cat, args = [id]).start()



# ### Cuando hilos gatos empiezan primero

# for id in range(number_of_mice):
#     Thread(target = mouse, args = [id]).start()

# for id in range(number_of_cats):
#     Thread(target = cat, args = [id]).start()



# ### Cuando hilos gatos y ratones se inician a la par

# greater_number_of_animals = (
#     number_of_cats 
#     if number_of_cats > number_of_mice 
#     else number_of_mice
# )

# for id in range(greater_number_of_animals):
#     if id <= number_of_mice:
#         Thread(target = mouse, args = [id]).start()
#     if id <= number_of_cats:
#         Thread(target = cat, args = [id]).start()