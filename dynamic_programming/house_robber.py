'''
You are a professional robber planning to rob houses along a street. 
Each house has a certain amount of money stashed, 
the only constraint stopping you from robbing each of them is that 
adjacent houses have security system connected and 
it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, 
determine the maximum amount of money you can rob tonight without alerting the police.
'''


def rob(house_money_list):
    size = len(house_money_list)
    max_money_at_position = [0] * (size + 1)
    if size:
        max_money_at_position[1] = house_money_list[0]
    for i in xrange(2, size + 1):
        max_money_at_position[i] = max(max_money_at_position[i - 1], max_money_at_position[i - 2] + house_money_list[i - 1])
    return max_money_at_position[size]


import unittest


class Test(unittest.TestCase):
    def test_rob(self):
        self.assertEqual(rob([4, 10, 3, 1, 5]), 15)
        self.assertEqual(rob([3, 6, 4]), 7)
        self.assertEqual(rob([0]), 0)
        self.assertEqual(rob([5, 10]), 10)
        self.assertEqual(rob([5, 1, 1, 5]), 10)

unittest.main()
