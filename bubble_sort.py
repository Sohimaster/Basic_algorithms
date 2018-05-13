import random as rand

def bubble_sort(array):
	iterations = 0
	while True:
		bubbles = 0
		for i in range(len(array)-iterations):
			if i != len(array)-1:
				if array[i] > array[i+1]:
					array[i], array[i+1] = array[i+1], array[i]
					bubbles+=1
		if not bubbles:
			break
		iterations+=1
	return array

def get_numbers(count, stop):
	return rand.choices(range(stop), k=count)

numbers = get_numbers(20, 30)
print('Not sorted:', numbers)
sorted_numbers = bubble_sort(numbers)
print('Sorted numbers:', sorted_numbers)