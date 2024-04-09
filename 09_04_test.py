class Vehicle:
    def __init__(self, rychlost, vaha):
        self.rychlost = rychlost
        self.vaha = vaha

    def ziskej_info(self):
        print(f'Rychlost: {self.rychlost}')
        print(f'Váha: {self.vaha}')

class Kamion(Vehicle):
    def __init__(self,rychlost,vaha, checkSpeedLimitObec, checkSpeedLimit_dalnice):
        super().__init__(rychlost,vaha)
        self.CheckSpeedLimitObec = checkSpeedLimitObec
        self.CheckSpeedLimitDalnice = checkSpeedLimit_dalnice

    def jedes_rychle(self,rychlost):
        if rychlost > 50:
            print(f'Jedeš rychleji než je povoleno v obci! Tvá rychlost je: {self.rychlost}')

auto1 = Vehicle(100,800)
kamion1 = Vehicle(110, 1000)




