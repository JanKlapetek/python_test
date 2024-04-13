class MyClass:
    def __init__(self):
        # Veřejný atribut
        self.public_attribute = "Veřejný atribut"

        # Privátní atribut (používáme dvojité podtržítko)
        self.__private_attribute = "Privátní atribut"

        # Chráněný atribut (používáme jednoduché podtržítko)
        self._protected_attribute = "Chráněný atribut"

    def public_method(self):
        # Veřejná metoda
        return "Toto je veřejná metoda."

    def __private_method(self):
        # Privátní metoda
        return "Toto je privátní metoda."

    def _protected_method(self):
        # Chráněná metoda
        return "Toto je chráněná metoda."

# Vytvoření instance třídy
objekt = MyClass()

# Přístup k atributům a metodám
print(objekt.public_attribute)  # Veřejný atribut
print(objekt.public_method())    # Veřejná metoda

# Privátní atribut a metoda nejsou přístupné zvenčí
# print(objekt.__private_attribute)  # Chyba!
# print(objekt.__private_method())    # Chyba!

# Chráněný atribut a metoda jsou přístupné, ale jsou označeny jako chráněné
print(objekt._protected_attribute)  # Chráněný atribut
print(objekt._protected_method())    # Chráněná metoda