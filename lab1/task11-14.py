import re

def diff(x):
    return abs(len( r'[тйкнгшщцзхъфвпрлджчсмб]', x, re.IGNORECASE) - len(r'[ёуеыаоэяию]', x, re.IGNORECASE))

def chardifrange(str):
    str.sort(key = diff()) 
    for i in str:
        print(i)

def 