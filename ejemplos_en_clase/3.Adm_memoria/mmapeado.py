#!/usr/bin/python3
import mmap
from time import sleep
from os import getpid
from random import random

print('Soy el proceso %d' % getpid())
fh = open('/tmp/mmapeado', 'r+')
mm = mmap.mmap(fh.fileno(), 0)

mm[0:10] = bytes('Hola mundo', 'utf-8')
mm[15:27] = bytes('Mundoinmundo', 'utf-8')

num = 0

while True:
    mm[100:144] = bytes( 'Es el intento #%03d y mí aleatôrio es %1.3f' % (num, random()) ,
                         'utf-8' )
    num += 1
    sleep(3)
