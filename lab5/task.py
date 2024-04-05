import re

class WrongLink(Exception):
    def __init__(self, text):
        self.txt = text

def linkCheker(stroke):

    if re.fullmatch(r'(?:http|https)://[\w]+\.(?:com|ru|uk)(?:/)', stroke):
        return True    
    else:
        raise WrongLink("Данная строка не является ссылкой")

print(linkCheker(input()))

# print("Да" if re.fullmatch(r'(?:http|https)://[\w]+\.(?:com|ru|uk)(?:/)', input()) else "Нет")