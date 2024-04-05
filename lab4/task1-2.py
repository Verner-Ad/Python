file=open('27-99b.txt')
numb=int(file.readline())
masInput=[int(x) for x in file.readlines()]
sum0,right,left=0,0,0
for i in range(1, numb//2):
    sum0=sum0 + masInput[i]*i + masInput[i-1]*i
    right += masInput[i]
    left += masInput[-i]
sum0 += masInput[numb//2]*numb//2
right+=masInput[numb//2]
left+=masInput[0]
sm=[sum0]
for i in range(1, numb):
    sm.append(sm[i-1]-right+left)
    right=right-masInput[i]+masInput[(i+numb//2)%numb]
    left=left+masInput[i]-masInput[(i+numb//2)%numb]
print(sm.index(min(sm))+1)