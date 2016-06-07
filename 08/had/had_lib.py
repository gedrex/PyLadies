#!/usr/bin/python3.4
from random import randint
    
def nakresli_mapu(size, souradnice, tah, fruit):
    
    board = [] #hraci pole(seznam) a jeho definice
    for x in range(size):
        board.append(['.'] * size)

    #seznam poli v hracim poli(dvojice souradnic)
    board_net = []
    for x in range(size):
        for y in range(size):
            board_net.append([x, y]) 
    if len(fruit) < 1:
        ovoce(board, fruit)
    
    if tah % 30 == 0:
        ovoce(board, fruit)
    
    for bod in souradnice:
        board[bod[0]][bod[1]] = 'X'
    
    for kousek in fruit:
        board[kousek[0]][kousek[1]] = '?'
    
    print(board)
    for line in board:
        for l in line:
            print(l, end=' ')
        print()

def pohyb(smer, souradnice, size, fruit):
    if smer == 's':
        souradnice_new = [souradnice[-1][0]-1, souradnice[-1][1]]
    elif smer == 'j':
        souradnice_new = [souradnice[-1][0]+1, souradnice[-1][1]]
    elif smer == 'v':
        souradnice_new =[souradnice[-1][0], souradnice[-1][1]+1]
    elif smer == 'z':
        souradnice_new = [souradnice[-1][0], souradnice[-1][1]-1]
    
    if souradnice_new[0] in range(0, size) and souradnice_new[1] in range(0, size) and souradnice_new not in souradnice:
        souradnice.append(souradnice_new)
        if souradnice_new in fruit:
            del fruit[fruit.index(souradnice_new)]
        else:
            del souradnice[0]
    else:
        raise ValueError

def ovoce(board, fruit):
    i = 0
    while i<30:
        x = randint(0, len(board)-1)
        y = randint(0, len(board)-1)
        if board[x][y] == '.':
            fruit.append([x,y])
            break
        else:
            i = i + 1
