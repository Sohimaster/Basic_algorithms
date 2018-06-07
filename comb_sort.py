import random as rand

def comb_sort(array):
    j = (len(array) * 10 // 13)
    while True:
        swapped = 0
        for i in range(len(array) - j):
            if array[i + j] < array[i]:
                array[i], array[i + j] = array[i + j], array[i] 
                swapped = 1
        if not swapped and j < 2:
            break
        j = (j * 10 // 13)
    return array

def get_numbers(count, stop):
    return rand.choices(range(stop), k=count)

numbers = get_numbers(10000, 10)
print('Not sorted:', numbers)
sorted_numbers = comb_sort(numbers)
print('Sorted numbers:', sorted_numbers)