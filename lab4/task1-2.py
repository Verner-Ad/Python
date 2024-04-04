f=open('27-99b.txt')
n=int(f.readline())
a=[int(x) for x in f.readlines()]
s0,m,p=0,0,0
for i in range(1, n//2):
    s0=s0 + a[i]*i + a[i-1]*i
    m += a[i]
    p += a[-i]
s0 += a[n//2]*n//2
m+=a[n//2]
p+=a[0]
sm=[s0]
for i in range(1, n):
    sm.append(sm[i-1]-m+p)
    m=m-a[i]+a[(i+n//2)%n]
    p=p+a[i]-a[(i+n//2)%n]
print(sm.index(min(sm))+1)