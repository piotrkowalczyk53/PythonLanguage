n = 5
import glob
import numpy

#ZAD1
print("Zadanie 1")
def fun1(name, amount):
    with open(name) as data:
        lines = data.readlines()
        print(lines[:amount])
        print(lines[-amount:])
        print(lines[::amount])
        print([i.split(" ")[amount-1] for i in lines if len(i.split(" ")) >=amount])
        print([i[amount-1] for i in lines if len(i) >=amount])
fun1("data/data1.in", n)
print()

#ZAD2
print("Zadanie 2")
matching_files = glob.glob("data*.in")
all_lines = []
with open("data.out", "w") as result:
    for i in range(len(matching_files)):
        with open(matching_files[i]) as data:
            lines = data.readlines()
            all_lines.append(lines)
    for i in range(max(map(len, all_lines))):
        result.write(str(i) + " ")
        temp = []
        for j in range(len(all_lines)):
            temp.append(float(all_lines[j][i]))
        result.write("%f %f\n"%(numpy.average(temp), numpy.std(temp)))
print()

#ZAD3
print("Zadanie 3")
def fun3():
    with open("instructions.py", "w") as result:
        result.write('''import matplotlib.pyplot as plt
import glob
import numpy
x, yav, ydev = numpy.loadtxt("data.out", unpack=True)
#wyrysowanie krzywej y(x) wraz z niepewnościami
plt.errorbar(x, yav, marker='*', yerr=ydev)
#
matching_files = glob.glob("data*.in")
for file in matching_files:
    with open(file):
        y = numpy.loadtxt(file, unpack=True)
    plt.plot(x, y, 'o')
#opis osi
plt.xlabel('x')
#zapis do pliku, format określony przez rozszerzenie w nazwie
plt.savefig('res.pdf')''')
fun3()
print()

# #ZAD4
# print("Zadanie 4")
# with open("general_ranking.out", "w") as result:
#     matching_files = glob.glob("rankings/20*.txt")
#     for file in matching_files:

# print()