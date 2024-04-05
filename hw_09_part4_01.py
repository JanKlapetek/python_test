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
class Meat_grinder(Device):
    def __init__(self, znacka, model, vykon):
        super().__init__(znacka, model)
        self.vykon = vykon

    def namel_maso(self):
        return f'Mletí masa o výkonu: {self.vykon}'
print('\n')
# Kávovar
coffee_machine = Coffee_machine('Delonghi', 'Ecam290', 'mletá káva, zrna' )
print(coffee_machine.ziskej_info())
print(coffee_machine.udelat_kavu())
print('\n')
# Mixér
blender_machine = Blender('Tefal', 'BL435', '5')
print(blender_machine.ziskej_info())
print(blender_machine.udelej_mix())
print('\n')
# Mlýnek na maso
meat_machine = Meat_grinder('Tefal', 'NE105', '1400W')
print(meat_machine.ziskej_info())
print(meat_machine.namel_maso())
print('\n')

