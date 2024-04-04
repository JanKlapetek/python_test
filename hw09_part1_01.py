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

