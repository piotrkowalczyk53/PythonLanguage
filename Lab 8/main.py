"Lab 9 --- Modol zawierajacy zadania z laboratoriow"
import random
import matplotlib.pyplot as plt
import datetime
import statistics

class BadNumberOfOptions(Exception):
    pass

class BadProbability(Exception):
    pass

class BadNumberOfFactors(Exception):
    pass


def translation(fac, prop, x = 1, y = 1):
    "Zad 1 --- Funkcja dokonujaca przeksztalcenia punktu na plaszczyznie"
    if len(fac) != len(prop):
        raise BadNumberOfOptions
    if sum(prop) != 1:
        raise BadProbability
    for i in map(len, fac):
        if i != 6:
            raise BadNumberOfFactors
    chance = random.random()
    if chance >= 1 - prop[0]:
        x = fac[0][0]*x+fac[0][1]*y+fac[0][2]
        y = fac[0][3]*x+fac[0][4]*y+fac[0][5]
    elif chance < 1 - prop[0] and chance >= 1 - prop[0] + prop[1]:
        x = fac[1][0]*x+fac[1][1]*y+fac[1][2]
        y = fac[1][3]*x+fac[1][4]*y+fac[1][5]
    elif chance < 1 - prop[0] + prop[1] and chance >= 1 - prop[0] + prop[1] + prop[2]:
        x = fac[2][0]*x+fac[2][1]*y+fac[2][2]
        y = fac[2][3]*x+fac[2][4]*y+fac[2][5]
    elif chance < 1 - prop[0] + prop[1] + prop[2] + prop[3]:
        x = fac[3][0]*x+fac[3][1]*y+fac[3][2]
        y = fac[3][3]*x+fac[3][4]*y+fac[3][5]
    return x, y
try:
    x = [1]
    y = [1]
    for i in range(1000): 
        tx, ty = translation(((0,0,0,0,0.16,0), (0.2,-0.26,0,0.23,0.22,1.6), (-0.15,0.28,0,0.26,0.24,0.44), (0.85,0.04,0,-0.04,0.85,1.6)), prop=(0.01, 0.07, 0.07, 0.85), x = x[i-1], y = y[i-1])
        x.append(tx)
        y.append(ty)
    #wyrysowanie krzywej y(x), 'o' oznacza styl punktu
    plt.plot(x, y, '.')
    #opis osi
    plt.xlabel('x')
    plt.ylabel('f(x)')
    #zapis do pliku, format określony przez rozszerzenie w nazwie
    plt.savefig('res.pdf')
except BadNumberOfOptions:
    print("Ilosc krotek wspolczynnikow jest inna niz ilosc elementow krotki prawdopodobienstwa")
except BadProbability:
    print("Prawdopodobienstwo jest rozne od 100%")
except BadNumberOfFactors:
    print("Podano zla ilosc wspolczynnikow")

class BadMonth(Exception):
    pass

class BadYear(Exception):
    pass

class BadDay(Exception):
    pass

class BadGener(Exception):
    pass

class BadControl(Exception):
    pass

def checkPESEL(PESEL, date, gender):
    "Zad 2 --- Funkcja sprawdzajaca poprawnosc numeru PESEL"
    if len(PESEL) != 11:
        raise BadPESEL
    if int(PESEL[:2]) != date.year%100:
        raise BadYear
    if date.year < 1800:
        raise BadPESEL
    if date.year >= 1800 and date.year < 1900:
        if int(PESEL[2:4])+80 != date.month:
            raise BadMonth
    if date.year >= 1900 and date.year < 2000:
        if int(PESEL[2:4]) != date.month:
            raise BadMonth
    if date.year >= 2000 and date.year < 2100:
        if int(PESEL[2:4])+20 != date.month:
            raise BadMonth
    if date.year >= 2100 and date.year < 2200:
        if int(PESEL[2:4])+40 != date.month:
            raise BadMonth
    if date.year >= 2200 and date.year < 2300:
        if int(PESEL[2:4])+60 != date.month:
            raise BadMonth
    if int(PESEL[5:6]) != date.day:
        raise BadDay
    if int(PESEL[6:10]) % 2 == 0 and gender == "m":
        raise BadGener
    if int(PESEL[6:10]) % 2 == 1 and gender == "k":
        raise BadGener
    controls = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]
    control = 0
    for i in range(len(PESEL)-1):
        control = control + int(PESEL[i]) * controls[i]
    control = control % 10
    control = 10 - control
    control = control % 10
    if int(PESEL[-1]) != control:
        raise BadControl
    return True

try:
    checkPESEL("02070803628", datetime.date(1902, 7, 8), "k")
except ValueError:
    print("Podano niepoprawna date urodzenia")
except BadPESEL:
    print("Podano niepoprawny nr PESEL")
except BadYear:
    print("Podano niepoprawny rok urodzenia")
except BadMonth:
    print("Podano niepoprawny miesiac urodzenia")
except BadDay:
    print("Podano niepoprawny dzien urodzenia")
except BadPControl:
    print("Niepoprawna cyfra kontrolna")

class BadDate(Exception):
    pass

def meanAge(t):
    "Zad 3 --- Funkcja liczace sredni wiek osob ktorych daty urodzenia sa w pliku"
    dates = []
    today = datetime.date.today()
    with open("daty.in") as daty:
        lines = daty.readlines()
        for line in lines:
            if len(line.split(" ")) != 3:
                    if t == 'r':
                        raise BadDate
                    if t == 'l':
                        pass
            else:
                day, month, year = line.split(" ")
                dates.append(today.year - int(year))
    return statistics.mean(dates)

try:
    print(meanAge(t='l'))
except BadDate:
    print("Niepoprawny wpis")
