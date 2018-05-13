import random as rand

def insertion_sort(array):
	for i in range(len(array)):
		j = i
		while j > 0 and array[j-1] > array[j]:
			array[j], array[j-1] = array[j-1], array[j]
			j-=1
	return array

def get_numbers(count, stop):
	return rand.choices(range(stop), k=count)

nums = get_numbers(20, 10)
print('Not sorted:', nums)
sorted_nums = insertion_sort(nums)
print('Sorted numbers:', sorted_nums)