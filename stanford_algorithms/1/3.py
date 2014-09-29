
# takes in two unordered sets and returns the intersection of the two sets
# set A with n elements
# set B with m elements

import unittest

class Test(unittest.TestCase):
	def setUp(self):
		self.setA = set(['cat', 'dog', 'mouse', 'rat'])
		self.setB = set(['cat', 'dog', 'rat'])

	def test_union_of_two_sets(self):
		self.assertEqual(union_of_two_sets(self.setA, self.setB), set(['cat', 'dog', 'rat']))

# assumes sets a and b are given as arrays
def union_of_two_sets(a, b): 
	# return a.intersection(b)
	new = set()
	for item in a: 
		if item in b: 
			new.add(item)
	return new

if __name__ == "__main__":
	unittest.main()
