inp = []
for i in range(int(input())):
    inp.append(input().split())
cust = []
for i in inp:
    if i not in cust:
        cust.append(i)