"""
Given two strings, return True if there is one and only one edit between the two strings. 
Return False otherwise. 

Examples
('cat', 'cot') -> True
('cat', 'cta') -> False

also true for addition or deletion of one letter
('cat', 'ct') -> True
('cat', 'coat') -> True
"""

import unittest

class Test(unittest.TestCase):
	def test_one_edit(self):
		self.assertEqual(one_edit('cat', 'cot'), True)
		self.assertEqual(one_edit('cat', 'cta'), False)
		self.assertEqual(one_edit('cat', 'ct'), True)
		self.assertEqual(one_edit('cat', 'coat'), True)
		self.assertEqual(one_edit('cat', 'caat'), True)
		self.assertEqual(one_edit('caaaaat', 'cat'), False)
		self.assertEqual(one_edit('', ''), False)
		self.assertEqual(one_edit('', 'a'), True)
		self.assertEqual(one_edit('a', 't'), True)

def one_edit(s1, s2):
	if abs(len(s1) - len(s2)) > 1:
		return False

	# one empty string, one single-character string
	if (len(s1) == 0 or len(s2) == 0) and (len(s1) == 1 or len(s2) == 1):
		return True

	if len(s1) > len(s2):
		long_string = s1
		short_string = s2
	else:
		long_string = s2
		short_string = s1
		# if strings are the same length, this doesn't matter

	long_i = 0
	short_i = 0
	one_edit = False
	diff_len = len(long_string) != len(short_string)

	while long_i < len(long_string) and short_i < len(short_string):
		if long_string[long_i] == short_string[short_i]:
			long_i += 1
			short_i += 1
		elif one_edit: # we have already seen one edit
			return False
		elif diff_len:
			one_edit = True
			long_i += 1
		else: 
			one_edit = True
			long_i += 1
			short_i += 1
	return one_edit

def main():
	unittest.main()

if __name__ == "__main__":
	main()
