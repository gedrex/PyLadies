#!/usr/bin/python3.4

katakana_count = 0
hiragana_count = 0
with open('katakana.txt', encoding='utf-8') as katakana:
    katakana = katakana.read().replace('\n', '')

with open('hiragana.txt', encoding='utf-8') as hiragana:
    hiragana = hiragana.read().replace('\n', '')

with open('rozsypanycaj.txt', encoding='utf-8') as rozsypanycaj:
    rozsypanycaj = rozsypanycaj.read()

for char in katakana:
    katakana_count = katakana_count + rozsypanycaj.count(char)

print('Počet znaků katakana v textu je:', katakana_count)
for char in hiragana:
    hiragana_count = hiragana_count + rozsypanycaj.count(char)

print('Počet znaků hiragana v textu je:', hiragana_count)
