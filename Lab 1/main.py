#ZAD1
print("Zadanie 1")
k = [2, 2, 3, 4, 5, 2, 2, 2, 5, 6,]
c = k[:]
print(k)
n = 2
for i in c:
    if (i == n):
        k.remove(n)
print(k)
print()

#ZAD2
print("Zadanie 2")
k = [2, 2, 3, 4, 5, 2, 2, 2, 5, 6,]
print(k)
while n in k:
        k.remove(n)
print(k)
print()

#ZAD3
print("Zadanie 3")
k = [2, 2, 3, 4, 5, 2, 2, 2, 5, 6,]
print(k)
for i in range(0, len(k), 2):
    print(k[i])
print()

#ZAD4
print("Zadanie 4")
k = [2, 2, 3, 4, 5, 2, 2, 2, 5, 6,]
for i in k[::2]:
    print(i)
print()

#ZAD5
print("Zadanie 5")
k = [2, 2, 3, 4, 5, 2, 2, 2, 5, 6,]
print(k)
for i in range(len(k)-1, 0, -2):
    print(k[i])
print()

#ZAD6
print("Zadanie 6")
k = [2, 2, 3, 4, 5, 2, 2, 2, 5, 6,]
print(k)
for i in k[::-2]:
    print(i)
print()

#ZAD7
print("Zadanie 7")
k = [2, 2, 3, 4, 5, 2, 2, 2, 5, 6,]
print(k)
c = [(i, j) for i, j in enumerate(k)]
print(c)
print()

#ZAD8
print("Zadanie 8")
c.sort(key = lambda x: x[1])
print(c)
print()

#ZAD9
print("Zadanie 9")
k = [2, 2, 3, 4, 5, 2, 2, 2, 5, 6,]
print(k)
c = [(i, j) for i, j in enumerate(k) if not(k[i] % 2)]
print(c)
print()

#ZAD10
print("Zadanie 10")
k = [2, 2, 3, 4, 5, 2, 2, 2, 5, 6,]
print(k)
c = [(i, k[i]) if i < k[i] else (k[i], i) for i in range(len(k))]
print(c)
print()

#ZAD11
print("Zadanie 11")
n = 10
k = 2
c = [[1 if not(j < k) and not(i < k) and not(j > n - k - 1) and not (i > n - k - 1) else 0 for j in range(n)] for i in range(n)]
print('\n'.join(map(str,c)))
print()

c = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
print('\n'.join(map(str,c)))
print()

c = [[1 if j + i == n - 1 else 0 for j in range(n)] for i in range(n)]
print('\n'.join(map(str,c)))
print()

c = [[1 if i == j or j + i == n - 1 else 0 for j in range(n)] for i in range(n)]
print('\n'.join(map(str,c)))
print()

c = [[1 if (i+j) % 2 else 0 for j in range(n)] for i in range(n)]
print('\n'.join(map(str,c)))
print()
