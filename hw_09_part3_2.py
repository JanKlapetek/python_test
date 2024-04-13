class TeplotniPrevodnik:
    def __init__(self):
        self.pocet_prepoctu = 0

    @staticmethod
    def celsius_na_f(teplota_c):
        teplota_f = (teplota_c * 1.8) + 32
        return teplota_f


