class Uzivatel:
    minimalni_delka_hesla = 6

    @staticmethod
    def zvaliduj_heslo(heslo):
        if len(heslo) >= Uzivatel.minimalni_delka_hesla:
            return True
        else:
            return False

print(Uzivatel.zvaliduj_heslo("heslojeveslo"))