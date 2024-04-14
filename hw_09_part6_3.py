import pickle
class Tvar:
    def __init__(self, nazev):
        self.nazev = nazev
    def zobraz(self):
        print(f'Typ tvaru je: {self.nazev}')
    def uloz(self, soubor):
        with open(soubor, 'wb') as f:
            pickle.dump(self,f)

    @staticmethod
    def nacti(soubor):
        with open(soubor, 'rb') as f:
            return pickle.load(f)

class Ctverec(Tvar):
    def __init__(self, nazev, x, y, delka_strany):
        super().__init__(nazev)
        self.x = x
        self.y = y
        self.delka_strany = delka_strany

    def zobraz(self):
        super().zobraz()
        print(f'Souřadnice levého horního rohu: ({self.x}, {self.y})')
        print(f'Délka strany: {self.delka_strany}')




