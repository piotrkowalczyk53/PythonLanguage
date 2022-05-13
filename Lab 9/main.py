import random
import copy
import math
keys = ("111", "110", "101", "100", "011", "010", "001", "000")

#ZAD1
print("Zadanie 1")
class Automat:
    def __init__(self, NumberOfCells, rule, random):
        self.NumberOfCells = NumberOfCells
        if random:
            self.state = [str(random.choice((0, 1))) for _ in range(NumberOfCells)]
        else:
            temp = NumberOfCells//2
            self.state = [str(1) if i == temp else str(0) for i in range(NumberOfCells)]
        self.rule = {}
        rule = bin(rule).removeprefix("0b")
        if len(rule) != 8:
            for _ in range(8 - len(rule)):
                rule = "0" + rule
        for i in range(8):
            self.rule.setdefault(keys[i], rule[i])

    def evolve(self, steps):
        tempState = []
        for _ in range(steps):
            for i in range(self.NumberOfCells):
                if i < self.NumberOfCells - 1:
                    tempState.append(self.rule.setdefault(str(self.state[i-1]) + str(self.state[i]) + str(self.state[i+1])))
                else:
                    tempState.append(self.rule.setdefault(str(self.state[i-1]) + str(self.state[i]) + str(self.state[0])))
        self.state = tempState

    def print(self, steps):
        for _ in range(steps):
            # print(str(self.state).replace("1", "*").replace("0", " "))
            for i in self.state:
                if i == "1":
                    print("*", end="")
                else:
                    print(" ", end="")
            self.evolve(1)
            print()
        print()
            
a = Automat(31, 90, False)
a.print(16)

a = Automat(31, 94, False)
a.print(16)

a = Automat(31, 182, False)
a.print(16)
print()

#ZAD2
print("Zadanie 2")
class Wektor3D:
    def __init__(self, x = 0, y = 0, z = 0):
        self.x = x
        self.y = y
        self.z = z
    
    def __add__(self, other):
        return Wektor3D(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Wektor3D(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, x):
        return Wektor3D(self.x * x, self.y * x, self.z * x)

    __rmul__ = __mul__
    
    def __str__(self):
        return '[%d, %d, %d]'%(self.x, self.y, self.z)

    def length(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    def scalarProduct(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z

    def vectorProduct(self, other):
        return Wektor3D(self.y*other.z - self.z*other.y, self.z*other.x - self.x*other.z, self.x*other.y - self.y*other.x)

    def tripleProduct(self, other, another):
        return another.scalarProduct(self.vectorProduct(other))

a = Wektor3D(2, 4, 6)
b = Wektor3D(1, 2, 5)
c = Wektor3D(3, 7, 11)
print("a: ", a)
print("b: ", b)
print("c: ", c)
print("len(b): ", b.length())
print("a+b: ", a+b)
print("Scalar product: ", a.scalarProduct(b))
print("Vector product: ", a.vectorProduct(b))
print("Triple product: ", a.tripleProduct(b, c))
print()

#ZAD3
print("Zadanie 3")
def induction(B, S):
    return B.scalarProduct(S)

def Lorentz(q, E, v, B):
    return q*(E + v.vectorProduct(B))

def LorentzWork(q, E, v):
    return q*E.scalarProduct(v)

q = 5
print(induction(a, b))
print(Lorentz(q, a, b, c))
print(LorentzWork(q, a, b))