def get_factorial(num):
	fact = 1
	while num != 1:
		fact = num * fact
		num-=1
	return fact

print('Write number')
num = int(input())
print('Factorial of', num, 'is', get_factorial(num))