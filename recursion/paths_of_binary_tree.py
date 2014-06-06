"""
Write a function that prints all paths of a binary tree. 
"""

def all_paths(n):

	if not n.right and not n.left:
		return [n.val]

	out = []
	paths = []

	if n.left: 
		paths.extend(all_paths(n.left))

	if n.right:
		paths.extend(all_paths(n.right))

	for p in paths:
		out.append([n.val] + p)

	return out

