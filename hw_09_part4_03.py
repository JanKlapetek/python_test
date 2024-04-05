# Úkol 3
# Vytvořte třídu Money pro práci s penězi (objekt třídy pracuje s jednou měnou).
# Třída musí obsahovat pole pro uložení celočíselné části (dolary, eura, hřivny atd.) a pole pro uložení zlomkové části (centy, eurocenty, kopějky atd.).
# Implementujte metody pro tisk částek a nastavení hodnot částí (celočíselných a zlomkových).
# Na základě třídy Money vytvořte třídu Product. Implemen-tujte metodu, která umožní snížit cenu o zadané číslo.
# Implementujte metody a pole požadované pro každou třídu.

import decimal
class Money:
    def __init__(self, dolary=0, centy=0):
        # Inicializace celé a desetinné části
        self.dolary = dolary
        self.centy = centy

    def nastav_hodnotu(self, dolary, centy):
        # Nastavení celé a desetinné části
        self.dolary = dolary
        self.centy = centy

    def __str__(self):
        return f'{self.dolary} $ {self.centy:02d} c'

class Produkt:
    def __init__(self, nazev, cena):
        self.nazev = nazev
        self.cena = cena

    def snizit_cenu(self, snizeni):
        # Snížení ceny o zadanou částku
        self.cena.dolary -= snizeni.dolary
        self.cena.centy -= snizeni.centy

    def __str__(self):
        return f'{self.nazev}: {self.cena}'


pocatecni_cena = Money(dolary=int(input('Zadej počáteční cenu knihy v dolarech: ')), centy=int(input('Zadej centy: ')))
produkt = Produkt('Kniha stojí: ', cena=pocatecni_cena)
snizeni = Money(dolary=int(input('Zadej o kolik dolarů snížíme cenu: ')), centy=int(input('Zadej o kolik centů: ')))
produkt.snizit_cenu(snizeni)
print(produkt)