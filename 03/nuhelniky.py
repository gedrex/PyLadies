#!/usr/bin/python3.4
from turtle import forward, left, exitonclick

#n = pocet uhlu
n = int(input('zadej pocet uhlu:\n'))

#a = delka strany
a = 500/n

#r = polomer otocky
r = 180 - (180 * (1 - (2/n)))

for i in range(n):
    forward(a)
    left(r)

exitonclick()

