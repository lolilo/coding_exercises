"""Question 1 / 1 (Game)
The beauty of a number X is the number of 1s in the binary representation of X.

Two players are plaing a game. There is number n written on a black board. The game is played as following:

Each time a player chooses an integer number (0 <= k) so that 2^k is less than n and (n-2^k) has as beautiful as n.
Next he removes n from blackboard and writes n-2^k instead.
The player that can not continue the game (there is no such k that satisfies the constrains) looses the game.

The First player starts the game and they play in turns alternatively. Knowing that both two players play optimally you have to specify the winner.

Input:

First line of the Input contains an integer T, the number of testcase. 0 <= T <= 5.

Then follow T lines, each containing an integer n.

 n more than 0 and less than 10^9 +1.

Output

For each testcase print "First Player" if first player can win the game and "Second Player" otherwise.

Sample Input

7
1
2
8
16
42
1000
123

Sample Output

Second Player
First Player
First Player
Second Player
Second Player
First Player
Second Player

Explanation

In the first example n is 1 and first player can't change it so the winner is the second player.

In the second example n is 2, so the first player subtracts 1 (2^0) from n and the second player looses the game.
"""

import re

def get_test_cases():
    T = int(raw_input('T > '))
    testcases = []
    for i in xrange(T):
        testcase = raw_input('testcase > ')
        testcases.append(testcase)
    return testcases

# convert number to binary
# check if a positive integer exists such that 2^k < n and n-2^k in binary
# has the same number of 1's as n

def print_who_wins(l):
    for i in l:
        n = int(i)
        binary_n = bin(n)
        # find valid k
        k = 0

        winner = "Second Player"
        # print 'n is', n
        # print 'k is', k
        # print '2^k is', 2**k
        # print '2^k < n is', 2**k < n
        
        while 2**k < n:
            # print 'n is', n
            # print 'k is', k
            # print '2^k is', 2**k
            new_n_binary = bin(n - 2**k)


            # print re.findall('[1]', new_n_binary),
            # print re.findall('[1]', binary_n)

            if re.findall('[1]', new_n_binary) == re.findall('[1]', binary_n):

                # print 'switching winner'
                if winner == "Second Player":
                    winner = "First Player"
                else: # winner = First Player
                    winner = "Second Player"
                # print n - 2**k
                n = n - 2**k
                k = 0
                # print ''
                continue

            k += 1

        print winner

def main():
    print_who_wins(get_test_cases())

if __name__ == "__main__":
    main()

# 1:22 time remaining from 2 hrs, so 40< minutes...
# ...turns out the entire two hours is for one problem. What. 
