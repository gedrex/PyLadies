#!/usr/bin/python3.4

from turtle import forward, left, exitonclick

#n = pocet uhlu
n = 12
#rozestup mezi carami ornamentu
rozestup = int(input('zadej rozestup: \n'))

#a = delka strany
a = 50/n

#r = polomer otocky
r = 180 - (180 * (1 - (2/n)))

for x in range(6):
    for i in range(n):
        a = a + (rozestup/n)
        forward(a)
        left(r)

exitonclick()
