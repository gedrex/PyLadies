#!/usr/bin/python3.4

from glib import input_control
from futils import * 
from pictures_lib import fault

print('Zahrej si Šibenici. Uhodni písmenko ve slově: \n \n')

word = chosen_word()
blind_char = '-'
starting_board = len(word)*blind_char
miss = 0

def game(word, miss, board):
    while blind_char in board:
        print('slovo: ', board)
        player_choice = input_control('s', 'Zvol si písmeno: ', 1)
        
        correct = is_right(player_choice, word)
        
        if correct:
            board = change_board(correct, player_choice, board)
        else:
            miss = miss + 1
            print(fault(miss-1)+'\n') 
        if miss > 9:
            print('\033[1;41mVisíš!! Konec hry.\033[1;m')
            print('Správné slovo bylo:\033[1;31m', word, '\033[1;m')
            break
    else:
        print('\033[1;42mVyhrál jsi!!!\033[1;m')

game(word,miss,starting_board)
