import re

print(len((re.findall(r'\b'.join(input()),(open("text.txt",'r',encoding = "utf-8")).read()))))