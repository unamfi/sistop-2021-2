#importations
from time import sleep  #Generate sleep btw threads
from random import randint #generate random integer
from threading import Semaphore, Thread #Threads and semaphores

#global vars initialization
#Reigndeers
total_reigndeers=0
reigndeers= 10
reigndeersWorking= 10
reigndeersSemaphore= Semaphore(0)
reigndeersMutex= Semaphore(1)
#Elves
mutexElves= Semaphore(1)
elfSemaphore= Semaphore(0)
elves= 300
elvesInCharge= 5
totalElves=0
#Santa's wake up semaphore and gifts
delivered_gifts = True
wakeUpSanta= Semaphore(0)

#FUNCTIONS OF PARTICIPANTS
def Reigndeer(i):
    global total_reigndeers,delivered_gifts
    deerSlave= 'Im not a slave anymore!!. Reigndeer  number: {}, is on vacations, BYE.'.format(i)
    print(deerSlave)
    vacationDuration= randint(15,60)
    sleep(vacationDuration)
    print('Reigndeer number: {}, is back!'.format(i))
    reigndeersMutex.acquire()
    total_reigndeers+=1

    while total_reigndeers==reigndeersWorking:
        x=1
        while x<reigndeersWorking:
           reigndeersSemaphore.release()
           x+=1
        total_reigndeers=0
    delivered_gifts=False
    reigndeersSemaphore.acquire()
    reigndeersMutex.release()
    wakeUpSanta.release()
    
    
def Elves(i):
    global elves
    print ('Elve number: {}, working on the stuff'.format(i))
    totalProblems=randint(5,20)
    sleep(totalProblems)
    print('Time to work!! Elve number: {}adquire stuff'.format(i))
    mutexElves.acquire()
    totalElves+=1

    print('Total of elves working: {}'.format(totalElves))

    if totalElves==elvesInCharge:
        for x in range (1,elvesInCharge):
            elfSemaphore.release()
        totalElves=0
        print('Theres {} elves working'.format(elvesInCharge))
        wakeUpSanta.release()
    mutexElves.release()
    elfSemaphore.acquire()

def PapaNoel():
    wakeUpSanta.acquire() #Santa's semaphore in order to get the flag.
    while True: 
        job='Santa helps elves with the gifts' if delivered_gifts==True else  'Total of reigndeers: {}, Santa is on the road '.format(reigndeersWorking)
        print(job)
        wakeUpSanta.acquire() #increment semaphore
        break
    print('Santa is done')



#Threads and initializations
#Santa's thread
t= Thread(target=PapaNoel)  
t.start()
#Elves Thread
z=0
while z<elves:
    t=Thread(target = Elves, args = [l]).start()
    z+=1
#Reigndeers thread
y=0
while y< reigndeers:
    t= Thread(target =Reigndeer, args = [k]).start()
    y+=1

