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

