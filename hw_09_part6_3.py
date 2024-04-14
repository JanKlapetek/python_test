import pickle
class Tvar:
    def __init__(self, nazev):
        self.nazev = nazev
    def zobraz(self):
        print(f'Typ tvaru je: {self.nazev}')
    def uloz(self, soubor):
        with open(soubor, 'wb') as f:
            pickle.dump(self,f)

    @staticmethod
    def nacti(soubor):
        with open(soubor, 'rb') as f:
            return pickle.load(f)



