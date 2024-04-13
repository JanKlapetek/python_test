class Zvire:
    def zvuk(self):
        pass

class Pes(Zvire):
    def zvuk(self):
        return "Haf!"

class Kocka(Zvire):
    def zvuk(self):
        return "Mňau!"

def vypis_zvuk(zvire):
    print(zvire.zvuk())

# Použití polymorfismu
pes = Pes()
kocka = Kocka()

vypis_zvuk(pes)  # Vypíše: "Haf!"
vypis_zvuk(kocka)  # Vypíše: "Mňau!"