class TeplotniPrevodnik:
    pocet_prepoctu = 0

    @staticmethod
    def celsius_na_f(teplota_c):
        teplota_f = (teplota_c * 1.8) + 32
        return teplota_f

    @staticmethod
    def f_na_celsius(teplota_f):
        teplota_c = (teplota_f - 32) / 1.8
        return teplota_c

    @staticmethod
    def zjisti_pocet_prepoctu():
        return TeplotniPrevodnik.pocet_prepoctu

    @staticmethod
    def preved(teplota, jednotka):
        if jednotka.lower() == 'c':
            TeplotniPrevodnik.pocet_prepoctu += 1
            return TeplotniPrevodnik.celsius_na_f(teplota)
        elif jednotka.lower() == 'f':
            TeplotniPrevodnik.pocet_prepoctu += 1
            return TeplotniPrevodnik.f_na_celsius(teplota)
        else:
            return 'Neplatná jednotka! Zadej C nebo F!'

teplotni_prevodnik = TeplotniPrevodnik()

while True:
    try:
        volba = input("Zadej 'C' pro stupně Celsia nebo 'F' pro stupně Fahrenheita (nebo 'exit' pro ukončení): ")
        if volba.lower() == 'exit':
            break

        teplota = float(input("Zadej teplotu: "))
        prevedena_teplota = teplotni_prevodnik.preved(teplota, volba)
        if volba.lower() == 'c':
            print(f"Zadaná teplota se rovná {prevedena_teplota:.1f} stupňů Fahrenheita.")
        elif volba.lower() == 'f':
            print(f"Zadaná teplota se rovná {prevedena_teplota:.1f} stupňů Celsia.")
    except ValueError:
        print("Neplatný vstup! Zadej číslo jako teplotu.")
        continue

print(f"Program ukončen. \nPočet provedených přepočtů: {teplotni_prevodnik.zjisti_pocet_prepoctu()}")