#!/home/gedrex/pyladies/venv/bin/python

#definice tridy
class Kotatko:
    ###specialni metoda, ktera aktivuje objekt a krome samu sebe, vzdy musi byt pritomen atribut jmeno
    def __init__(self, jmeno):
        self.jmeno = jmeno
    
    def snez(self, jidlo):
        print('{}: {} mi chutna!'.format(self.jmeno, jidlo))

    ###dalsi specialni funkce, ktera prevadi to, co funkce vraci, na string
    #def __str__(self):
    #    return '<Kotatko s jmenem: {}'.format(self.jmeno)
    
    ###dalsi specialni funkce(funguje stejne jako len(ve fcich)
    #def __len__(self):
    #    return 1


    #definice metody funkce
    def zamnoukej(self):
        print('{}: Mnau!'.format(self.jmeno))


micka = Kotatko('Micka')

mourek = Kotatko(jmeno='Mourek')

micka.zamnoukej()
mourek.zamnoukej()

kocour = Kotatko('Kocour')
kocour.snez('ryba')
print(kocour.jmeno)
       
#volani __str__:
#print(micka)
#print(mourek.__str__())
#print(str(micka))


### dalsi specialni metoda
#print(len(micka))
#print(micka.__len__())


