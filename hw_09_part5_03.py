# Úkol 3
# Vytvořte třídu Letadlo. Pomocí přetěžování operátorů implementujte následující:
# ■ Zkontrolujte, zda se typy letadel rovnají (operátor ==);
# ■ Zvyšování a snižování počtu cestujících v letadle.
# (operátory: + - + = - =);
# ■ Porovnání dvou letadel na maximální možný počet
# cestujících na palubě (operátory: > < <= >=).

class Letadlo:
    def __init__(self, typ, max_cestujicich):
        self.typ = typ
        self.max_cestujicich = max_cestujicich
        self.aktualni_cestujici = 0

    def __eq__(self, other):
        return self.typ == other.typ

    def __add__(self, cestujici):
        self.aktualni_cestujici += cestujici
        return self

    def __sub__(self, cestujici):
        self.aktualni_cestujici -= cestujici
        return self

    def __iadd__(self, cestujici):
        self.aktualni_cestujici += cestujici
        return self

    def __isub__(self, cestujici):
        self.aktualni_cestujici -= cestujici
        return self

    def __lt__(self, other):
        return self.max_cestujicich < other.max_cestujicich

    def __le__(self, other):
        return self.max_cestujicich <= other.max_cestujicich

    def __gt__(self, other):
        return self.max_cestujicich > other.max_cestujicich

    def __ge__(self, other):
        return self.max_cestujicich >= other.max_cestujicich

letadlo1 = Letadlo(typ=input('Zadej název letadla 1: '), max_cestujicich=input('Zadej max cestujících: '))
letadlo2 = Letadlo(typ=input('Zadej název letadla 2: '), max_cestujicich=input('Zadej max cestujících: '))


print(f"Typ letadla 1: {letadlo1.typ}")
print(f"Maximální počet cestujících na palubě letadla 1: {letadlo1.max_cestujicich}")
print(f"Aktuální počet cestujících na palubě letadla 1: {letadlo1.aktualni_cestujici}")

letadlo1 += 200
print(f"Po přidání 200 cestujících: {letadlo1.aktualni_cestujici}")

if letadlo1 == letadlo2:
    print("Typy letadel jsou stejné.")
else:
    print("Typy letadel nejsou stejné.")

if letadlo1 > letadlo2:
    print("Letadlo 1 má větší kapacitu než letadlo 2.")
else:
    print("Letadlo 1 nemá větší kapacitu než letadlo 2.")
