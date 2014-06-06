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


def regex(p, s): 
	pi = 0
	si = 0
	lp = len(p)
	ls = len(s)

	while pi < lp and si < ls:
		if pi + 1 < lp and p[pi + 1] == '*':
			if p[pi] == '.': 
				return True

			while p[pi] == s[si]:
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

	if si < ls: 
		return False

	# a* and '' are valid, in this case exit while loop for s
	# aaaaa and a are not valid, again, exited while loop for s
	while pi < lp: 
		if pi + 1 < lp and p[pi + 1] == '*': # this is valid
			pi += 2
		else: # not _* 
			return False

	return True


def main():
	unittest.main()

if __name__ == "__main__":
	main()

