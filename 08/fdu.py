#!/usr/bin/python3.4
from glib import input_control

def animals_list(file_name):
    """
    Načte soubor slova.txt, ve kterém jsou slova k hádání, očistí je o mezery před a za slovy a o odřádkování a vrátí seznam slov
    """
    with open(file_name, encoding='utf-8') as words_file:
        words = []
        for word in words_file:
            word = word.replace('\n', '')
            word = word.strip()
            words.append(word)
    while '' in words:
        words.remove('')

    return words

def shorter_then_5(words):
    return [word for word in words if len(word)<5]

def starting_with_k(words):
    return [word for word in words if word.startswith('k')]

def if_is_in_list(words, users_word):
    if users_word in words:
        return True
    else:
        return False

def two_lists(list1, list2):
    complete_list = [[],[],[]]
    complete_list[0].extend([list2_item for list2_item in list2 if list2_item in list1])
    complete_list[1].extend([list1_item for list1_item in list1 if list1_item not in list2])
    complete_list[2].extend([list2_item for list2_item in list2 if list2_item not in list1])
    return complete_list

def sort_animals(animals):
    return sorted(animals, key=str.lower)

def sort_animals2(animals):
    list_of_pairs = []
    list_of_pairs.extend([animal[1], animal] for animal in animals)
    list_of_pairs.sort()
    
    return [value[1] for value in list_of_pairs]

print(shorter_then_5(animals_list('zviratka.txt')))
print(starting_with_k(animals_list('zviratka.txt')))
print(if_is_in_list(animals_list('zviratka.txt'), 'had'))
print(two_lists(animals_list('zviratka.txt'), animals_list('zviratka2.txt')))
print(sort_animals(animals_list('zviratka2.txt')))
print(sort_animals2(animals_list('zviratka2.txt')))
