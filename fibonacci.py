def get_fibonacci(num):
    fibonacci = []
    for i in range(abs(num) + 1):
        if i > 1:
            fibonacci.append(abs(fibonacci[i-1])+abs(fibonacci[i-2]))
        else:
            fibonacci.append(i)
        if num < 0 and i%2 == 0:
            fibonacci[i] = -fibonacci[i]       
    return fibonacci

# print('Enter your number')
# num = int(input())
print(get_fibonacci(-100000)[-1])
