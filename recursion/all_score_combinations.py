# find all the ways you can create target score t by adding possible scores in list l

def all_scores(l, t):
	out = []
	if t == 0: # this only happens if initial t == 0
		return []

	if t < min(l):
		return None

	if t in l:
		out.append([t])

	for n in l: 
		if n >= t: # already accounted for n == t earlier
			continue

		new_t = t - n
		rest = all_scores(l, new_t)
		if rest == None: 
			continue
		for score in rest:
			out.append([n] + score)

	if out == []:
		return None # can wrap all_scores around another function if we want to return a string instead of None
	return out # could also use wrapper to print out scores rather than return a list

l1 = [2, 5, 10]
l2 = [1, 2, 5, 10]
l3 = [3]

t1 = 10
t2 = 0
# print all_scores(l1, t2)
print all_scores(l3, t1)

l = [2, 6, 10]
t = 10
print all_scores(l, t)
