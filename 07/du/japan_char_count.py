#!/usr/bin/python3.4

katakana_count = 0
hiragana_count = 0

#otevre soubor katakana.txt, ulozi abecedu oklestenou o odradkovani do promenne katakana
with open('katakana.txt', encoding='utf-8') as katakana:
    katakana = katakana.read().replace('\n', '')

#otevre soubor hiragana.txt, ulozi abecedu oklestenou o odradkovani do promenne hiragana
with open('hiragana.txt', encoding='utf-8') as hiragana:
    hiragana = hiragana.read().replace('\n', '')

#otevre soubor rozsypanycaj.txt, ulozi abecedu oklestenou o odradkovani do promenne rozsypanycaj
with open('rozsypanycaj.txt', encoding='utf-8') as rozsypanycaj:
    rozsypanycaj = rozsypanycaj.read()

#do promenne katakana_count uozi pocet vyskytu kazdeho znaku katakana v souboru rozsypanycaj, pricte k ostatnim a vypise
for char in katakana:
    katakana_count = katakana_count + rozsypanycaj.count(char)

print('Počet znaků katakana v textu je:', katakana_count)

#do promenne hiragana_count uozi pocet vyskytu kazdeho znaku katakana v souboru rozsypanycaj, pricte k ostatnim a vypise
for char in hiragana:
    hiragana_count = hiragana_count + rozsypanycaj.count(char)

print('Počet znaků hiragana v textu je:', hiragana_count)
