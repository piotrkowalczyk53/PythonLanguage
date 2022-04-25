import sys
import random
import string

#ZAD1
print("Zadanie 1")
def zad1(funkcja):
    stale = string.ascii_letters.replace("x", "")
    wartosciStalych = ''.join([str(random.randrange(10)) for _ in range(len(stale))])
    p = str.maketrans(stale, wartosciStalych)
    return [(x := random.random(), eval(funkcja.translate(p))) for _ in range(10)]
print(zad1(sys.argv[1]))
print()

#ZAD2
print("Zadanie 2")
def zad2(*parametry):
    dlugosc = len(parametry)
    lista = []
    for i in parametry[0]:
        for j in parametry:
            if i not in j:
                break
            else:
                if i not in lista:
                    lista.append(i)
    return lista
print(zad2('b', 'b', ('a', 'b')))
print()

#ZAD3
print("Zadanie 3")
def zad3(sekwencja1, sekwencja2, parametr=True):
    dlugosc1 = len(sekwencja1)
    dlugosc2 = len(sekwencja2)
    lista = []
    if parametr:
        dlugosc = min(dlugosc1, dlugosc2)
    else:
        dlugosc = max(dlugosc1, dlugosc2)
    for i in range(dlugosc):
        if i not in range(min(dlugosc1, dlugosc2)):
            lista.append((sekwencja1[i], None))
        else:
            lista.append((sekwencja1[i], sekwencja2[i]))
    return lista
    # lista = [(sekwencja1[i], sekwencja2[i]) for i in range(dlugosc) if i < min(dlugosc1, dlugosc2)]
print(zad3((1, 2, 3), (3, 4), parametr=False))
print()

#ZAD4
print("Zadanie 4")
def zad4(kwota, nominaly = (10, 5, 2)):
    wydane = {i: 0 for i in nominaly}
    while kwota > 0:
        for i in nominaly:
            if i <= kwota:
                kwota -= i
                wydane[i] += 1
                break
        else:
            break
    return wydane
print(zad4(68))
print()

#ZAD5
print("Zadanie 5")
def zad5(zgadywana, granica_dolna, granica_gorna, parametr='r'):
    kroki = 0

    while True:
            kroki += 1
            srodek = random.randint(granica_dolna, granica_gorna) if parametr == 'r' else (granica_gorna + granica_dolna) // 2
            if srodek == zgadywana:
                break
            elif srodek <= zgadywana:
                granica_dolna = srodek
            else:
                granica_gorna = srodek
    return kroki
print(zad5(68, 1, 70, 'g'))
print()
