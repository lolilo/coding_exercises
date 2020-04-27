import bisect
import random
import string

# Use a constant see to ensure that we see
# the same pseudo-random numbers each time
# we run the loop.
random.seed(1)

# Generate x random numbers and
# insert them into a list in sorted
# order.
x = 200000
letters = string.ascii_lowercase

def bisect_test(x, letters):
	l = []
	for i in range(1, x):
	    r = ''.join(random.choice(letters) for i in range(10))
	    # position = bisect.bisect(l, r)
	    bisect.insort_left(l, r)
	    # print('%2d %2d' % (r, position), l)


def sort_test(x, letters):
	l = []
	for i in range(1, x):
	    r = ''.join(random.choice(letters) for i in range(10))
	    l.append(r)
	sorted(l)

# sorting at the end always seems significantly faster

sort_test(x, letters)
# bisect_test(x, letters)

