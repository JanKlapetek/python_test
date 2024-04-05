# Vytvořte třídu Device obsahující informace o zařízení.
# Pomocí dědičnosti implementujte třídu CoffeeMachine (obsahuje informace o kávovaru),
# třídu Blender (obsahuje informace o mixéru), třídu MeatGrinder (obsahuje informace o mlýnku na maso).
# Každá třída musí mít požadované metody.

class Device:
    def __init__(self, znacka, model):
        self.znacka = znacka
        self.model = model


    def