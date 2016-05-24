#!/usr/bin/python3.4
from glib import input_control

###
old_file = input('Zadej jmeno souboru v aktualnim adresari, ktery chces zkopirovat, vcetne koncovky: ')
if old_file:
    try:
        with open(old_file, encoding='utf-8') as temp_data:
            temp_data = temp_data.read()
    except FileNotFoundError:
        old_file = input('Takovy soubor neexistuje. Zadej jmeno existujiciho souboru vcetne koncovky: ')
    else:
        old_file = old_file

with open(old_file, encoding='utf-8') as old_file:
    file_for_write = open(input('Zadej jmeno noveho souboru: '), 'a')
    file_for_write.write(old_file.read())
    file_for_write.close()
