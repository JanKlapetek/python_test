#Implementujte třídu Car. V polích třídy by měly být uloženy následující údaje: model, rok vydání, výrobce, objem motoru, barva, cena.
#Implementujte metody třídy pro vstup a výstup dat, poskytněte přístup k jednotlivým polím prostřednictvím metod třídy.

class car:
    def __init__(self, model, rok, vyrobce, objem, barva, cena):
        self.model = model
        self.rok = rok
        self.vyrobce = vyrobce
        self.objem = objem
        self.barva = barva
        self.cena = cena

# Zobrazim info o autě.
    def info(self):
        print(f'Model: {self.model}')
        print(f'Rok: {self.rok}')
        print(f'Výrobce: {self.vyrobce}')
        print(f'Objem: {self.objem}')
        print(f'Barva: {self.barva}')
        print(f'Cena: {self.cena}')

moje_auto = car(model='Octavia 2 RS', rok='2013', vyrobce='Škoda', objem=2, barva='Bílá', cena=190000)
vase_auto = car(model=input('Zadej model auta: '), rok=input('Zadej rok auta: '), vyrobce=input('Zadej výrobce auta: '),
                objem=input('Zadej objem auta: '), barva=input('Zadej barvu auta: '), cena=input('Zadej cenu auta: '))
print('\nMoje auto:')
moje_auto.info()
print('\nZadané auto:')
vase_auto.info()
print('\nKonec programu.')



