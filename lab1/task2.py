def pal(str):
    return str.lower() == ''.join(reversed(str))

print(pal(input()))
