from math import sin, tan, log, radians  # import funkcí z modulu math

# definice proměnných
poledniky = []
rovnobezky = []


def nahrad_vysoke_hodnoty(a, seznam):
    """nahrazuje hodnoty y větší něž 100 cm a menší než - 100 cm pomlčkou"""
    if a > 100 or a < -100:
        seznam.append('-')
    else:
        a = round(a, 1)
        seznam.append(a)


def pol_vse(polomer, meritko, poledniky):
    """počítá vzdálenosti poledníků pro všechny zobrazení"""
    for v in range(-180, 190, 10):  # rozsah poledníků
        x = (polomer * radians(v))/meritko  # vzorec výpočtu, převod na radiány a do měřítka
        nahrad_vysoke_hodnoty(x, poledniky)


def rov_lam(polomer, meritko, rovnobezky):
    """počítá vzdálenosti rovnoběžek pro Lambertovo zobrazení"""
    for u in range(-90, 100, 10):
        y = (polomer * sin(radians(u)))/meritko
        nahrad_vysoke_hodnoty(y, rovnobezky)


def rov_mar(polomer, meritko, rovnobezky):
    """počítá vzdálenosti rovnoběžek pro Marinovo zobrazení"""
    for u in range(-90, 100, 10):
        y = (polomer * radians(u))/meritko
        nahrad_vysoke_hodnoty(y, rovnobezky)


def rov_bra(polomer, meritko, rovnobezky):
    """počítá vzdálenosti rovnoběžek pro Braunovo zobrazení"""
    for u in range(-90, 100, 10):
        y = (2 * polomer * tan(radians(u) / 2))/meritko
        nahrad_vysoke_hodnoty(y, rovnobezky)


def rov_mer(polomer, meritko, rovnobezky):
    """počítá vzdálenosti rovnoběžek pro Mercatorovo zobrazení"""
    for u in range(180, -10, -10):
        if u == 0 or u == 180:  # podmínkou if ošetřeny póly, které se v Mercatorově tobrazení nezobrazují
            y = 200
        else:
            y = (polomer * log(1 / tan(radians(u)/2)))/meritko
        nahrad_vysoke_hodnoty(y, rovnobezky)


print('Výpočet vybraných válcových zobrazení')

# výběr daného zobrazení, funkcí while ošetřeny nekorektní vstupy
zobrazeni = input('Zadej zkratku zobrazení:\nL - Lambertovo\nA - Marinovo\nB - Braunovo\nM - Mercatorovo\n')
while zobrazeni != 'L' and zobrazeni != 'A' and zobrazeni != 'B' and zobrazeni != 'M':
    zobrazeni = input('Špatně zadaná zkratka zobrazení. Zkus to znova, zadej zkratku zobrazení:\nL - Lambertovo\nA - '
                      'Marinovo\nB - Braunovo\nM - Mercatorovo\n')

# výběr měřítka, funkcí while ošetřeny nekorektní vstupy (string), převod na integer
while True:
    meritko = int(input('Zadej měřítko - 1 : '))
    if meritko > 0:
        break
    else:
        print('Špatně zadané měřítko, zkus to znovu.')

# výběr poloměru, funkcí while ošetřeny nekorektní vstupy (string), převod na float, převod na cm
while True:
    polomer = float(input('Zadej poleměr Země v km. Pro poloměr 6371,11 km zadej \"0\"\n'))
    if polomer > 0:
        polomer = polomer * 100000
        break
    elif polomer == 0:
        polomer = 637111000
        break
    else:
        print('Špatně zadaný poloměr, zkus to znovu.')

# volání funkcí podle zvoleného zobrazení
pol_vse(polomer, meritko, poledniky)
if zobrazeni == 'L':
    rov_lam(polomer, meritko, rovnobezky)
    print('Lambertovo zobrazení')
if zobrazeni == 'A':
    rov_mar(polomer, meritko, rovnobezky)
    print('Marinovo zobrazení')
if zobrazeni == 'B':
    rov_bra(polomer, meritko, rovnobezky)
    print('Braunovo zobrazení')
if zobrazeni == 'M':
    rov_mer(polomer, meritko, rovnobezky)
    print('Mercatorovo zobrazení')

# vytisknutí vzdáleností poledníků a rovnoběžek
print(f"Poledníky: {poledniky} cm\nRovnoběžky: {rovnobezky} cm")