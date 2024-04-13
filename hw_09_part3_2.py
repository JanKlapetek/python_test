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
            TeplotniPrevodnik.f_na_celsius(teplota)
        else:
            return 'Neplatná jednotka! Zadej C nebo F! '

teplotni_prevodnik = TeplotniPrevodnik()
teplota_celsius = 37.5
teplota_fahrenheit = teplotni_prevodnik.preved(teplota_celsius,'c')

print(f"{teplota_celsius} stupně Celsia se rovná {teplota_fahrenheit:.1f} stupně Fahrenheita.")
print(f"Počet provedených přepočtů: {teplotni_prevodnik.zjisti_pocet_prepoctu()}")


