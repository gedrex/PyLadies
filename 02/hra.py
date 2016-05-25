#!/usr/bin/python3.4

#import of python functions from libs
from random import randrange

#man input from keyboard
man_turn = input('co hrajes? kamen, kuzky nebo papir? ')

#check if man input is valid
valid_string = man_turn == 'kamen' or man_turn == 'nuzky' or man_turn == 'papir'

if valid_string:
    #random number from 0 to 3 and it's set to string value
    pc_turn = randrange(3)
    if pc_turn == 0:
        pc_turn = 'kamen'
    elif pc_turn == 1:
        pc_turn = 'nuzky'
    else:
        pc_turn = 'papir'
    #comparation of choices 
    if man_turn == pc_turn:
        print("PC has \'" + pc_turn + "\' as well, it's a Match...")
    elif (man_turn == 'kamen' and pc_turn == 'nuzky') or (man_turn == 'nuzky' and pc_turn == 'papir') or (man_turn == 'papir' and pc_turn =='kamen'):
        print("PC has \'" + pc_turn + "\'. You win!")
    else:
        print("PC has \'" + pc_turn + "\'. You lost")
else:
    print('bad input, try it again')
