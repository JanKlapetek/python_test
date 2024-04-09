class Vehicle:
    def __init__(self, rychlost, vaha):
        self.rychlost = rychlost
        self.vaha = vaha

    def ziskej_info(self):
        print(f'Rychlost: {self.rychlost}')
        print(f'Váha: {self.vaha}')

class Kamion(Vehicle):
    def __init__(self,rychlost,vaha, zatizeni):
        super().__init__(rychlost, vaha)
        self.zatizeni = zatizeni


    def limit_dalnice(self):
        if self.rychlost > 100:
            return 'Pokuta!'
        elif self.rychlost < 80:
            return 'Pokuta, jedeš pomalu!'
        else:
            return 'Není pokuta!'

kamion = Kamion(150, 2000, 500)
print(kamion.limit_dalnice())


