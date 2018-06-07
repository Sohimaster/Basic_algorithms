import random as rand

def selection_sort(array):
	last_sorted = 0
	while last_sorted < len(array):
		min_index = array[last_sorted:].index(min(array[last_sorted:]))+last_sorted
		array[min_index], array[last_sorted] = array[last_sorted], array[min_index]
		last_sorted+=1
	return array

def get_numbers(count, stop):
    return rand.choices(range(stop), k=count)

nums = get_numbers(10000, 1000)
print('Not sorted:', nums)
sorted_nums = selection_sort(nums)
print('Sorted numbers:', sorted_nums)