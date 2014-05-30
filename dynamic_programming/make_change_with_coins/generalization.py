#!/usr/bin/env python

# modified from: http://bryceboe.com/2009/11/04/dynamic-programming-%E2%80%93-coin-change-problem-in-python/

def solve_coin_change(coins, value):
    """A dynamic solution to the coin change problem"""
    # can also do with dictionary/actual hash table rather than list

    # table = [None for x in range(value + 1)] # initialize cache list
    table = [None] * (value + 1)
    table[0] = [] # set first element of list to an empty list; takes 0 coins to make zero

    for i in range(1, value + 1):
        
        for coin in coins:
            if coin > i: # coin > target value i; skip it 
                continue # cannot completely break out of loop, since input coins list is unsorted

            # if coin value not in table or if we can make a shorter list for table[i]
            elif not table[i] or len(table[i - coin]) + 1 < len(table[i]): 
                # we could combine the following 'if' with above, but this is more readable
                
                if table[i - coin] != None:
                    table[i] = table[i - coin][:] # create copy of list rather than point to same one
                    table[i].append(coin) # append new coin to list
                    # even if we're doing table[3], we're appending 3 to an empty list, since table[i-coin] = table[0] = []

    # print table

    if table[-1] != None: # last entry in table will be the for value, same as table[value]
        print '%d coins: %s' % (len(table[-1]), table[-1])
    else:
        print 'No solution possible'


coins = [1, 3, 4]
value = 11
solve_coin_change(coins, value)
