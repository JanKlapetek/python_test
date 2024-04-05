# Úkol 3
# Implementujte třídu Stadion. Do polí třídy se ukládají následující údaje: název stadionu, datum otevření, země, město, počet míst k sezení.
# Implementujte metody třídy pro vstup a výstup dat, zajistěte přístup k jednotlivým polím prostřednictvím metod třídy.

class Stadion:
    def __init__(self, nazev_stadionu, datum_otevreni, zeme, mesto, pocet_mist):
        self.nazev_stadionu = nazev_stadionu
        self.datum_otevreni = datum_otevreni
        self.zeme = zeme
        self.mesto = mesto
        self.pocet_mist = pocet_mist

    def info_stadion(self):
        print(f'Název stadionu: {self.nazev_stadionu}')
        print(f'Datum otevření: {self.datum_otevreni}')
        print(f'Země: {self.zeme}')
        print(f'Město: {self.mesto}')
        print(f'Počet míst: {self.pocet_mist}')

pridej_stadion = Stadion(
    nazev_stadionu='Old Trafford',
    datum_otevreni='19.02.1910',
    zeme='Velká Británie',
    mesto='Manchester',
    pocet_mist=74310
)

volba = int(input('Zadej číslo 1 a zobrazí se ten nej stadion na světě a nebo 0 pro ukončení programu: '))

if volba == 1:
    pridej_stadion.info_stadion()
elif volba == 0:
    print('Program ukončen.')
    exit()
else:
    print('Špatná volba. Program ukončen.')
