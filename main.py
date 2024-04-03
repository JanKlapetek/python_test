uzivatele = {
    'alice': 'heslo123',
    'bob': 'tajneHeslo456',
    'charlie': 'superTajneHeslo789'
}

def prihlaseni():
    uziv_jmeno = input("Zadej uživatelské jméno: ")
    heslo = input("Zadej heslo: ")

    if uziv_jmeno in uzivatele and uzivatele[uziv_jmeno] == heslo:
        print(f"Vítej, {uziv_jmeno}! Jsi úspěšně přihlášen.")
    else:
        print("Chybné uživatelské jméno nebo heslo.")

prihlaseni()
print('Hello world')
