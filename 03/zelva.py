#!/usr/bin/python3.4

from turtle import shape, forward, left, color, exitonclick, penup, pendown

shape('turtle')
color('red')

for i in range(3):
    for x in range(4):
        forward(90)
        left(90)
    left(20)
exitonclick()
