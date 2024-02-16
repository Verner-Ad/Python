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

def func3(prime):
	divs = []
	nodivs = []
	for i in range (2, prime):
		if prime % i == 0:
			divs.append(i)
		else:
			nodivs.append(i)
	print(divs)
	print(nodivs)
	for i in range (0,len(nodivs)):
			if max(nodivs) % min(divs) == 0:
					nodivs.remove(max(nodivs))
	numSum = 0
	num = prime
	while num != 0:
		if num % 10 < 5:
			numSum += num % 10
		num //= 10
	if nodivs:
		return max(nodivs) * numSum
	else:
		return "no"

n = int(input())
if n == 1:
	print(func1(int(input())))
if n == 2:
	print(func2(int(input())))
if n == 3:
	print(func3(int(input())))