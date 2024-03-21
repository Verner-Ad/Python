n, k= (int(i) for i in input().split())
numOfStrikes = 0
listOfStrikes = []
for _ in range(k):
    strikeEl = input().split()
    strikeEl[0] = int(strikeEl[0])
    strikeEl[1] = int(strikeEl[1])
    listOfStrikes.append(strikeEl)
for i in range(n):
    if (i+1) % 7 != 0 and ((i+1) % 7) - 6 != 0:
        strikeOn = False
        for j in range(k):
            if (i+1) % listOfStrikes[j][1] == listOfStrikes[j][0] or (i+1) == listOfStrikes[j][0] :
                strikeOn = True
        if strikeOn:
            numOfStrikes+=1
print(numOfStrikes)