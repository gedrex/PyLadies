#!/usr/bin/python3.4

from turtle import forward, left, exitonclick

#n = pocet uhlu
n = int(input('zadej pocet uhlu:\n'))
#rozestup mezi carami ornamentu
rozestup = int(input('zadej rozestup: \n'))

#a = delka strany
a = 200/n

#r = polomer otocky
r = 180 - (180 * (1 - (2/n)))

for x in range(12):
    for i in range(n):
        a = a + rozestup
        forward(a)
        left(r)

exitonclick()
