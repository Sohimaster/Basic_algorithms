import random as rand

def insertion_sort(array):
	for i in range(len(array)):
		while i > 0 and array[i-1] > array[i]:
			array[i], array[i-1] = array[i-1], array[i]
			i-=1
	return array

def get_numbers(count, stop):
	return rand.choices(range(stop), k=count)

nums = get_numbers(10000, 1000)
print('Not sorted:', nums)
sorted_nums = insertion_sort(nums)
print('Sorted numbers:', sorted_nums)