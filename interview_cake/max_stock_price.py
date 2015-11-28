'''
Suppose we could access yesterday's stock prices as a list, where:

The indices are the time in minutes past trade opening time, which was 9:30am local time.
The values are the price in dollars of Apple stock at that time.
So if the stock cost $500 at 10:30am, stock_prices_yesterday[60] = 500.

Write an efficient function that takes stock_prices_yesterday and returns the best profit I could have made from 1 purchase and 1 sale of 1 Apple stock yesterday.
'''

# similar to max continuous subsequence?
def get_max_profit(stock_prices_yesterday): 
    length_times = len(stock_prices_yesterday)
    if length_times < 1:
        raise ValueError('List can not be empty.')
    current_min_price = stock_prices_yesterday[0]
    potential_max_profit = 0
    final_max_profit = 0
    for i in xrange(length_times):
        potential_max_profit = stock_prices_yesterday[i] - current_min_price
        current_min_price = min(current_min_price, stock_prices_yesterday[i])
        final_max_profit = max(potential_max_profit, final_max_profit)
    return final_max_profit

# stock_prices_yesterday = [10, 7, 5, 8, 11, 9]
# print get_max_profit(stock_prices_yesterday)
# returns 6 (buying for $5 and selling for $11)

import unittest


class Test(unittest.TestCase):

    def test_get_max_profit(self):
        self.assertEqual(get_max_profit([10, 7, 5, 8, 11, 9]), 6)
        self.assertEqual(get_max_profit([10, 7, 5, 4, 4, 4, 2]), 0)
        self.assertRaises(ValueError, get_max_profit, [])

unittest.main()
