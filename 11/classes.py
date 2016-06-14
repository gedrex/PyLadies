#!/home/gedrex/pyladies/venv/bin/python

#definice tridy
class Kotatko:
    #specialni metoda, ktera aktivuje objekt a krome samu sebe, vzdy musi byt pritomen atribut jmeno
    def __init__(self, jmeno):
        self.jmeno = jmeno

    #definice metody funkce
    def zamnoukej(self):
        print('{}: Mnau!'.format(self.jmeno))


#prirazeni tridy do promene
micka = Kotatko()

#prirazeni atributu tridy
micka.jmeno = 'Micka'

#volani metody Kotatka micka
micka.zamnoukej()

#tak ne:
# Kotatko.zamnoukej(kotatko)

mourek = Kotatko()
mourek.jmeno = 'Mourek'
mourek.zamnoukej()

