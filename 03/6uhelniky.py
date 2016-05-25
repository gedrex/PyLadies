#!/usr/bin/python3.4

from turtle import shape, forward, left, right, color, exitonclick, penup, pendown

shape('turtle')
color('red')

for i in range(6):
    for x in range(6):
        forward(50)
        left(60)
    forward(50)
    right(60)
    
exitonclick()
