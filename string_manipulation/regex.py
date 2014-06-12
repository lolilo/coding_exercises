"""
regex function, subset
char a - z
. 
*
"""

import unittest

class Test(unittest.TestCase):
	def test_regex(self):
		self.assertEqual(regex('a*', ''), True)
		self.assertEqual(regex('z*b*', ''), True)
		self.assertEqual(regex('aa*', 'a'), True)
		self.assertEqual(regex('.', 'a'), True)
		self.assertEqual(regex('.*', 'anblskfj'), True)
		self.assertEqual(regex('a*', 'anblskfj'), False)
		self.assertEqual(regex('aaa', 'a'), False)
		self.assertEqual(regex('a*aa', 'aa'), True)


def regex(p, s): 
	pi = 0
	si = 0
	len_p = len(p) # do this so that we don't need to calculate length each time
	len_s = len(s)

	while pi < len_p and si < len_s:
		if pi + 1 < len_p and p[pi + 1] == '*':
			if p[pi] == '.': 
				return True

			while si < len_s and p[pi] == s[si]:
				si += 1
			pi += 2

		elif p[pi] == '.':
			pi += 1
			si += 1

		elif ord('a') <= ord(p[pi]) <= ord('z'):
			if p[pi] == s[si]: 
				pi += 1
				si += 1
			else:
				return False

	# at this point, check if we are in a valid state
	# if we haven't consumed all of the input s, we know it's invalid

	if si < len_s: 
		return False

	# a* and '' are valid, in this case exit while loop for s
	# aaaaa and a are not valid, again, exited while loop for s
	while pi < len_p: 
		if pi + 1 < len_p and p[pi + 1] == '*': # this is valid
			pi += 2
		else: # not _* 
			return False

	return True


def main():
	unittest.main()

if __name__ == "__main__":
	main()

