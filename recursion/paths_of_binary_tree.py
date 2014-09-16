"""
Write a function that prints all paths of a binary tree. 
"""

def all_paths(n):
	all_paths_helper(n, '')

	def all_paths_helper(n, path):
		
		if not n.right and not n.left: # leaf node
			print path + n.value

		if n.right:
			all_paths(n.right, path + 'n.value')

		# another path starting now
		if n.left:
			all_paths(n.left, path + 'n.value')


# this is non-optimal? If we just need to print out paths, no need to store all of them in space.
def all_paths_bad(n):

	if not n.right and not n.left:
		return [n.val]

	out = [] # eventual list of lists
	paths = [] # also a list of lists, but will be missing n.val at their beginning

	if n.left: 
		paths.append(all_paths(n.left))

	if n.right:
		paths.append(all_paths(n.right))

	for p in paths:
		out.append([n.val] + p)

	return out

