#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
from random import randint
"""
Cilem je vytvorit funkcni verzi hry Lode. Tohle je 2. pokus, mel by byt tedy o neco lepsi, nez puvodni. Zatim nebudu pouzivat tridy a objekty. Ty snad budu schopna pouzit v dalsi verzi.

pro kontrolu je v komentari radek 215 - 219 , po odkomentovani se lodicky zobrazi na hraci plose, vcetne bezpecnostnich zon kolem nich

ze stejnych duvodu jsou zakomentovany radky: 139(zobrazi, na kolikaty pokus se jaka lod vygenerovala) a 241(zobrazi seznam se vsemi vygenerovanymi lodemi)
"""

### uvodni popis ###
print "ZAHRAJEM SI LODĚ!!!\n"
print "Hru už jste to hráli na čtverečkovaný papír. Počítač před vámi schová lodě a vy musíte uhodnout, kde lodě jsou. Můžete si určit, na jak velkém poli budete chtít hrát a kolik lodí před vámi má počítač schovat. Lodě se můžou dotýkat maximálně rohy, nikoli hranami. Ve hře jsou 3 typy lodí. Lodě můžou být libovolně natočené.\n"
print "Typ 1 - největší loď: \n\n     X\n    XXX\n\nTyp 2:\n\n    XXX\n\nTyp 3:\n\n     X\n    XXX\n     X\n\n"
print "Jen podotýkám, že máš maximálně 10 střel mimo."
### --- ###
def control(control_input, min_count, max_count):
    """
    funkce pro kontrolu vstupu, ktere maji byt typu int a mit minimalni a maximalni hodnotu. Vraci zadane cislo v typu 'int', pokud je ve spravnem rozmezi
    """
    test_int = 0
    while test_int < 1:
        if control_input.isdigit() == False:
            print "Type number from %s up to %s:" % (min_count, max_count)
            control_input = raw_input("Type number from %s up to %s:" % (min_count, max_count))
        elif control_input.isdigit() == True:
            control_input = int(control_input)
            if control_input not in range(min_count, max_count+1):
                print "Type number from %s up to %s" % (min_count, max_count)
                control_input = raw_input("Type number from %s up to %s:" % (min_count, max_count))
            else:
                test_int += 1
                return int(control_input)
### konec kontroly vstupu ###

### promenne
zones = []

board_size = raw_input("Type the size of the board from 3 up to 25:") # velikost hrany hraciho pole
board_size = control(board_size, 3, 25)

board_symbol = ' '  #symbol pro vodu v hracim poli
ships1_count = raw_input("Type ammount of ships type 1 from 1 up to 10:") # mnozstvi lodicek typu 1
ships1_count = control(ships1_count, 1, 10)
ships2_count = raw_input("Type ammount of ships type 2 from 1 up to 10:") # mnozstvi lodicek typu 2
ships2_count = control(ships2_count, 1, 10)
ships3_count = raw_input("Type ammount of ships type 3 from 1 up to 10:") # mnozstvi lodicek typu 3
ships3_count = control(ships3_count, 1, 10)

#definice hraciho pole
board = [] #hraci pole(seznam) a jeho definice
for x in range(board_size):
    board.append([board_symbol] * board_size)
board_net = [] #seznam poli v boardu. Dulezite pro vytvareni zon v deklaraci lodi - pro kontrolu, jestli je dostatek volnych pozic pro jeji vytvoreni. Po kazdem vytvoreni zony se z board net pole dane zony vymazou.
for x in range(board_size):
        for y in range(board_size):
            board_net.append([x, y])

all_ships = [] #seznam souradnic vsech lodi, kazda lod ve vlastnim seznamu


###vygeneruje nahodnou pozici na hracim poli v podobe 2prvkoveho seznamu.
def random_point(board_size):
    randposition = []
    randposition.append(randint(0, board_size-1))
    randposition.append(randint(0, board_size-1))
    return randposition

### vykresleni hraciho pole
def print_board(board):
    print "    ",
    print '| %s' % ' | '.join(str(x) for x in range(len(board)) if x < 10),
    print '| %s' % '| '.join(str(x) for x in range(len(board)) if x > 9)
    print '    ','-' * 4 * len(board) + '-'
    for i in range(len(board)):
        if i < 10:
            print "|%s|  |" % str(i), " | ".join(board[i]), '|'
        if i > 9:
            print "|%s| |" % str(i), " | ".join(board[i]), '|'
        print '    ','-' * 4 * len(board) + '-'

