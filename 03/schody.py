#!/usr/bin/python3.4

from turtle import shape, forward, left, right, color, exitonclick, penup, pendown

shape('turtle')
color('red')

for i in range(10):
    for x in range(4):
        forward(50)
        left(90)
        forward(50)
        right(90)
exitonclick()
