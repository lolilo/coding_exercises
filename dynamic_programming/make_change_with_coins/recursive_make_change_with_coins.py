def memoize(f):
    cache = {}
    def decorated_function(*args):
        coin_list = args[0]
        target_value = args[1]
        args = (tuple(coin_list), target_value)
        if args not in cache.keys():
            cache[args] = f(*args)
        return cache[args]

    return decorated_function

# cannot memoize like this if you plan on changing the coin list. DUH.
# def memoize(f):
#     cache = {}
#     def decorated_function(*args):
#         # coin_list = args[0]
#         target_value = args[1]
#         # args = (tuple(coin_list), target_value)
#         if target_value not in cache.keys():
#             cache[target_value] = f(*args)
#         print ''
#         print cache
#         return cache[target_value]

#     return decorated_function


@memoize
def recursive_coin_change(coins, target): 
    if target == 0: 
        return []

    final_list = []

    for coin in coins:
        if coin > target:
            continue
        new_target = target - coin
        rest = recursive_coin_change(coins, new_target)

        if rest == 0: 
            continue

        coin_list = [coin]
        coin_list.extend(rest) # be mindful -- this returns nothing! alters list in place. earlier I was doing coin_list = [coin].extend(rest)
        if not final_list or len(final_list) > len(coin_list):
            final_list = coin_list

    if final_list == []:
        return 0
    return final_list


import unittest


class Test(unittest.TestCase):
   def test_make_change(self):
      self.assertEqual(recursive_coin_change([1, 10, 25], 30), [10, 10, 10])
      self.assertEqual(recursive_coin_change([], 30), 0)
      self.assertEqual(recursive_coin_change([25], 30), 0)
      self.assertEqual(recursive_coin_change([1, 5, 10, 25], 30), [5, 25])
      self.assertEqual(recursive_coin_change([1, 5, 10, 25], 29), [1, 1, 1, 1, 25])

unittest.main()
