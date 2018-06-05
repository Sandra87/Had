# -*- coding: utf-8 -*-
import pohyb, random
from threading import Timer

def nakresli_mapu(vyska, sirka, souradnice, potrava):
    'Vypíše aktuální stav na hracím poli'
    seznam_radku = []
    for pocet_radku in range(vyska):
        radek = []
        for pocet_pozic in range(sirka):
            radek.append('.') # na každé pozici v řádku bude '.'
        seznam_radku.append(radek)
    for pozice in souradnice:
        seznam_radku[pozice[0]][pozice[1]] = 'X' # kde je had, nahradí '.' za 'X'
    for pozice in potrava:
        seznam_radku[pozice[0]][pozice[1]] = '?' # kde je potrava,  nahradí '.' za '?'
    return seznam_radku

def po_limitu():
    'po upynutí limitu vyvolá výjimku'
    raise ValueError("Time's up !!!")
    #moznosti =["s", "j", "v", "z"]
    #smer = random.choice(moznosti)

def had_hra(vyska, sirka):
    """Průběh hry.
    Zeptá se uživatele na směr pohybu, zavolá fci pohyb a vypíše stav.
    Každých 30 tahů přidá novou potravu."""
    count = 0 # počítadlo tahů
    souradnice = [(0, 0), (0, 1), (0, 2)] # had
    potrava = [(2, 3)]
    while True:
        limit = 10 # časový limit
        t = Timer(limit, po_limitu) # co se má stát po uplynutí limitu
        t.start() # začátek odpočtu
        smer = input("Máš %d sekund. Vyber si směr a zadej s, j, v nebo z:" % limit)
        t.cancel() # zrušení odpočtu (uživatel to stihl)
        pohyb.pohyb(sirka, vyska, souradnice, smer, potrava)
        tabulka = nakresli_mapu(sirka, vyska,souradnice, potrava)
        # výpis stavu hry
        for radek in tabulka:
            for pozice in radek:
                print(pozice, end = ' ')
            print()
        count+=1 # tah se zvýší o 1

        if count == 30: # každých třicet tahů
            radky = random.randrange(vyska) # náhodně zvolený řádek
            sloupce =  random.randrange(sirka) # náhodně zvolený sloupec

            # dokud je zvolená pozice obsazená
            while (radky, sloupce) in souradnice or (radky, sloupce) in potrava:
                radky = random.randrange(vyska) # hledej dál
                sloupce =  random.randrange(sirka)

            potrava.append((radky, sloupce)) # ulož zvolenou pozici do seznamu potrava
            count = 0 # vynuluje počet tahů
