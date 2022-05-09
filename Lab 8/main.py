import lab8
import matplotlib.pyplot as plt
import datetime


#help(lab8)
#help(lab8.translation)
#help(lab8.checkPESEL)
#help(lab8.meanAge)

#TASK 1
try:
    x = [0]
    y = [0]
    for i in range(10000): 
        tx, ty = lab8.translation(((0,0,0,0,0.16,0), (0.2,-0.26,0,0.23,0.22,1.6), (-0.15,0.28,0,0.26,0.24,0.44), (0.85,0.04,0,-0.04,0.85,1.6)), (0.01, 0.07, 0.07, 0.85), x = x[i], y = y[i])
        x.append(tx)
        y.append(ty)
    plt.plot(x, y, '.')
    plt.savefig('result.pdf')

except Exception as exc:
    print(exc.args)


#TASK 2
try:
    lab8.checkPESEL("02070803628", datetime.date(1902, 7, 8), "k")
except ValueError:
    print("Podano niepoprawna date urodzenia")
except Exception as exc:
    print(exc.args)


#TASK 3
try:
    print(lab8.meanAge(1))
except Exception as exc:
    print(exc.args)
