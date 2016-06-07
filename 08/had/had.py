#!/usr/bin/python3.4
import had_lib
from glib import input_control
from random import randint

size = 10
souradnice = [[5,5]]
fruit = []
tah = 0

had_lib.nakresli_mapu(size,souradnice, tah, fruit)

while True:
    try:
        smer = input_control('s', 'Sever, jih, vychod nebo zapad? ',sever = 's', jih = 'j', vychod = 'v', zapad = 'z' )
        had_lib.pohyb(smer, souradnice, size, fruit)
        had_lib.nakresli_mapu(size, souradnice, tah, fruit)
        tah = tah + 1
    except ValueError:
        print('Game Over!')
        break

