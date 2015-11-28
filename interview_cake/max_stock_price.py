'''
Suppose we could access yesterday's stock prices as a list, where:

The indices are the time in minutes past trade opening time, which was 9:30am local time.
The values are the price in dollars of Apple stock at that time.
So if the stock cost $500 at 10:30am, stock_prices_yesterday[60] = 500.

Write an efficient function that takes stock_prices_yesterday and returns the best profit I could have made from 1 purchase and 1 sale of 1 Apple stock yesterday.
'''

# similar to max continuous subsequence?
def get_max_profit(stock_prices_yesterday): 
    length_times = len(stock_prices_yesterday) - 1 
    current_max = 0
    final_max = 0
    for i in xrange(length_times):
        current_max = max(stock_prices_yesterday[i:]) - stock_prices_yesterday[i]
        final_max = max(current_max, final_max)
    return final_max

stock_prices_yesterday = [10, 7, 5, 8, 11, 9]
print get_max_profit(stock_prices_yesterday)
# returns 6 (buying for $5 and selling for $11)
