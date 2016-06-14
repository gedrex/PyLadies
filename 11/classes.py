#!/home/gedrex/pyladies/venv/bin/python

#definice tridy
class Kotatko:
    #definice metody funkce
    def zamnoukej(self):
        print('{}: Mnau!'.format(self.jmeno))

#prirazeni tridy do promene
kotatko = Kotatko()

#prirazeni atributu tridy
kotatko.jmeno = 'Micka'

#volani metody tridy Kotatko
kotatko.zamnoukej()

#tak ne:
# Kotatko.zamnoukej(kotatko)

