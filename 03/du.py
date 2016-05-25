#!/usr/bin/python3.4

from turtle import penup, pd, ht, st, pos, setpos, circle, begin_fill, end_fill, right, left, fd, color, heading, exitonclick, screensize, pensize
from random import randint

"""
zelvicka co kresli nahodne na platno nahodne tvary, v nahodnych barvach a nahodnych velikostech na nahodne pozice v nahodnem uhlu
"""
#otazka na pocet tvaru na platne s kontrolou spravnosti
shapes_count = input('Kolik má želvička vykreslit tvarů od 1 do 25? ')

while not shapes_count.isnumeric():
    shapes_count = input('Tak znova. Kolik tvarů od 1 do 25? ')

while shapes_count.isnumeric():
    if 0 < int(shapes_count) < 26:
        shapes_count = int(shapes_count)
        break
    else:
        shapes_count = input('Tak znova. Kolik tvarů od 1 do 25? ')
    
#Barvy ktere zelvicka pouzije v seznamu
colors = ['red', 'green', 'blue', 'yellow', 'orange', 'violet']

#zelvicka si zjisi maximalni a minimalni pozici, na ktere muze zacit malovat, schova se a zvedne pripravene pero
screen_size = screensize()
ht()
penup()
#maximalni souradnice, na ktere muze zelvicka malovat, aby nezacala malovat az uplne do kraje nebo nekam za platno
max_x = (screen_size[0]/2)-10
max_y = (screen_size[1]/2)-10

for i in range(shapes_count): #pocet tvaru na platne
    #zelvicka si zvoli nahodnou pozici v ramci platna. Pokud je za hranici platna, zvoli nahodny bod znovu.
    x_position = randint(-max_x, max_x)
    y_position = randint(-max_y, max_y)
    while not -max_x < x_position < max_x:
        x_position = randint(-max_x, max_x)
    while not -max_y < y_position < max_y:
        y_position = randint(-max_y, max_y)
        
    setpos(x_position, y_position) #zelvicka jde na urcenou pozici
    #zelvicka si zvoli nahodnou z 6ti tvaru, barvu a velikost
    shape = randint(0,5)
    color(colors[randint(0,5)])
    size = randint(1,6)
    begin_fill() 
    st() 
    pd() 
    if shape == 0: #kolecko
        circle(size*5)
    elif shape == 1: #ctverecek
        strana = size*5
        for i in range(4):
            fd(strana)
            right(90)
    elif shape == 2: #trojuhelnik
        strana = size*5
        for i in range(3):
            fd(strana)
            right(120)
    elif shape == 3: #spirala
        pen_size = randint(1,6)
        pensize(pen_size)
        end_fill()
        n = size+20
        a = 50/n
        for x in range(randint(1,5)):
            for i in range(n):
                a = a + (pen_size/n)
                fd(a)
                left(180 - (180 * (1 - (2/n))))
        begin_fill()
        pensize(1)
    elif shape == 4: #hvezdicka
        strana = size*10
        for i in range(7):
            fd(strana)
            left(180-(180/7))
    else: # slunicko
        pozice = pos()
        velikost = 10+size
        for i in range(18):
            circle(10+velikost, -120)
            setpos(pozice)
            left(20)
    end_fill()    
    penup()
    ht()
    right(randint(0,180)) #zelvicka se otoci do nahodneho uhlu

exitonclick()

