strs = []
n = int(input())
for i in range(n):
    c = input()
    strs.append([c,len(c.split())])
for i in range(c):
    for j in range(c)-1:
        if c[j][1] > c[j+1][1]:
            c[j][1], c[j+1][1] = c[j+1][1], c[j][1]