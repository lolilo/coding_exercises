# http://stackoverflow.com/questions/13751572/dynamic-programming-optimal-coin-change
"""
It looks to me like the code is solving the problem for every cent value up 
until target cent value. Given a target value v and a set of coins C, 
you know that the optimal coin selection S has to be of the form union(S', c), 
where c is some coin from C and S' is the optimal solution for v - value(c) 
(excuse my notation). So the problem has optimal substructure. 
The dynamic programming approach is to solve every possible subproblem. 
It takes cents * size(C) steps, as opposed to something that blows up 
much more quickly if you just try to brute force the direct solution.

Nice and clear. Basically, we know that the collection of coins used to make change 
must consist of (a) some coin in coinValueList plus 
(b) a bunch of other coins used to make up the rest. 
So, "guess" a coin for (a), and look up the best way to make change on the rest. 
(Conveniently, the rest is smaller than change, so we must have found 
an optimal solution for it in an earlier loop iteration.) 
If we repeat this for every possible guess for (a) (i.e. every different coin value), 
then (at least) one of these (a)s plus its corresponding (b) must be optimal.
"""

def make_change(coinValueList,change,minCoins):
   # Solve the problem for each number of cents less than the target
   for cents in range(change+1):

      # At worst, it takes all pennies, so make that the base solution
      coinCount = cents

      # Try all coin values less than the current number of cents
      for j in [c for c in coinValueList if c <= cents]:

            # See if a solution to current number of cents minus the value
            # of the current coin, with one more coin added is the best 
            # solution so far  
            if minCoins[cents-j] + 1 < coinCount:
               coinCount = minCoins[cents-j]+1

      # Memoize the solution for the current number of cents
      minCoins[cents] = coinCount

   # By the time we're here, we've built the solution to the overall problem, 
   # so return it
   return minCoins[change]


print make_change([1, 10, 25], 30, {})
