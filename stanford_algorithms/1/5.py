# Given a sorted array of n numbers, describe a (n)-algorithm that,
# given another number x, determines whether or not there exist 
# two elements in the input array whose sum is exactly x. 
# Do not use hashing.

import unittest

class Test(unittest.TestCase):
	def setUp(self):
		self.l1 = [-3, 1, 2, 3, 10, 55]
		self.l2 = [1, 5, 32, 40]
		self.l3 = range(-5, 6)

	def two_elements_sum_to_x(self):
		self.assertEqual(two_elements_sum_to_x(self.l1, 0), True)
		self.assertEqual(two_elements_sum_to_x(self.l1, 7), True)
		self.assertEqual(two_elements_sum_to_x(self.l1, -1), False)
		self.assertEqual(two_elements_sum_to_x(self.l1, 13), True)

		self.assertEqual(two_elements_sum_to_x(self.l2, 45), True)

		self.assertEqual(two_elements_sum_to_x(self.l3, 0), True)
		self.assertEqual(two_elements_sum_to_x(self.l3, 13), True)

# input is an integer list and an integer x
# returns a boolean 
# linear time O(n)
def two_elements_sum_to_x(l, x):
	element_index = 0
	target = x - l[element_index]
	potential_pair_index = -1

	# also need to keep track of indexes bound by list length 
	while potential_pair_index > element_index:

		if target < l[potential_pair_index]:
			potential_pair_index -= 1
		elif target > l[potential_pair_index]:
			element_index += 1
			target = x - l[element_index]
		else: # l[potential_pair_index] = target
			return True

	return False



if __name__ == "__main__":
	unittest.main()
