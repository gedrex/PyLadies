#!/usr/bin/python3.4

strana_ctverce = int(input("Napis delku strany ctverce: "))
plus_num = strana_ctverce > 0 

if plus_num:
    print("Obvod je", 4 * strana_ctverce, "cm.")
    print("Obsah je", strana_ctverce ** 2, "cm2.")
else:
    print('Napis KLADNE cele cislo')


