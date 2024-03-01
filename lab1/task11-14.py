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

def diff(x):
    return abs(len( r'[qwrtpsdfghjklzxcvbnm]', x, re.IGNORECASE) - len(r'[eyuioa]', x, re.IGNORECASE))

def quad_dev(x, y):
    numerator = 0
    amount = 0
    for i in range(len(x)):
        numerator += (ord(x[i]) - y)**2
        amount += 1
    return (numerator / amount)**0.5

def chardifrange(str):
    str.sort(key = diff()) 
    for i in str:
        print(i)

def 