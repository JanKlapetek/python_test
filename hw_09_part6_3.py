import pickle

class Tvar:
    def __init__(self, nazev):
        self.nazev = nazev
        pass  # Základní inicializace tvaru

    def zobraz(self):
        print('Tvar: ')

    def uloz(self, soubor):
        with open(soubor, 'wb') as soubor:
            pickle.dump(self, soubor)

    @classmethod
    def nacti(cls, soubor):
        with open(soubor, 'rb') as soubor:
            return pickle.load(soubor)

class Ctverec(Tvar):
    def __init__(self, nazev, x, y, delka_strany):
        super().__init__(nazev)
        self.x = x
        self.y = y
        self.delka_strany = delka_strany

    def zobraz(self):
        super().zobraz()
        print(f'{self.nazev}: Horní levý roh ({self.x}, {self.y}), Délka strany: {self.delka_strany}\n')

class Obdelnik(Tvar):
    def __init__(self, nazev, x, y, sirka, vyska):
        super().__init__(nazev)
        self.x = x
        self.y = y
        self.sirka = sirka
        self.vyska = vyska

    def zobraz(self):
        super().zobraz()
        print(f'{self.nazev}: Levý horní roh ({self.x}, {self.y}), Šířka: {self.sirka}, Výška: {self.vyska}\n')

class Kruznice(Tvar):
    def __init__(self, nazev, stred_x, stred_y, polomer):
        super().__init__(nazev)
        self.stred_x = stred_x
        self.stred_y = stred_y
        self.polomer = polomer

    def zobraz(self):
        super().zobraz()
        print(f'{self.nazev}: Střed ({self.stred_x}, {self.stred_y}), Poloměr: {self.polomer}\n')

class Elipsa(Tvar):
    def __init__(self, nazev, x, y, sirka, vyska):
        super().__init__(nazev)
        self.x = x
        self.y = y
        self.sirka = sirka
        self.vyska = vyska

    def zobraz(self):
        super().zobraz()
        print(f'{self.nazev}: Horní levý roh opsaného obdélníku ({self.x}, {self.y}), Šířka: {self.sirka}, Výška: {self.vyska}')

# Příklad použití
ctverec = Ctverec('Čtverec', 0, 0, 5)
obdelnik = Obdelnik('Obdélník', 2, 3, 8, 6)
kruznice = Kruznice('Kružnice', 10, 10, 4)
elipsa = Elipsa('Elipsa', 5, 5, 12, 8)

tvary = [ctverec, obdelnik, kruznice, elipsa]

# Uložení tvarů do souboru
for i, tvar in enumerate(tvary):
    tvar.uloz(f'tvar_{i}.pickle')

# Načtení tvarů ze souboru
nactene_tvary = []
for i in range(len(tvary)):
    nactene_tvary.append(Tvar.nacti(f'tvar_{i}.pickle'))

# Zobrazení informací o načtených tvarech
for nacteny_tvar in nactene_tvary:
    nacteny_tvar.zobraz()
