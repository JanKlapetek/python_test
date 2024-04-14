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

class Obdelnik(Tvar):
    def __init__(self, nazev, x, y, sirka, vyska):
        super().__init__(nazev)
        self.x = x
        self.y = y
        self.sirka = sirka
        self.vyska = vyska

    def zobraz(self):
        super().zobraz()
        print(f'Souřadnice levého horního rohu: {self.x}, {self.y}')
        print(f'Šířka: {self.sirka}, Výška: {self.vyska}')

class Kruh(Tvar):
    def __init__(self, nazev, stred_x, stred_y, polomer):
        super().__init__(nazev)
        self.stred_x = stred_x
        self.stred_y = stred_y
        self.polomer = polomer

    def zobraz(self):
        super().zobraz()
        print(f'Souřadnice středu: ({self.stred_x}, {self.stred_y})')
        print(f'Poloměr: {self.polomer}')

class Elipsa(Tvar):
    def __init__(self, nazev, x, y, sirka, vyska):
        super().__init__(nazev)
        self.x = x
        self.y = y
        self.sirka = sirka
        self.vyska = vyska

    def zobraz(self):
        super().zobraz()
        print(f'Souřadnice levého horního rohu opsaného obdelníku: ({self.x}, {self.y})')
        print(f'Šířka opsaného obdelníku: {self.sirka}')
        print(f'Výška opsaného obdelníku: {self.vyska}')

# Vytvoření seznamu všech tvarů
tvary = [
    Ctverec('Čtverec', 0, 0, 5),
    Obdelnik('Obdélník', 0, 0, 8, 6),
    Kruh('Kruh', 0, 0, 5),
    Elipsa('Elipsa', 0, 0, 10, 7)
]
# Uložení tvarů do souboru
nazev_souboru = 'tvary_data.pkl'
for tvar in tvary:
    tvar.uloz(nazev_souboru)

# Načtení tvarů ze souboru
nactene_tvary = [Tvar.nacti(nazev_souboru) for _ in range(len(tvary))]

# Zobrazení informací o každém tvaru
for tvar in nactene_tvary:
    tvar.zobraz()
    print()





