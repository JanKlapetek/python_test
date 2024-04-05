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
        return f'Název lodi: {self.nazev}', f'Délka: {self.delka}', f'Počet motorů: {self.pocet_motoru}', f'Výkon: {self.vykon}'

class Fregata:
    def __init__(self, nazev, delka, pocet_motoru, vykon, pocet_plachet):
        super().__init__(nazev, delka, pocet_motoru, vykon)
        self.pocet_plachet = pocet_plachet

    def info_fregata(self):
        return f'Počet plachet je: {self.pocet_plachet}'


a = Ship('velika', 300, 7, '600W')
a.ziskej_info()