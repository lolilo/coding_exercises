"""Given an input string, print out the N most common characters in that string."""

# implement a hash map and a min heap of the current max nums. 
# hash map size len(s)
# min heap size O(n)

# s is a string
# n is an int
def most_common_chars(s, n):
	if len(s) < n:
		print "There are fewer than %d characters in %r." % (n, s)

	for char in s: 
		if char in d:
			d[char] += 1
			if d[char] > d[heap.top]:
				heap.pop()
				heap.insert(char) # the heap will perculate up according to d[char] value
				# otherwise, we could store tuples in the heap, (char, #)
		else: 
			d[char] = 1
			if heap.size < 10:
				heap.insert(char)

	# heap is represented as a list
	for i in heap.list:
		print i
