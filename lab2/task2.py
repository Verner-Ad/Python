inp = []
for i in range(int(input())):
    inp.append(input().split())
cust = []
for i in inp:
    if i[0] not in cust:
        cust.append(i[0])
custDict = {}
for i in cust:
    tempDict = {}
    for j in inp:
        if i == j[0]:
            if j[1] in list(tempDict.keys()):
                tempDict[j[1]] += int(j[2])
            else:
                tempDict[j[1]] = int(j[2])
    custDict[i] = tempDict
CL = list(custDict.keys())
for i in CL:
    print(i + ":\n" + str(custDict[i]))
"""
6
Ivanov paper 10
Petrov pens 5
Ivanov marker 3
Ivanov paper 7
Petrov envelope 20
Ivanov envelope 5
"""