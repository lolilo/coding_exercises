## Example 5: Using memoization as decorator
class Memoize:
    def __init__(self, fn):
        self.fn = fn
        self.memo = {}
    def __call__(self, arg):
        print arg
        if arg not in self.memo:
            self.memo[arg] = self.fn(arg)
            # print self.memo[arg]
            return self.memo[arg]
 
@Memoize
def fib(n):
 a,b = 1,1
 for i in range(n-1):
  a,b = b,a+b
 return a

print fib(10)