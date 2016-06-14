#!/home/gedrex/pyladies/venv/bin/python

###
#Python nejdriv hleda metody a atributy v podtride, pak se teprve kouka do rodicovske. Pokud funguje dedicnost, jdeme tedy odspoda nahoru.
#proto muzeme predefinovat cele funkce

class Zviratko:
    def __init__(self, jmeno):
        self.jmeno = jmeno

    def snez(self, jidlo):
        print('{}: {} mi chutna!'.format(self.jmeno, jidlo))

    def udelej_zvuk(self):
        print('{}: {}!'.format(self.jmeno, self.zvuk))

#definice podtridy - dedicnost
class Kotatko(Zviratko):
    zvuk = 'Mnau' 
    def snez(self, jidlo):
        print('{} si s {} nejdriv hraje, nez to sni!'.format(self.jmeno, jidlo))    
        #volani funkce super zavola metodu rodicovske tridy s atributy ktere zadame
        super().snez(jidlo)


class Stenatko(Zviratko):
    zvuk = 'Haf'

class Hadatko(Zviratko):
    zvuk = 'Sssss'
    def __init__(self, jmeno):
        jmeno = jmeno.replace('s', 'sss')
        super().__init__(jmeno)


micka = Kotatko('Kocour')
micka.snez('ryba')

puclik = Stenatko('Puclik')
puclik.snez('ryba')
puclik.udelej_zvuk

standa = Hadatko('Stanislav')
standa.snez('myš')


#### Krmení dravé zvěře ####

zoo = [Kotatko('Mourek'), Stenatko('Punťa'), Hadatko('stanislav')]

for zviratko in zoo:
    zviratko.snez('flákota')
    zviratko.udelej_zvuk()

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



