#task 15 10
def sameel():
    mas2 = []
    mas1 = []
    c = 0
    num = int(input())
    for _ in range(num):
        mas1.append(input())
    num = int(input())
    for _ in range(num):
        mas2.append(input())
    for i in range(len(mas1) if len(mas1)>len(mas2) else len(mas2)):
        if len(mas1)>len(mas2):
            if mas1[i] in mas2: 
                c+=1
        else:
            if mas2[i] in mas1: 
                c+=1
    return c

#task 16 22
def mininline():
    lineMas = []
    mas = []
    num = int(input())
    for _ in range(num):
        mas.append(input())
    a = input()
    b = input()
    if a > b:
        b, a = a, b
    for i in mas:
        if i < b and i > a:
            lineMas.append(i)
    return lineMas.count(min(lineMas))

#task 17 34
def inrange():
    lineMas = []
    mas = []
    num = int(input())
    for _ in range(num):
        mas.append(input())
    a = input()
    b = input()
    if a > b:
        b, a = a, b
    for i in mas:
        if i < b and i > a:
            lineMas.append(i)
    return lineMas

#task 18 46
def 

#task 19 58

