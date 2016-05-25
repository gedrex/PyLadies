#!/usr/bin/python3.4

from turtle import heading, shape, forward, left, right, color, exitonclick, penup, pendown, begin_fill, end_fill, circle

#zelvicka namaluje cervenou kyticku se stonkem a listecky
#zelvicka jede nahoru, aby udelala misto pro kyticku
shape('turtle')
color('red')
penup()
left(90)
forward(150)
right(90)
pendown()

#zelvicka dela ctverecky a z nich vybarvi kvitecek
begin_fill()
for i in range(18):
    for x in range(4):
        forward(50)
        left(90)
    left(20)
end_fill()

#zelvicka meni barvu na zelenou a jde delat stonek
color('green')
right(90)
penup()
forward(66)
pendown()
forward(50)
#zelvicka si vybira sklon, pocet a delku prvniho listku
sklon_listku = 24
pocet_listku = 7
delka_listku = 12

#a zelvicka jde malovat listecky

for listek in range(pocet_listku):
    delka_listku = delka_listku+listek
    strana_listku = listek%2
    left(180)
    
    #zelvicce zalezi na tom, jestli je to prava nebo leva strana stonku.
    if strana_listku > 0:
        right(sklon_listku)
        begin_fill()
        for i in range(2):
            for x in range(delka_listku):
                forward(3)
                right(2)
            #zelvicka si uvedomuje, kam smeruje a podle toho se otaci
            right(heading()+sklon_listku+90)
        end_fill()
        left(270-heading())
    else:
        left(sklon_listku)
        begin_fill()
        for i in range(2):
            for x in range(delka_listku):
                forward(3)
                left(2)
            left(270-heading()+sklon_listku)
        end_fill()
        right(heading()-270)
    forward(25)


exitonclick()
