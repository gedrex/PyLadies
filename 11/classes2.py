#!/home/gedrex/pyladies/venv/bin/python

#definice tridy
class Kotatko:
    #specialni metoda, ktera aktivuje objekt a krome samu sebe, vzdy musi byt pritomen atribut jmeno
    def __init__(self, jmeno):
        self.jmeno = jmeno
    
    #dalsi specialni funkce, ktera prevadi to, co funkce vraci, na string
    def __str__(self):
        return '<Kotatko s jmenem: {}'.format(self.jmeno)

    #definice metody funkce
    def zamnoukej(self):
        print('{}: Mnau!'.format(self.jmeno))


micka = Kotatko('Micka')

mourek = Kotatko(jmeno='Mourek')

micka.zamnoukej()
mourek.zamnoukej()

#volani __str__:
print(micka)
print(micka.__str__())
print(str(micka))

