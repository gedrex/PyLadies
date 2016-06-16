#!../venv/bin/python

###
#Python nejdriv hleda metody a atributy v podtride, pak se teprve kouka do rodicovske. Pokud funguje dedicnost, jdeme tedy odspoda nahoru.
#proto muzeme predefinovat cele funkce

class Zviratko:
    def __init__(self, jmeno):
        self.jmeno = jmeno

    def snez(self, jidlo):
        print('{}: {} mi chutna!'.format(self.jmeno, jidlo))



#definice podtridy - dedicnost
class Kotatko(Zviratko):
    def zamnoukej(self):
        print('{}: Mnau!'.format(self.jmeno))
    
    def snez(self, jidlo):
        print('{} si s {} nejdriv hraje, nez to sni!'.format(self.jmeno, jidlo))    
        #volani funkce super zavola metodu rodicovske tridy s atributy ktere zadame
        super().snez(jidlo)


class Stenatko(Zviratko):
    def zastekej(self):
        print('{}: Haf!'.format(self.jmeno))


class Hadatko(Zviratko):
    def __init__(self, jmeno):
        jmeno = jmeno.replace('s', 'sss')
        super().__init__(jmeno)


micka = Kotatko('Kocour')
micka.snez('ryba')

puclik = Stenatko('Puclik')
puclik.snez('ryba')
puclik.zastekej

standa = Hadatko('Stanislav')
standa.snez('myš')


#### Krmení dravé zvěře ####

zoo = [Kotatko('Mourek'), Stenatko('Punťa'), Hadatko('stanislav')]

for zviratko in zoo:
    zviratko.snez('flákota')

### priklad dedicnosti 
#   auto muze mit volant, volant nemuze mit auto
class Volant:
    pass

class Auto:
    def __init__(self, volant=None):
        if volant == None:
            self.volant = Volant()
        else:
            self.volant = volant



