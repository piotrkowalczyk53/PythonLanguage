"Lab 8 --- Module containing tasks for the laboratories"
import random
import datetime
import statistics


def translation(factors, probabilities, x = 1, y = 1):
    "Task 1 --- Function translating points"
    if len(factors) != len(probabilities):
        raise Exception("Number of factors don't match number of probabilities")
    if sum(probabilities) != 1:
        raise Exception("Probability does not sum up to 100%")
    if any(list(map(lambda l:len(l)!=6, factors))):
        raise Exception("Bad number of factors")

    cw = random.choices(factors, weights=probabilities)
    cw = cw[0]
    newX = cw[0]*x + cw[1]*y + cw[2]
    newY = cw[3]*x + cw[4]*y + cw[5]

    return newX, newY


def checkPESEL(PESEL, date, gender):
    "Task 2 --- Function checking if PESEL number is a correct one"
    if len(PESEL) != 11:
        raise Exception("Bad lenght of PESEL")
    if int(PESEL[:2]) != date.year%100:
        raise Exception("Bad year of birth")
    if date.year < 1800:
        raise Exception("No PESEL number for that decade")
    if date.year >= 1800 and date.year < 1900:
        if int(PESEL[2:4])+80 != date.month:
            raise Exception("Bad month of birth")
    if date.year >= 1900 and date.year < 2000:
        if int(PESEL[2:4]) != date.month:
            raise Exception("Bad month of birth")
    if date.year >= 2000 and date.year < 2100:
        if int(PESEL[2:4])+20 != date.month:
            raise Exception("Bad month of birth")
    if date.year >= 2100 and date.year < 2200:
        if int(PESEL[2:4])+40 != date.month:
            raise Exception("Bad month of birth")
    if date.year >= 2200 and date.year < 2300:
        if int(PESEL[2:4])+60 != date.month:
            raise Exception("Bad month of birth")
    if int(PESEL[5:6]) != date.day:
        raise Exception("Bad day of birth")
    if int(PESEL[6:10]) % 2 == 0 and gender == "m":
        raise Exception("Bad gender")
    if int(PESEL[6:10]) % 2 == 1 and gender == "k":
        raise Exception("Bad gender")

    controls = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]
    control = 0
    for i in range(len(PESEL)-1):
        control = control + int(PESEL[i]) * controls[i]
    control = control % 10
    control = 10 - control
    control = control % 10

    if int(PESEL[-1]) != control:
        raise Exception("Bad control")
    print("Valid PESEL")


def meanAge(mode):
    "Task 3 --- Function counting average age from birthdates in a file"
    dates = []
    today = datetime.date.today()
    with open("daty.in") as daty:
        lines = daty.readlines()
        for line in lines:
            if len(line.split(" ")) != 3:
                    if mode == 0:
                        raise Exception("Bad entry")
                    if mode == 1:
                        pass
            else:
                day, month, year = line.split(" ")
                dates.append(today.year - int(year))
    return statistics.mean(dates)
