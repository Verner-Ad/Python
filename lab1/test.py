from math import sqrt

def f(x1, x2):
    return 3 * x1 ** 2 + 4 * x2 ** 2 - 2 * x1 * x2 + x1

def golden_ratio(f, a, b, l):
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

def grad(f, x1, x2):
    h = 1e-10
    return [(f(x1 + h, x2) - f(x1, x2)) / h, (f(x1, x2 + h) - f(x1, x2)) / h]

def euclid_norm(x1, x2):
    return sqrt(x1 ** 2 + x2 ** 2)

M = 50
eps1, eps2 = 0.1, 0.15
x0 = [2, 1,5]
x = []
x.append(x0)
k = 0
step_four_cond = False
while k < M:
    def varphi(t):
        return f(x[-1][0] - t * grad(f, x[-1][0], x[-1][1])[0], x[-1][1] - t * grad(f, x[-1][1], x[-1][1])[1])
    a, b = -10, 10
    t_min = a
    while t_min == a or t_min == b:
        t_min = golden_ratio(varphi, a, b, eps1)
        if abs(t_min - a) <= eps1:
            a -= 10
            b -= 10
            t_min = b
        if abs(t_min - b) <= eps1:
            a += 10
            b += 10
            t_min = a
    x.append([x[-1][0] - t_min * grad(f, x[-1][0], x[-1][1])[0], x[-1][1] - t_min * grad(f, x[-1][1], x[-1][1])[1]])
    grad_f = grad(f, x[-1][0], x[-1][1])
    if euclid_norm(grad_f[0], grad_f[1]) < eps1:
        break
    if k > 1 and euclid_norm(x[-1][0] - x[-2][0], x[-1][1] - x[-2][1]) < eps2:
        if step_four_cond:
            break
        else:
            step_four_cond = True
    else:
        step_four_cond = False
    k += 1
print("x* ~=", x[-1])
print("f(x*) =", f(x[-1][0], x[-1][1]))	
