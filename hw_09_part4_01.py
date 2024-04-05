# Vytvořte třídu Device obsahující informace o zařízení.
# Pomocí dědičnosti implementujte třídu CoffeeMachine (obsahuje informace o kávovaru),
# třídu Blender (obsahuje informace o mixéru), třídu MeatGrinder (obsahuje informace o mlýnku na maso).
# Každá třída musí mít požadované metody.

class Device:
    def __init__(self, znacka, model):
        self.znacka = znacka
        self.model = model

    def ziskej_info(self):
        return f'Zařízení: {self.znacka} {self.model}'

class Coffee_machine(Device):
    def __init__(self, znacka, model, druh_kavy):
        super().__init__(znacka, model)
        self.druh_kavy = druh_kavy
    def udelat_kavu(self):
        return f'Příprava kávy {self.druh_kavy}'

class Blender(Device):
    def __init__(self, znacka, model, rychlost):
        super().__init__(znacka, model)
        self.rychlost = rychlost

    def udelej_mix(self):
        return f'Příprava smoothie na rychlost: {self.rychlost}'

