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

def func2(num):
  nums = []
  while num != 0:
    nums.insert(-0,num % 10)
    num //= 10
  while True:
    if max(nums) % 3 == 0:
      nums.remove(max(nums))
    else:
      return max(nums)

print(func1(int(input())))
print(func2(int(input())))
