#!/usr/bin/python3.4

from turtle import forward, left, right, exitonclick, penup, pendown
from math import sqrt

#a = delka steny domecku
a = 90
#c = delka prepony
c = sqrt(2)*a


#prejeti na levou cast
penup()
left(180)
forward(200)
left(180)
pendown()

for x in range(5):

    #domecek
    for i in range(4):
        forward(a)
        left(90)
    left(45)
    forward(c)
    for i in range(2):
        left(90)
        forward(c/2)
    left(90)
    forward(c)

    left(45)
    penup()
    forward(15)
    pendown()

exitonclick()
