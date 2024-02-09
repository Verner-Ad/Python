def func1(prime):
  divs = []
  nodivs = []
  for i in range (2, prime):
    b = True
    if prime % i == 0:
      divs.insert(-1,i)
    for j in divs:
      if i % j == 0:
        b = False
        break
    if prime % i != 0 and b and i % 2 == 0:
        nodivs.insert(-1,i)
  print(divs)
  print(nodivs)
  return len(nodivs)

print(func1(int(input())))