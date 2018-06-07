import random as rand

def bubble_sort(array):
	iterations = 0
	while True:
		for i in range(len(array)-iterations):
			if i != len(array)-1:
				if array[i] > array[i+1]:
					array[i], array[i+1] = array[i+1], array[i]
		if iterations == len(array):
			break
		iterations+=1
	return array

def get_numbers(count, stop):
	return rand.choices(range(stop), k=count)

numbers = get_numbers(10000, 1000)
print('Not sorted:', numbers)
sorted_numbers = bubble_sort(numbers)
print('Sorted numbers:', sorted_numbers)