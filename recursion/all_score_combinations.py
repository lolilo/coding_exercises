# find all the ways you can create target score t by adding possible scores in list l

def memoize(fn):
    cache = {}
    def decorated_fn(*args):
        # need to convert key into immutable. cannot have nested list inside tuple
        key_1 = tuple(args[0])
        key = (key_1, args[1])

        if cache.get(key): # unhashable type, list? Whaaaat. It's a tuple! 
            return cache[key]
        else:
            cache[key] = fn(*args)
            return cache[key]
    return decorated_fn

@memoize
def all_score_combinations(scores, t):
	out = []
	if t == 0: # this only happens if initial t == 0
		return []

	if t < min(scores):
		return None

	if t in scores:
		out.append([t])

	for score in scores: 
		if score >= t: # already accounted for score == t earlier
			continue

		new_t = t - score
		rest = all_score_combinations(scores, new_t)
		if rest == None: 
			continue
		for l in rest:
			out.append([score] + l)

	if out == []:
		return None # can wrap all_score_combinations around another function if we want to return a string instead of None
	return out # could also use wrapper to print out scores rather than return a list

l1 = [2, 5, 10]
l2 = [1, 2, 5, 10]
l3 = [3]

t1 = 10
t2 = 0
# print all_score_combinations(l1, t2)
print all_score_combinations(l3, t1)

l = [2, 6, 10]
t = 10
print all_score_combinations(l, t)
