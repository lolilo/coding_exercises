def max_subarray_of_positive_values(l):
	prev_max_subarray = []
	curr_max_subarray = []
	prev_max_sum = 0
	curr_max_sum = 0

	for x in l:
		if x + curr_max_sum >= curr_max_sum:
			curr_max_sum += x
			curr_max_subarray.append(x)
		else:
			if curr_max_sum > prev_max_sum or prev_max_sum == 0:
				prev_max_subarray = curr_max_subarray[:]
				prev_max_sum = curr_max_sum
			curr_max_sum = 0
			curr_max_subarray = []

	if sum(curr_max_subarray) > prev_max_sum:
		prev_max_subarray = curr_max_subarray
	return prev_max_subarray

print max_subarray_of_positive_values([1, 2, 3, -20, 5]) == [1, 2, 3]
print max_subarray_of_positive_values([5, 5, -1, 4]) == [5, 5]
print max_subarray_of_positive_values([5, 5, -1, -1, -20, 4]) == [5, 5]
print max_subarray_of_positive_values([100, -1, 100]) == [100]
print max_subarray_of_positive_values([1, 2, 5, -7, 2, 3]) == [1, 2, 5]
print max_subarray_of_positive_values([0, 0, -1, 0]) == [0, 0]
print max_subarray_of_positive_values([756898537, -1973594324, -2038664370, -184803526, 1424268980]) == [1424268980]

def max_subarray_of_positive_values2(l):
	max_sum = -1
	max_subarray = []
	i = 0
	len_l = len(l)

	while i < len_l:
		while i < len_l and l[i] < 0:
			i += 1

		curr_sum = 0
		curr_subarray = []
		while i < len_l and l[i] >= 0:
			curr_sum += l[i]
			curr_subarray.append(l[i])
			i += 1

		if curr_sum > max_sum:
			max_sum = curr_sum
			max_subarray = curr_subarray

	return max_subarray

print max_subarray_of_positive_values2([1, 2, 3, -20, 5]) == [1, 2, 3]
print max_subarray_of_positive_values2([5, 5, -1, 4]) == [5, 5]
print max_subarray_of_positive_values2([5, 5, -1, -1, -20, 4]) == [5, 5]
print max_subarray_of_positive_values2([100, -1, 100]) == [100]
print max_subarray_of_positive_values2([1, 2, 5, -7, 2, 3]) == [1, 2, 5]
print max_subarray_of_positive_values2([0, 0, -1, 0]) == [0, 0]
print max_subarray_of_positive_values2([756898537, -1973594324, -2038664370, -184803526, 1424268980]) == [1424268980]
