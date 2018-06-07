import random as rand

def linear_search(key, array):
    i = 0
    ind = None
    while True:
        if i < len(array):
            if key == array[i]:
                ind = i
                break
            else:
                i+=1
        else:
            break
    return ind

def get_numbers(count, stop):
    return rand.choices(range(stop), k=count)

numbers = get_numbers(10000, 10000)
print('Numbers:', numbers)
key = linear_search(9999, numbers)
if key:
    print('Key:', key)
    print('Number:', numbers[key])
else:
    print('Not found')