###funkce pro nalezeni stejnych  poli
def getMatches(first, second):
    count = 0
    for item in first:
        if item in second:
            count += 1
    return count


### randpoint zajistuje, aby se lode negenerovaly za okrajem hraciho pole. Bod je zavisly na nejdelsim rozmeru dane lodi.
def randpoint(board_size, random_point, ship_range):
    random = []
    central = random_point(board_size) # centralni nahodny bod muze byt u kraje. Pokud tomu tak je, musime ho posunout.
    closest = int(ship_range/2)
    if central[0]-closest < 0:
        central[0]=central[0]+closest
    if central[0]+closest > board_size-1:
        central[0]=central[0]-closest

    if central[1]-closest < 0:
        central[1]=central[1]+closest
    if central[1]+closest > board_size-1:
        central[1]=central[1]-closest

    random.extend([central[0],central[1]])

    return random

### definice lodi libovolneho druhu.
def ship(randpoint, zones, board_net, ship_type):
    #vygeneruje nahodny smer otoceni lodi od 0 do 3, podle smeru hod. rucicek:
    direction = randint(0,3)
    temp_ship_zone = []
    shipzone = []
    zone_ship = []
    test_ship = []
    retry = 0
    max_retries = 200
    count = 0
    #kontrola, aby se zony lodi negenerovaly pres sebe, s maximalnim poctem pokusu o umisteni
    while retry < max_retries:
        ship = ship_type(direction,shipzone)
        ship_range = ship[0]
        central = randpoint(board_size, random_point, ship_range)
        closest = int(ship_range/2)
        #pred kazym pokusem o vygenerovani pozice lodi je nutne vyprazdnit jejich pole z minuleho cyklu
        del temp_ship_zone[:]
        del test_ship[:]

        # docasne pole pro generovani lodi
        for x in range(ship_range):
            for y in range(ship_range):
                temp_ship_zone.append([central[0]+(-closest+x),central[1]+(-closest+y)])

        test_ship.extend(ship_type(direction, temp_ship_zone)[1::]) # lod vygenerovana podle typu v docasnem poli

        for item in test_ship:
            if item in zones:
                count = 1
        if count < 1:
            shipzone = test_ship #souradnice lodi
            break
        elif retry == (max_retries-1):
            print "Ship could not be placed, there is no place for it."
            break
        elif count > 0:
            retry += 1
            count = 0
    #pokud zadne pole lodi neni v zadne z bezpecnostnich zon, vygeneruje lod ve forme seznamu souradnic poli lodi
    #print "lod vytvorena v %s. pokusu" % (retry+1)
    sec_zone = [] #vytvoreni pole pro bezpecnostni zonu
    #vytvoreni bezpecnostniho zony kolem kazdeho bodu lodi
    for a in shipzone:
        for x in range(3):
            for y in range(3):
                sec_zone.append([a[0]+(-1+x),a[1]+(-1+y)])
    #vymazani souradnic samotne lodi z bezpecnostni zony
    for a in shipzone:
        if a in sec_zone:
            sec_zone.remove(a)

    zone_ship.append(sec_zone)
    zone_ship.append(shipzone)

    for i in zone_ship[0]:
        if i in board_net:
            board_net.remove(i)
    for i in zone_ship[1]:
        if i in board_net:
            board_net.remove(i)

    return zone_ship

###### Definice tvaru samotnych lodi
### Kazda lod vraci seznam "ship", coz je seznam 2 seznamu. Prvni prvek je nejdelsi rozmer lodi, nasleduji souradnice samotne lodi podle smeru natoceni
#   X
# X X X
#
def type1(direction, safety_zone):
    ship = []
    ship.append(3) #prvni hodnotou v seznamu je nejdelsi rozmer lodi, potrebny pro velikost bezpecnostni zony
    if direction == 0 and safety_zone != []:
        ship.extend([safety_zone[1],safety_zone[3],safety_zone[4],safety_zone[5]])
    elif direction == 1 and safety_zone != []:
        ship.extend([safety_zone[1],safety_zone[4],safety_zone[5],safety_zone[7]])
    elif direction == 2 and safety_zone != []:
        ship.extend([safety_zone[3],safety_zone[4],safety_zone[5],safety_zone[7]])
    elif direction == 3 and safety_zone != []:
        ship.extend([safety_zone[1],safety_zone[3],safety_zone[4],safety_zone[7]])
    return ship

