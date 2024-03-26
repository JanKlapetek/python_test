def uzivatel(jmeno, prijmeni):
    print(f'Vítej {jmeno} {prijmeni}')
def menu():
    print('1. součet')
    print('2. součin')
    print('3. odčítání')
    print('4. dělení')
    print('5.' adssasdasd')

def scitani(cislo1, cislo2):
        soucet = cislo1 + cislo2
        return print(f'Součet čísla {cislo1} a čísla {cislo2} je: {soucet}')

def nasobeni(cislo1, cislo2):
    if volba == 2:
        soucin = cislo1 * cislo2
        return print(f'Součin čísla {cislo1} a čísla {cislo2} je: {soucin}')
def odcitani(cislo1, cislo2):
    if volba == 3:
        rozdil = cislo1 - cislo2
        return print(f'Rozdíl čísel {cislo1} a {cislo2} je: {rozdil}')

def deleni(cislo1, cislo2):
    if volba == 4:
        podil = cislo1 / cislo2
        return print(f'Podíl čísel {cislo1} a {cislo2} je: {podil}')



uzivatel(jmeno=input('Zadejte jméno: '), prijmeni=input('Zadejte příjmení: '))
print('')
menu()
volba = int(input('Vyber číslo z menu: '))
print('')
if volba == 1:
    vysledek = scitani(cislo1=int(input('Zadej první číslo: ')), cislo2=int(input('Zadej druhé číslo: ')))

elif volba == 2:
    vysledek2 = nasobeni(cislo1=int(input('Zadej první číslo: ')), cislo2=int(input('Zadej druhé číslo: ')))

elif volba == 3:
    vysledek3 = odcitani(cislo1=int(input('Zadej první číslo: ')), cislo2=int(input('Zadej druhé číslo: ')))

elif volba == 4:
    vysledek4 = deleni(cislo1=int(input('Zadej první číslo: ')), cislo2=int(input('Zadej druhé číslo: ')))

else:
    print('špatně zadáno:')




