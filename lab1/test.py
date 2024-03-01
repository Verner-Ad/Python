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

def mostusual(str):
    maxChar = {}
    for i in str:
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

def quaddifusualchar():
    strs = []
    for _ in range(int(input())):
        strs.append(input())
    masStr = []
    for i in strs:
        masStr.append([i,mostusual(i)[1]/len(i) - freq[mostusual(i)[0]]])
    for i in range(0,len(masStr)):
        for j in range(0,len(masStr)-1):
            if masStr[j][1] > masStr[j+1][1]:
                masStr[j][1], masStr[j+1][1] = masStr[j+1][1], masStr[j][1]
    print(masStr)

quaddifusualchar()

