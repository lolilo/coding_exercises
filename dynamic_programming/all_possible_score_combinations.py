"""
Given a set of possible scores in a game and a total target score, 
print out all the possible ways to arrive at that target score.

([2, 6, 10], 10) -> [[2, 2, 2, 2, 2], [6, 2, 2], [10]]
"""

def memoize(fn):
    cache = {}
    def decorated_fn(*args):
        # only need t as a key; assume scores array will be the same. 
        # breaks if method takes in varying scores.
        key = tuple((tuple(args[0]), args[1]))

        if not cache.get(key):
            cache[key] = fn(*args)
        print cache 
        return cache[key]         

    return decorated_fn

@memoize
def add_to_total(scores, t): # takes in a list of ints and a target score
    if t == 0:
        return 1
    if t < min(scores):
        return 0
    # if t == min(scores):
    #     return 1

    total_possible_ways = 0
    for score in [score for score in scores if score <= t]:
        if t == 3:
            print 'score', score 
            print 'total_possible_ways', total_possible_ways
            print '' 
        total_possible_ways += add_to_total(scores, t - score)
        # if possible_ways > 0:   
            # total_possible_ways += possible_ways
    return total_possible_ways

    # for score in [score for score in scores if score <= t]:
    #     possible_ways = add_to_total(scores, t - score)
    #     if possible_ways > 0:
    #         total_possible_ways += possible_ways
    # return total_possible_ways

print add_to_total([2], 3) == 0 # [1, 1], [2]
# print add_to_total([1, 2, 5], 2) == 2 # [1, 1], [2]
print add_to_total([1, 2, 5], 3) == 2 # [1, 1, 1], [1, 2]
# print add_to_total([1, 2, 5], 5) == 4
# print add_to_total([2, 6, 10], 10) == 3
