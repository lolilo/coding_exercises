"""
Given a set of possible scores in a game and a total target score, 
print out all the possible ways to arrive at that target score.

([2, 6, 10], 10) -> [[2, 2, 2, 2, 2], [6, 2, 2], [10]]

Well, I'm getting [[10], [2, 2, 6], [2, 2, 2, 2, 2], [2, 6, 2], [6, 2, 2]]
Just need another check. We can sort the lists to redefine what is considered unique combinations.
"""

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
def add_to_total(scores, t): # takes in a list of ints and a target score
    out = []

    if t == 0:
        return [out]

    if t in scores:
        out.append([t])

    for score in scores:
        if score >= t:
            continue
        # find all possible lists that can add up to number needed to reach target
        rest = add_to_total(scores, t-score)

        # print 'rest is', rest

        for l in rest:
            out.append([score] + l)
        
    # print 'out is', out
    # print ''
    # be careful with data types. All returned values should be list of list(s).

    return out

l = [2, 6, 10]
t = 10
print add_to_total(l, t)

