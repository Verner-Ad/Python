f=open('27-99a.txt')
n=int(f.readline())
a=[int(x) for x in f.readlines()]
b=[0]*n
for i in range(n//2):
    b[i]=i
    b[n-i-1]=i+1
if n%2==1: b[n//2]=n//2
m=10**20
mi=0
def move(b):
    t=b[-1]
    for i in range(n-1, 0, -1):
        b[i]=b[i-1]
    b[0]=t
for i in range(n):
    s = 0
    for j in range(n):
        s += a[j]*b[j]
    if s<m:
        m=s
        mi=i
    move(b)
print(mi+1)