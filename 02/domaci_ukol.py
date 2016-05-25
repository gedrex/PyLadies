#!/usr/bin/python3.4

print('Podle úkolu č. 14 si mám něco vymyslet. Tak jo, říkali jste si o to, doslova ;-)')

ans1 = input('Zadej náhodné cele cislo od 1 do 100 včetně: ')
ans2 = input('Zadej počet kafí/čajů/libovolných povzbuzovadel, které za den vypiješ: ')
ans3 = input('Zadej tvůj průměrný počet sprostých slov, které za den řekneš, když se ti něco nedaří("vole" se nepočítá): ')

#uznavam, tady jsem trochu cheatovala, nelibily se mi ValueError co to vyhazovalo pri zadavani pismenek, takze dotaz na google na "python is numeric" a nasla jsem tohle http://www.tutorialspoint.com/python/string_isnumeric.htm

#kontrola spravnosti zadani
if not ans1.isnumeric():
    print('Ty mě zkoušíš, což? Ale to je v pořádku, \'' + ans1 + '\' neprojde.')
elif not ans2.isnumeric():
    print('Ty mě zkoušíš, což? Ale to je v pořádku, \'' + ans2 + '\' neprojde.')
elif not ans3.isnumeric():
    print('Ty mě zkoušíš, což? Ale to je v pořádku, \'' + ans3 + '\' neprojde.')
else:
    #prevod odpovedi na integer
    ans1 = int(ans1)
    ans2 = int(ans2)
    ans3 = int(ans3)

    #zamitaci hlaseni pri nekterych nerealnych odpovedich
    if ans1 < 1 or ans1 > 100:
        print('Zkoušíš mě, že? Říkala jsme od 1 do 100, což', ans1, 'rozhodně není. Za trest program skončí a budeš ho muset spustit znova.')
    elif ans1 == 42:
        print('42 není náhodný číslo!!! :-P Za trest to spusť znova')
    elif ans2 < 1 or ans2 > 20:
        print(ans2, 'povzbuzovadel? To ti nežeru.')
    elif ans3 < 5:
        print('Ani 5 sprostých slov??? To ti nežeru.') 
    elif ans3 > 80:
        print(ans3, 'sprosťáren za den? To čteš jmenný seznam poslanců za poslední 4 volební období? To ti nežeru.')
    else:
        #spocitani magickeho cisla a odpoved z nejlepsiho generatoru nahodnych cisel na svete
        magic_number = ans1 * (ans1%3) + ans3 - ans2
        print("Otázka zní: Co dostaneme, když vynásobíme zvolené číslo zbytkem po jeho dělení číslem 3, přičteme průměrný počet sprostých slov a od toho odečteme počet kafí? Odpověď? Nejlepší generátor náhodných čísel na světě!!!")
        if magic_number==0:
            print("Tak že náhodné číslo dělitelné třemi a k tomu stejný počet kafí jako sprostých slov??(proč to piješ, když tomu pak nadáváš???), to chce opravdový kumšt, protože tvé magické číslo je '0'")
        elif magic_number==42:
            print("GRATULUJU!!! Tvé magické číslo je 42.... JAKO FAKT??? Dostat tohle číslo z generátoru náhodných čísel nemůže být náhoda!!! Ty prostě víš, jak se zeptat!")
        else:
            print("Tvé magické číslo je: ", magic_number)
    
