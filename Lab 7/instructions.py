import matplotlib.pyplot as plt
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
plt.savefig('res.pdf')