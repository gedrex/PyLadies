#!/usr/bin/python3.4
from random import randrange
from pictures_lib import *

def words_list():
    """
    Načte soubor slova.txt, ve kterém jsou slova k hádání, očistí je o mezery před a za slovy a o odřádkování a vrátí seznam slov
    """
    with open('slova.txt', encoding='utf-8') as words_file:
        words = []
        for word in words_file:
            word = word.replace('\n', '')
            word = word.strip()
            words.append(word)
    while '' in words:
        words.remove('')

    return words

def chosen_word():
    """
    Ze seznamu slov vybere nahodne jedno a vrati ho ve forme retezce
    """
    words = words_list()
    if len(words)<2:
        return words[0]
    else:
        return words[randrange(len(words)-1)]

def is_right(char, word):
    """
    funkce si bere pismeno ze zadani od uzivatele a porovnava ho s pismeny ve vybranem slove. Pokud je spravne, vrati index pismene ve slove + 1(pokud je to nula, je to jako by to vracelo False, v dalsim kodu se s tim musi pocitat). Pokud je spatne, vyhodi False
    """
    if char in word:
        return word.index(char)+1
    else:
        return False

def change_board(position, char, board):
    """
    podle zadane pozice zmeni pismenko v retezci board na zadane hracem
    """
    correct = position - 1
    return board[:correct]+char+board[correct+1:]
