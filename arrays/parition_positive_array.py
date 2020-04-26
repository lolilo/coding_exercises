# You're given an array made up of positive integers. 
# Split the given array into two smaller arrays where the sums of each smaller array are equal. 
# Print out the two smaller arrays.

# [1,2,1,1,3] -> [1,2,1] & [1,3]
# [1,1,1,1,1,5] -> [1,1,1,1,1] & [5]
# [5,2,3] -> [5] & [2,3]

# def partitionArray(array):
# 	if len(array) < 2:
# 		return []
# 	for i in xrange(len(array)):
# 		everything_up_to_i_inclusive = array[:i + 1]
# 		everything_after_i_exclusive = array[i + 1:]
# 		if sum(everything_up_to_i_inclusive) == sum(everything_after_i_exclusive): 
# 			return [everything_up_to_i_inclusive, everything_after_i_exclusive]
# 	return []

# print partitionArray([1]) == []
# print partitionArray([]) == []
# print partitionArray([5, 3]) == []
# print partitionArray([1, 2, 1, 1, 3]) == [[1, 2, 1], [1, 3]]
# print partitionArray([1, 1, 1, 1, 1, 5]) == [[1, 1, 1, 1, 1], [5]]
# print partitionArray([5, 2, 3]) == [[5], [2, 3]]


def partitionArray(array):
	if len(array) < 2:
		return []

	curr_left_sum = array[0]
	curr_right_sum = sum(array[1:])

	if curr_left_sum == curr_right_sum: 
		return [[array[0]], array[1:]]

	for i in xrange(1, len(array)):
		curr_left_sum += array[i]
		curr_right_sum -= array[i]
		if curr_left_sum == curr_right_sum: 
			everything_up_to_i_inclusive = array[:i + 1]
			everything_after_i_exclusive = array[i + 1:]
			return [everything_up_to_i_inclusive, everything_after_i_exclusive]
	return []

print partitionArray([1]) == []
print partitionArray([]) == []
print partitionArray([5, 3]) == []
print partitionArray([1, 2, 1, 1, 3]) == [[1, 2, 1], [1, 3]]
print partitionArray([1, 1, 1, 1, 1, 5]) == [[1, 1, 1, 1, 1], [5]]
print partitionArray([5, 2, 3]) == [[5], [2, 3]]