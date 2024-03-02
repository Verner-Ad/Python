import re

freq = {
"a": 0.0817,
"b": 0.0149,
"c": 0.0278,
"d": 0.0425,
"e": 0.1270,
"f": 0.0223,
"g": 0.0202,
"h": 0.0609,
"i": 0.0697,
"j": 0.0015,
"k": 0.0077,
"l": 0.0403,
"m": 0.0241,
"n": 0.0675,
"o": 0.0751,
"p": 0.0193,
"q": 0.0010,
"r": 0.0599,
"s": 0.0633,
"t": 0.0906,
"u": 0.0276,
"v": 0.0098,
"w": 0.0236,
"x": 0.0015,
"y": 0.0197,
"z": 0.0007
}
#task11
def diff(x):
    return abs(len( r'[qwrtpsdfghjklzxcvbnm]', x, re.IGNORECASE) - len(r'[eyuioa]', x, re.IGNORECASE))

def chardifrange():
    strs = []
    i = int(input())
    for i in range(i):
        strs[i].insert(input())
    print(strs.sort(key = lambda string: diff(string)))
#task12
def mostusual(str_):
    maxChar = {}
    for i in str_:
        if i in maxChar:
            maxChar[i] += 1
        else:
            maxChar[i] = 1
    d = list(maxChar)
    c = [d[0],maxChar.get(d[0])]
    for i in d:
        if maxChar[i] > c[1]:
            c = [i,maxChar[i]]
    return c

def difusualchar():
    strs = []
    i = int(input())
    for _ in range(i):
        strs.append(input())
    masStr = []
    for i in strs:
        masStr.append([i,mostusual(i)[1]/len(i) - freq[mostusual(i)[0]]])
    for i in range(0,len(masStr)):
        for j in range(0,len(masStr)-1):
            if masStr[j][1] > masStr[j+1][1]:
                masStr[j][1], masStr[j+1][1] = masStr[j+1][1], masStr[j][1]
    print(masStr)

"""
5
qqqwwq
wwweew
rrrtte
aaaassa
aaaas
"""
#task13
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
    i = int(input())
    for _ in range(i):
        strs.append(input())
    print(strs)
    strs.sort(key = lambda x:quaddev(x,maxord(x)))
    print(strs)
#task14
def amounttriple(x):
    amount = 0
    for i in range (0,len(x)-2):
        if x[i] == x[i+2] and x[i] != x[i+1]:
            amount += 1
    return amount

def trilemirror():
    strs = []
    c = 0
    i = int(input())
    for _ in range(i):
        strs.append(input())
    strs.sort(key = lambda st: amounttriple(st))
    
    for i in strs:
        print(i)

a = [chardifrange,difusualchar,quaddifASCII,trilemirror]
print(a[int(input())]())