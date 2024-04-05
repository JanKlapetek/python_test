# Úkol 2
# Vytvořte třídu Ship obsahující informace o lodi.
# Pomocí dědičnosti implementujte třídu Fregata (obsahuje informace o fregatě),
# třídu Torpédoborec (obsahuje informace o torpédoborci), třídu Křižník (obsahuje informace o křižníku).
# Každá třída musí mít požadované metody.

class Ship:
    def __init__(self, nazev, delka, pocet_motoru, vykon):
        self.nazev = nazev
        self.delka = delka
        self.pocet_motoru = pocet_motoru
        self.vykon = vykon

    def ziskej_info(self):
        return f'Název lodi: {self.nazev} \nDélka: {self.delka} \nPočet motorů: {self.pocet_motoru} \nVýkon: {self.vykon}'

class Fregata(Ship):
    def __init__(self, nazev, delka, pocet_motoru, vykon, pocet_plachet):
        super().__init__(nazev, delka, pocet_motoru, vykon)
        self.pocet_plachet = pocet_plachet

    def info_fregata(self):
        return f'Počet plachet je: {self.pocet_plachet}'

class Torpedoborec(Ship):
    def __init__(self, nazev, delka, pocet_motoru, vykon, munice):
        super().__init__(nazev, delka, pocet_motoru, vykon)
        self.munice = munice

    def info_torpedoborec(self):
        return f'Jako munice se používá: {self.munice}'

class Kriznik(Ship):
    def __init__(self, nazev, delka, pocet_motoru, vykon, dela):
        super().__init__(nazev, delka, pocet_motoru, vykon)
        self.dela = dela

    def info_kriznik(self):
        return f'Křižník má {self.dela} děl.'


# Fregata
lod_fregata = Fregata('velika', 300, 7, 0,22)
print('\n')
print(lod_fregata.ziskej_info())
print(lod_fregata.info_fregata())

# Torpedoborec
lod_torpedoborec = Torpedoborec('HMS Havock', 150, 20, '1800MW', 'Rakety C8998')
print('\n')
print(lod_torpedoborec.ziskej_info())
print(lod_torpedoborec.info_torpedoborec())


