#!/usr/bin/python3.4

from turtle import penup, pd, ht, st, pos, setpos, circle, begin_fill, end_fill, right, left, fd, color, heading, exitonclick, screensize, pensize
from random import randint

number = int(input('num: '))
def sphere1(num):
    color('red')
    for i in range(num*4):
        circle(50, (180+(180/num)))
        right(90+(360/num))

def sphere2(num):
    for i in range(num*4):
        for x in range(4):
            fd(40)
            right(180/num)
        right(270/num)
setpos(-150,50)
sphere1(number)
setpos(50,-50)      
sphere2(number)

exitonclick()
