# Úkol 2
# Implementujte třídu Kniha. V polích třídy by měly být uloženy tyto údaje: název, rok vydání, nakladatel, žánr, autor, cena.
# Implementujte metody třídy pro vstup a výstup dat, zajistěte přístup k jednotlivým polím prostřednictvím metod třídy.

# Vytvoření třídy book
class Book:
    def __init__(self, nazev, rok_vydani, nakladatelstvi, zanr, autor, cena):
        self.nazev = nazev
        self.rok_vydani = rok_vydani
        self.nakladatelstvi = nakladatelstvi
        self.zanr = zanr
        self.autor = autor
        self.cena = cena

    def info_kniha(self):
        print(f'Název: {self.nazev}')
        print(f'Rok vydání: {self.rok_vydani}')
        print(f'Nakladatelství: {self.nakladatelstvi}')
        print(f'Žánr: {self.zanr}')
        print(f'Autor: {self.autor}')
        print(f'Cena: {self.cena}')

kniha_pad_domu_usheru = Book(
    nazev="Pád domu Usherů a jiné povídky",
    rok_vydani=2024,
    nakladatelstvi="Fobos",
    zanr=["Literatura světová", "Horory", "Povídky"],
    autor="Edgar Allan Poe",
    cena=500
)
# Zavolání funkce
kniha_pad_domu_usheru.info_kniha()
# Konec programu
print('\nKonec programu')