#
# X X X
#
def type2(direction, safety_zone):
    ship = []
    ship.append(3) #prvni hodnotou v seznamu je nejdelsi rozmer lodi
    if (direction == 0 or direction == 2) and safety_zone != []:
        ship.extend([safety_zone[1],safety_zone[4],safety_zone[7]])
    elif (direction == 1 or direction == 3) and safety_zone != []:
        ship.extend([safety_zone[3],safety_zone[4],safety_zone[5]])
    return ship

#    X
#  X X X
#    X
def type3(direction, safety_zone):
    ship = []
    ship.append(3) #prvni hodnotou v seznamu je nejdelsi rozmer lodi
    if direction in range(4) and safety_zone != []:
        ship.extend([safety_zone[1],safety_zone[3],safety_zone[4],safety_zone[5],safety_zone[7]])
    return ship

###generovani lodi
def generate_ship(all_ships, ship_type, ship_count):
    for n in range(ship_count):
        ships = ship(randpoint, zones, board_net, ship_type)
        if len(ships)>0:
            for a in ships[0]:
                if a in zones:
                    zones.remove(a)
            zones.extend(ships[0])

            #vykresleni lodi a jejich bezpecnostnich zon
            """
            for a in ships[0]:
                if a[0] in range(board_size) and a[1] in range(board_size):
                    board[a[0]][a[1]] = '~'
            for a in ships[1]:
                board[a[0]][a[1]] = '%s' % n
            """
            all_ships.append(ships[1]) #seznam souradnic vygenerovane lode se prida do seznamu vsech lodi
        else:
            print "Ship %s was not placed" %  n


###umisteni lodi

generate_ship(all_ships, type1, ships1_count)

generate_ship(all_ships, type2, ships2_count)

generate_ship(all_ships, type3, ships3_count)

print_board(board) #vykresleni hraci plochy

# odstraneni prazdnych seznamu(nevygenerovanych lodi) ze seznamu vsech lodi
while [] in all_ships:
    all_ships.remove([])
print "Count of ships on board:", len(all_ships)

#print all_ships

hit_ships = [] # zasazene lode
guess = [] # hadana souradnice
hit = 0 # zasah
guess_count = 0 # pocet hadani
sunk = 0 # pocet potopenych lodi
guessed = [] # seznam jiz hadanych souradnic
test_int = 0 # pocita, zda bylo zadane cislo nebo ne
max_guess_count = 10 #pocet pokusu
while guess_count < max_guess_count:

    guess_row = raw_input("Row number:")
    guess_row = control(guess_row, 0, board_size-1)
    guess.append(guess_row)

    guess_col = raw_input("Col number:")
    guess_col = control(guess_col, 0, board_size-1)
    guess.append(guess_col)

    if guess in guessed:
        print "You alredy guessed this"
        guess_count += 1
    elif guess not in guessed:
        guessed.append(guess)
        for a in range(len(all_ships)):
            if guess in all_ships[a]:
                if a not in hit_ships:
                    hit_ships.append(a)

                all_ships[a].remove(guess)
                if all_ships[a] == []:
                    sunk += 1
                    print "\033[1;45mGreat! You sunk whole ship!\033[1;m"
                hit += 1
            else:
                hit = hit

        if (hit > 0) and (len(all_ships) - sunk == 0):
            board[guess[0]][guess[1]] = "\033[1;32mX\033[1;m"
            print_board(board)
            print "\033[1;42mCongratulation! You sunk all my ships!\033[1;m"
            guess_count = max_guess_count
        elif hit > 0:
            board[guess[0]][guess[1]] = "\033[1;32mX\033[1;m"
            guess_count = guess_count
            hit = 0
            print_board(board)
            print "\033[1;32mHit!\033[1;m"
        elif hit == 0:
            guess_count += 1
            board[guess[0]][guess[1]] = "\033[1;37m-\033[1;m"
            hit = 0
            print_board(board)
            print "\033[1;37mNothing...\033[1;m"

    hit = 0

    guess = []

else:
    print "\033[1;41mGame Over\033[1;m"
    for ships in all_ships:
        for ship in ships:
            board[ship[0]][ship[1]] = "X"
    print_board(board)


