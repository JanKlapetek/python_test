def main():
    # Inicializace prázdného seznamu
    seznam = []

    while True:
        print("\nNabídka:")
        print("1. Přidat nové číslo do seznamu")
        print("2. Odstranit všechny výskyty čísla ze seznamu")
        print("3. Zobrazit obsah seznamu")
        print("4. Zkontrolovat, zda seznam obsahuje určité číslo")
        print("5. Nahradit hodnotu v seznamu")
        volba = input("Zadejte číslo akce (1-5) nebo 'konec' pro ukončení: ")

        if volba == "1":
            cislo = int(input("Zadejte číslo, které chcete přidat do seznamu: "))
            if cislo not in seznam:
                seznam.append(cislo)
                print(f"Číslo {cislo} bylo přidáno do seznamu.")
            else:
                print(f"Číslo {cislo} již v seznamu existuje.")

        elif volba == "2":
            cislo = int(input("Zadejte číslo, které chcete odstranit ze seznamu: "))
            if cislo in seznam:
                seznam.remove(cislo)
                print(f"Číslo {cislo} bylo odstraněno ze seznamu.")
            else:
                print(f"Číslo {cislo} není v seznamu.")

        elif volba == "3":
            vypis_seznam(seznam)

        elif volba == "4":
            cislo = int(input("Zadejte číslo, které chcete zkontrolovat v seznamu: "))
            if cislo in seznam:
                print(f"Číslo {cislo} je v seznamu.")
            else:
                print(f"Číslo {cislo} není v seznamu.")

        elif volba == "5":
            stare_cislo = int(input("Zadejte číslo, které chcete nahradit: "))
            nove_cislo = int(input("Zadejte nové číslo: "))
            if stare_cislo in seznam:
                index = seznam.index(stare_cislo)
                seznam[index] = nove_cislo
                print(f"Číslo {stare_cislo} bylo nahrazeno číslem {nove_cislo}.")
            else:
                print(f"Číslo {stare_cislo} není v seznamu.")

        elif volba.lower() == "konec":
            break

        else:
            print("Neplatná volba. Zadejte číslo od 1 do 5 nebo 'konec'.")

def vypis_seznam(seznam):
    if seznam:
        print("Obsah seznamu:")
        for cislo in seznam:
            print(cislo)
    else:
        print("Seznam je prázdný.")

if __name__ == "__main__":
    main()

