file=open('27-99a.txt')
numb=int(file.readline())
masInput=[int(x) for x in file.readlines()]
mas=[0]*numb
for i in range(numb//2):
    mas[i]=i
    mas[numb-i-1]=i+1
if numb%2==1: mas[numb//2]=numb//2
mx=10**20
mi=0
def move(b):
    t=b[-1]
    for i in range(numb-1, 0, -1):
        b[i]=b[i-1]
    b[0]=t
for i in range(numb):
    s = 0
    for j in range(numb):
        s += masInput[j]*mas[j]
    if s<mx:
        mx=s
        mi=i
    move(mas)
print(mi+1)