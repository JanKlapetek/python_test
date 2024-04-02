import datetime


def float_to_datetime(float_number):
    try:
        # Převod float na celé číslo (sekundy)
        seconds = int(float_number)

        # Vytvoření timedelta objektu s daným počtem sekund
        time_delta = datetime.timedelta(seconds=seconds)

        # Získání aktuálního data a času
        current_datetime = datetime.datetime.now()

        # Přidání timedelta k aktuálnímu datu a času
        result_datetime = current_datetime + time_delta

        return result_datetime
    except ValueError:
        return "Chyba: Zadejte platné číslo typu float."


# Zadejte libovolné číslo typu float
input_float = 1234.56
converted_datetime = float_to_datetime(input_float)

print(f"Zadané číslo {input_float} odpovídá času: {converted_datetime}")
def cas_jeti_linky(tuny):
    dt_now = datetime.datetime.now()
    print(dt_now)
    pocet_hodin_jeti_linky = tuny / 14
    pocet_hodin_jeti_linky
    vysledek = dt_now + pocet_hodin_jeti_linky

    formatovany_cas = vysledek.strftime("%Y-%m-%d %H:%M:%S")
    print(f'Formátovaný čas je: {formatovany_cas}')

    # Vytvoření dvou časových bodů
    cas1 = datetime.datetime(2024, 3, 27, 10, 30, 0)  # První čas
    cas2 = datetime.datetime(2024, 3, 27, 14, 45, 0)  # Druhý čas

    # Rozdíl mezi časy
    rozdil = cas2 - cas1

    # Výstup
    print(f"Rozdíl mezi časy: {rozdil}")
    print(f'Linka dojede v {vysledek}')

kolik_tun = (float(input('Zadej kolik tun se má udělat: ')))

cas_jeti_linky(kolik_tun)


