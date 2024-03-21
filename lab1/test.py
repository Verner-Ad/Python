from math import sqrt
delta, eps = 0.2, 0.5
a, b = 0, 10
def fibba(N):
    if N == 0:
        return 0
    elif N == 1:
        return 1
    return fibba(N - 1) + fibba(N - 2)
def f(x):
    return 2 * x ** 2 - 12 * x + 19
N = 0
L = b - a
fibs = [fibba(N)]
while fibba(N) < L / eps:
    N += 1
    fibs.append(fibba(N))
x = a + fibs[N - 2] / fibs[N] * (b - a)
y = a + fibs[N - 1] / fibs[N] * (b - a)
i = 0
for k in range(N - 2):
    i+=1
    if f(x) <= f(y):
        b = y
        y = x
        x = a + fibs[N - k - 3] / fibs[N - k - 1] * (b - a)
    else:
        a = x
        x = y
        y = a + fibs[N - k - 2] / fibs[N - k - 1] * (b - a)
    if abs(b - a) < 2 * eps:
        ab = (a + b) / 2
        print("x* ~= ", ab)
        print("f(x*) ~= ", f(ab))
        print(abs(f(ab)-f(3)))
        print(i)
        exit(0)
    x = (a + b) / 2
    y = x + delta
    if f(x) <= f(y):
        b = y
    else:
        a = x
ab = (a + b) / 2
print("x* ~= ", ab)
print("f(x*) ~= ", f(ab))
print(abs(f(ab)-f(3)))
print(i)
