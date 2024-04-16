from math import sqrt

def f(x1, x2):
    return 3 * x1 ** 2 + 4 * x2 ** 2 - 2 * x1 * x2 + x1

def GoldRat(f, a, b, l):
    while abs(b - a) > 2 * l:
        x = a + (3 - sqrt(5)) / 2 * (b - a)
        y = a + b - x
        if f(x) <= f(y):
            b = y
            y = x
            x = a + b - x
        else:
            a = x
            x = y
            y = a + b - y
    return (a + b) / 2

def Grad(f, x1, x2):
    h = 1e-10
    return [(f(x1 + h, x2) - f(x1, x2)) / h, (f(x1, x2 + h) - f(x1, x2)) / h]

def Phi(t):
    return f(x[-1][0] - t * Grad(f, x[-1][0], x[-1][1])[0], x[-1][1] - t * Grad(f, x[-1][1], x[-1][1])[1])
    
def ENorm(x1, x2):
    return sqrt(x1 ** 2 + x2 ** 2)

x0 = [2, 1,5]
x = []
x.append(x0)
M = 50
k = 0
e1, e2 = 0.1, 0.15
stepFourCond = False
while k < M:
    a, b = -10, 10
    tMin = a
    while tMin == a or tMin == b:
        tMin = GoldRat(Phi, a, b, e1)
        if abs(tMin - a) <= e1:
            a -= 10
            b -= 10
            tMin = b
        if abs(tMin - b) <= e1:
            a += 10
            b += 10
            tMin = a
    x.append([x[-1][0] - tMin * Grad(f, x[-1][0], x[-1][1])[0], x[-1][1] - tMin * Grad(f, x[-1][1], x[-1][1])[1]])
    gradF = Grad(f, x[-1][0], x[-1][1])
    if ENorm(gradF[0], gradF[1]) < e1:
        break
    if k > 1 and ENorm(x[-1][0] - x[-2][0], x[-1][1] - x[-2][1]) < e2:
        if stepFourCond:
            break
        else:
            stepFourCond = True
    else:
        stepFourCond = False
    k += 1
print("xk min =", x[-1])
print("f(xk) min =", f(x[-1][0], x[-1][1]))
print("delta x = ", abs(-2/11 - x[-1][0]),', ',abs(-1/22 - x[-1][1]))
print("delta f(x) = ", f(-2/11,-1/22) - f(x[-1][0],x[-1][1]))