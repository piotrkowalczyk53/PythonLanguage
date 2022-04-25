a = [1, 2, 3, 4, 5, 6, 7]
import random
import math

#ZAD1
print("Zadanie 1a")
def fibonacci():
    a, b = 0, 1
    yield a
    yield b
    while True:
        yield a + b
        a, b = a + b, a
print()

print("Zadanie 1b")
def onlyOddOrEven(seq, w = True):
    yield from filter(lambda x: x%2 if w else not x%2, seq)
for el in onlyOddOrEven(a, w=False):
    print(el)
print()

print("Zadanie 1c")
def lessOrEqualTo(seq, w):
    for el in seq:
        if el > w:
            return
        yield el
for el in lessOrEqualTo(a, 5):
    print(el)
print()

print("Zadanie 1d")
print(sum(lessOrEqualTo(onlyOddOrEven(fibonacci()),100)))
print()

#ZAD2
print("Zadanie 2")
def randomWalk(start):
    while True:
        yield start
        start += random.uniform(-0.4, 0.4)
        if start < 0.1:
            return
for el in randomWalk(1):
    print(el)
print()

#ZAD4
print("Zadanie 4")
def pascal(steps):
    row = []
    for j in range (steps):
        row = [row[i-1] + row[i] if i < len(row) and i > 0 else 1 for i in range(len(row)+1)]
        yield (j, row, sum(row))
for el in pascal(8):
    print(el)
print()

#ZAD5
print("Zadanie 5")
def sinus(x, eps):
    suma = 0
    k=0
    while math.fabs(math.sin(x) - suma) > eps:
        temp = ((-1)**k/math.factorial(1+2*k))*x**(1+2*k)
        suma += temp
        yield suma, k
        k += 1
for el in sinus(math.pi/2, 10**(-8)):
    print(el)
print()
