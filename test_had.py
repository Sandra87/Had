# -*- coding: utf-8 -*-
import pytest, pohyb, had

def test_pohyb():
    'Přidání nové pozice'
    souradnice = [(0, 0)]
    osa_x = souradnice[-1][0]
    osa_y = souradnice[-1][1]
    osa_y +=1
    souradnice.append((osa_x, osa_y))
    assert len(souradnice) == 2
    assert souradnice[1] == (0, 1)

def test_append():
    souradnice = [(0, 0)]
    for i in range(5):
        souradnice.append((2, 1))

    assert len(souradnice) == 6

def test_konec_hry():
    'Korektní ukončení hry'
    with pytest.raises(ValueError):
        pohyb.pohyb([(0, 7), (0, 8), (0, 9)], "v", [(2, 3)])
        pohyb.pohyb([(7, 0), (8, 0), (9, 0)], "j", [(2, 3)])
        pohyb.pohyb([(2, 0), (1, 0), (0, 0)], "s", [(2, 3)])
        pohyb.pohyb([(9, 2), (9, 1), (9, 0)], "z", [(2, 3)])

        pohyb.pohyb([(0, 7), (0, 8), (0, 9)], "z", [(2, 3)])
        pohyb.pohyb([(7, 0), (8, 0), (9, 0)], "s", [(2, 3)])
        pohyb.pohyb([(2, 0), (1, 0), (0, 0)], "j", [(2, 3)])
        pohyb.pohyb([(9, 2), (9, 1), (9, 0)], "v", [(2, 3)])

def test_index():
    'Přístup k jednotlivým souřadnicím v rámci pozice'
    souradnice = [(0, 0), (0, 1), (0, 2)]
    assert souradnice[-1][0] == 0
    assert souradnice[-1][1] == 2

def test_smer_pohybu():
    pohyb.pohyb([(0, 0), (0, 1), (0, 2)], "v", [(2, 3)])
    assert len(souradnice) == 3
    assert souradnice[0] == (0, 1)
    assert souradnice[2] == (0, 3)
