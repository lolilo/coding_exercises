# m = target value
# n = number of coins

# time: O(m * n)
# space: O(m)


# list, int, hash map where key = target value, value = list of fewest coins to make that target value
def make_change(coinValueList, target_value, minCoins):
   # Solve the problem for each number of cents less than the target
   for cents in xrange(target_value + 1):

      # At worst, it takes all pennies, so make that the base solution
      coinCount = cents
      coin_list = [1] * cents

      # Try all coin values less than the current number of cents
      for coin_value in [c for c in coinValueList if c <= cents]:

            # See if a solution to current number of cents minus the value
            # of the current coin, with one more coin added is the best 
            # solution so far  

            current_num_coins_if_using_current_coin_value = len(minCoins[cents - coin_value]) + 1 
            if current_num_coins_if_using_current_coin_value < coinCount:
               coinCount = current_num_coins_if_using_current_coin_value
               coin_list = minCoins[cents - coin_value][::] + [coin_value]

      # By the end of the for-loop, we've found how to reach coinCount with the fewest amount of coins
      # Memoize the solution for the current number of cents
      minCoins[cents] = coin_list

   # By the time we're here, we've built the solution to the overall problem, 
   # so return it
   return minCoins[target_value]


import unittest

class Test(unittest.TestCase):
   def test_make_change(self):
      self.assertEqual(make_change([1, 10, 25], 30, {}), [10, 10, 10])

unittest.main()
