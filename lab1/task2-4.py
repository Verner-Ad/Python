#task 2
def pal(str):
    return str.lower() == ''.join(reversed(str))

#task 3
def numOfSplit(str):
    return len(str.split())

#task4
def order(str):
    return sorted(str.split(), key=len)

a = [pal,numOfSplit,order]
print(a[int(input())](input()))
