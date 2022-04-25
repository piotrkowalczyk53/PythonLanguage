import random
import string

#ZAD1
k = 6
print("Zadanie 1")
lista = [random.randrange(5*k) for i in range(k)]
print(lista)
listaNiemieszana = lista.copy()
szalonySlowniczek = {i: 0 for i in range(100)}
for i in range(100):
    random.shuffle(lista)
    for j in range(len(lista)):
        if lista[j] == listaNiemieszana[j]:
            szalonySlowniczek[i] += 1
    listaNiemieszana = lista.copy()
print(szalonySlowniczek)
print()

#ZAD2
print("Zadanie 2")
for i in range(k):
    kropkiNienawisci = '.'.join(random.choices(string.ascii_lowercase, k=k))
print(kropkiNienawisci)
print()

#ZAD3A
print("Zadanie 3A")
lista = [random.randrange(20) for i in range(100)]
szalonySlowniczek = {}
for i in range(20):
    l = [j for j, x in enumerate(lista) if x == i]
    szalonySlowniczek.setdefault(i, l)
print(lista)
print(szalonySlowniczek)
print()

#ZAD3B
print("Zadanie 3B")
lista = [random.randrange(20) for i in range(100)]
szalonySlowniczek = {}
for i in range(20):
    l = []
    k = 0
    for j in lista:
        k += 1
        if j == i:
            l.append(lista.index(i, k-1))
    szalonySlowniczek.setdefault(i, l)
print(lista)
print(szalonySlowniczek)
print()

# #ZAD4
# print("Zadanie 4")
# n = random.randint(3, 6)
# liczba = random.rand
# slownik = {random.randint()}
# print()

#ZAD5
print("Zadanie 5")
d1 = {i: random.randint(1, 99) for i in range(10)}
d2 = {i: random.randint(1, 99) for i in range(10)}
print(d1)
print(d2)
d1 = {v: i for i, v in d1.items()}
d2 = {v: i for i, v in d2.items()}
print(d1)
print(d2)
d3 = {i: (d1, d2) for i in d1 if i in d2}
print()
