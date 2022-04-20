import sys
import string

#ZAD1
print("Zadanie 1")
if len(sys.argv) == 1:
    print('Brak argumentow wywolania!')
    sys.exit()
text = ''.join(sys.argv[1:])
print(text)
print()

#ZAD2
print("Zadanie 2")
lower = [i for i in text if i.islower()]
upper = [i for i in text if i.isupper()]
digits = [i for i in text if i.isnumeric()]
others = [i for i in text if i not in lower and i not in upper and i not in digits]
print(lower)
print(upper)
print(digits)
print(others)
print()

#ZAD3
print("Zadanie 3")
lowerNoRep = []
for i in lower:
    if i not in lowerNoRep:
        lowerNoRep.append(i)
newList = [(i, text.count(i)) for i in lowerNoRep]
print(lowerNoRep)
print(newList)
print()

#ZAD4
print("Zadanie 4")
for i, j in sorted(newList, key = lambda x: x[1], reverse=True):
    print(i, j)
print()

#ZAD5
print("Zadanie 5")
vowels = ('a', 'A', 'e', 'E', 'i', 'I', 'y', 'Y', 'u', 'U', 'o', 'O')
a = 0
for i in vowels:
    a += text.count(i)
b = 0
for i in string.ascii_letters:
    if i not in vowels:
        b += text.count(i)
anotherList = [(int(i), a * int(i) + b) for i in string.digits]
print(anotherList)
print()

#ZAD6
print("Zadanie 6")
averageX = sum(x for x, y in anotherList)
averageX /= len(anotherList)
D = sum((x - averageX) ** 2 for x, y in anotherList)
a = sum(y * (x - averageX) for x, y in anotherList)
a /= D
averageY = sum(y for x, y in anotherList)
averageY /= len(anotherList)
b = averageY - a * averageX
print('a =', a)
print('D =', D)
print('b =', b)
