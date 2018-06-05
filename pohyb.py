# -*- coding: utf-8 -*-
import random

def pohyb(vyska, sirka, souradnice, smer, potrava):
    'Posune hada daným směrem'
    radky = souradnice[-1][0] # index řádku pozice, kde je hlava hada
    sloupce = souradnice[-1][1] # ndex sloupce pozice, kde je hlava hada
    if smer == 'v':
        sloupce += 1 # při pohybu na východ se index sloupce zvýší o 1
        if (radky, sloupce) in souradnice: # na pozici už je had (kousnutí)
            raise ValueError('Game over !!!')
        if sloupce > sirka - 1: # pohyb mimo hrací pole
            raise ValueError('Game over !!!')
        if (radky, sloupce) not in souradnice and (radky, sloupce) not in potrava: # volné pole
            souradnice.append((radky, sloupce))
            del souradnice[0] # umazání první pozice (iluze pohybu)
        if (radky, sloupce) in potrava: # na pozici je potrava
            souradnice.append((radky, sloupce))
            potrava.remove((radky, sloupce)) # odstanění právě snězené potravy, had vyroste
        if potrava == []: # v poli už není potrava
            radky = random.randrange(vyska) # náhodně zvolený řádek
            sloupce =  random.randrange(sirka)
            if (radky, sloupce) not in souradnice: # na pozici není had
                potrava.append((radky, sloupce)) # přidání potravy
    elif smer == 'j':
        radky += 1
        if (radky, sloupce) in souradnice:
            raise ValueError('Game over !!!')
        if radky > vyska - 1:
            raise ValueError('Game over !!!')
        if (radky, sloupce) not in souradnice and (radky, sloupce) not in potrava:
            souradnice.append((radky, sloupce))
            del souradnice[0]
        if (radky, sloupce) in potrava:
            souradnice.append((radky, sloupce))
            potrava.remove((radky, sloupce))
        if potrava == []:
            radky = random.randrange(vyska)
            sloupce =  random.randrange(sirka)
            if (radky, sloupce) not in souradnice:
                potrava.append((radky, sloupce))
    elif smer == 'z':
        sloupce -= 1
        if (radky, sloupce) in souradnice:
            raise ValueError('Game over !!!')
        if sloupce < 0:
            raise ValueError('Game over !!!')
        if (radky, sloupce) not in souradnice and (radky, sloupce) not in potrava:
            souradnice.append((radky, sloupce))
            del souradnice[0]
        if (radky, sloupce) in potrava:
            souradnice.append((radky, sloupce))
            potrava.remove((radky, sloupce))
        if potrava == []:
            radky = random.randrange(vyska)
            sloupce =  random.randrange(sirka)
            if (radky, sloupce) not in souradnice:
                potrava.append((radky, sloupce))
    else:
            radky -= 1
            if (radky, sloupce) in souradnice:
                raise ValueError('Game over !!!')
            if radky < 0:
                raise ValueError('Game over !!!')
            if (radky, sloupce) not in souradnice and (radky, sloupce) not in potrava:
                souradnice.append((radky, sloupce))
                del souradnice[0]
            if (radky, sloupce) in potrava:
                souradnice.append((radky, sloupce))
                potrava.remove((radky, sloupce))
            if potrava == []:
                radky = random.randrange(vyska)
                sloupce =  random.randrange(sirka)
                if (radky, sloupce) not in souradnice:
                    potrava.append((radky, sloupce))
