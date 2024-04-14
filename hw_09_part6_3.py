class Tvar:
    def __init__(self, nazev):
        self.nazev = nazev
    def zobraz(self):
        print(f'Typ tvaru je: {self.nazev}')
    def uloz(self, soubor):
        with open(soubor, 'a') as f:
            f.write(f'{self.nazev}\n')
            self._uloz_specificke_informace(f)

    @staticmethod
    def nacti(soubor):
        with open(soubor, 'r') as f:
            nazev = f.readline().strip()
            tvar = Tvar(nazev)
            tvar._nacti_specificke_informace(f)
            return tvar

    def _uloz_specificke_informace(self, f):
        pass
    def _nacti_specificke_informace(self, f):
        pass

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

    def _uloz_specificke_informace(self, f):
        f.write(f'Souřadnice levého horního rohu: ({self.x}, {self.y})')
        f.write(f'Délka strany: {self.delka_strany}\n')

    def _nacti_specificke_informace(self, f):
        x, y = map(int, f.readline().split()[3][1:-1].split(','))
        self.x, self.y = x, y
        self.delka_strany = int(f.readline().split()[2])

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

    def _uloz_specificke_informace(self, f):
        f.write(f'Souřadnice levého horního rohu: ({self.x}, {self.y})\n')
        f.write(f'Šířka: {self.sirka}\n')
        f.write(f'Výška: {self.vyska}\n')

    def _nacti_specificke_informace(self, f):
        x, y = map(int, f.readline().split()[3][1:-1].split(","))
        self.x, self.y = x, y
        self.sirka = int(f.readline().split()[1])
        self.vyska = int(f.readline().split()[1])

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

    def _uloz_specificke_informace(self, f):
        f.write(f'Souřadnice středu: ({self.stred_x}, {self.stred_y})\n')
        f.write(f'Poloměr: {self.polomer}\n')

    def _nacti_specificke_informace(self, f):
        x, y = map(int, f.readline().split()[3][1:-1].split(","))
        self.stred_x, self.stred_y = x, y
        self.polomer = int(f.readline().split()[1])

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

    def _uloz_specificke_informace(self, f):
        f.write(f'Souřadnice levého horního rohu opsaného obdélníku: ({self.x}, {self.y})\n')
        f.write(f'Šířka opsaného obdélníku: {self.sirka}\n')
        f.write(f'Výška opsaného obdélníku: {self.vyska}\n')

    def _nacti_specificke_informace(self, f):
        x, y = map(int, f.readline().split()[3][1:-1].split(','))
        self.x, self.y = x, y
        self.sirka = int(f.readline().split()[1])
        self.vyska = int(f.readline().split()[1])

# Vytvoření seznamu všech tvarů
tvary = [
    Ctverec('Čtverec', 0, 0, 5),
    Obdelnik('Obdélník', 0, 0, 8, 6),
    Kruh('Kruh', 0, 0, 5),
    Elipsa('Elipsa', 0, 0, 10, 7)
]
# Uložení tvarů do souboru
nazev_souboru = 'tvary_data.txt'
with open(nazev_souboru, 'w') as f:
    for tvar in tvary:
        tvar.uloz(nazev_souboru)

# Načtení tvarů ze souboru
nactene_tvary = []
with open(nazev_souboru, 'r') as f:
    while True:
        try:
            tvar = Tvar.nacti(nazev_souboru)
            nactene_tvary.append(tvar)
        except EOFError:
            break

# Zobrazení informací o každém tvaru
for tvar in nactene_tvary:
    tvar.zobraz()
    print()





