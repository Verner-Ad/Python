def quaddev(x, y):
        numerator = 0
        amount = 0
        for i in range(len(x)//2): #середина при нечетных не учитывается, ибо там разница символов ноль
            numerator += (ord(x[i]) - ord(x[len(x)-1-i]) - y)**2
            amount += 1
        print([x,(numerator / amount)**0.5])
        return (numerator / amount)**0.5

def maxord(strs):
    c = 0
    for j in strs:
            if ord(j) > c:
                c = ord(j)
    return c

def quaddifASCII():
    strs = []
    for _ in range(int(input())):
        strs.append(input())
    print(strs)
    strs.sort(key = lambda x:quaddev(x,maxord(x)))
    print(strs)
    
quaddifASCII()