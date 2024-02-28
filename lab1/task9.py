strs = []
n = int(input())
for i in range(n):
    strs.append(input())

strs.sort(key = len)
for i in strs:
    print(i)
strs.sort(key = len, reverse = True)
for i in strs:
    print(i)