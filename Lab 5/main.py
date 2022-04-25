import time
from sys import version
import random
import functools

# dodawanie elementu
# forStatement         => 353102732
# listComprehension    => 193871348
# mapFunction          => 393253187
# generatorExpression  => 343366

# dodawanie elementu do kwadratu podniesionego
# forStatement         => 2032106760
# listComprehension    => 1884103126
# mapFunction          => 326884
# generatorExpression  => 507740

#sumowanie petla for (i dodawanie elementu)
# forStatement         => 1285087734
# listComprehension    => 944449741
# mapFunction          => 1213847006
# generatorExpression  => 1017881662

#sumowanie funckja sum (i dodawanie elementu)
# forStatement         => 406572370
# listComprehension    => 233464900
# mapFunction          => 404717659
# generatorExpression  => 293056594

#konwersja do listy (po dodaniu elementu)
# mapFunction          => 441671552
# generatorExpression  => 326484175


powt=1000
N=10000

def forStatement():
    result = []
    for i in range(N):
        result.append(i)
        # result.append(i**2)
    return result

def listComprehension():
    return [i for i in range(N)]
    # return [i**2 for i in range(N)]

def mapFunction():
    return map(lambda x: x, range(N))
    # return map(lambda x: x**2, range(N))
    # return list(map(lambda x: x, range(N)))

def generatorExpression():
    return (i for i in range(N))
    # return (i**2 for i in range(N))
    # return list((i for i in range(N)))

def tester(x):
    a = time.time_ns()
    temp = 0
    for i in range(powt):
        p = x()
        # for j in p:
            # temp += j
        # sum(p)
    b = time.time_ns()
    return b - a
    

print(version)
test=(forStatement, listComprehension, mapFunction, generatorExpression)
for testFunction in test:
    print(testFunction.__name__.ljust(20), '=>', tester(testFunction))

print()

#ZAD2
print("Zadanie 2")
def integral(fun, steps, x0, xk):
    dx = (xk-x0)/steps
    return sum(map(fun, (x0 + step*(dx) for step in range(steps))))/steps
print(integral(lambda x: x**2, N, 0, 1))
print()

#ZAD3
print("Zadanie 3")
print(4*len(list(filter(lambda x: x <= 1, (random.uniform(-1,1)**2 + random.uniform(-1,1)**2 for _ in range(N)))))/N)
print()

#ZAD5
print("Zadanie 5")
def fitting(xl, yl):
    averageX = sum(xl) / len(xl)
    averageY = sum(yl) / len(yl)
    D = functools.reduce(lambda x, y: x+y, map(lambda x: (x - averageX)**2, xl))
    a = functools.reduce(lambda x, y: x+y, map(lambda x, d: d*(x - averageX), xl, yl)) / D
    b = averageY - a * averageX
    return a, b
print(fitting([2,3,4,5,6], [3,4,7,4,1]))
print()
