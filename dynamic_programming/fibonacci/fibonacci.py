def fib_recursive(n):
    if n < 2:
        return n
    return fib_recursive(n-2) + fib_recursive(n-1)

# print fib_recursive(10)
# print map(fib_recursive, range(0, 10))

def fib_loop(n):
    a, b = 1, 1 # these are the first two
    for i in range(n-2): # offset by the first two, n < 2 returns 1
        temp = b
        b = a + b
        a = temp
    return b

def fib_loop_with_tuples(n):
    a, b = 1, 1
    for i in range(n-2):
        a, b = b, a+b
    return b

def fib_memoization(n):
    def fib_loop(n):
        a, b = 1, 1 # these are the first two
        for i in range(n-2): # offset by the first two, n < 2 returns 1
            temp = b
            b = a + b
            a = temp
        return b

    def memoize(fn, arg):
        memo = {}
        if arg not in memo:
            memo[arg] = fn(arg)
        return memo[arg]

    return memoize(fib_loop, n) 


# http://ujihisa.blogspot.com/2010/11/memoized-recursive-fibonacci-in-python.html
# decorator

def memoize(f):
    cache = {}
    def decorated_function(*args):
        if args in cache:
            return cache[args]
        else:
            cache[args] = f(*args)
            return cache[args]
    return decorated_function

@memoize
def fib(n):
    if n < 2:
        return n
    return fib_recursive(n-2) + fib_recursive(n-1)

    # fancy stuff
    # return n if n < 2 else fib(n-2) + fib(n-1)

def main():

    print fib_recursive(10)
    print fib_loop(10)
    print fib_loop_with_tuples(10)
    print fib_memoization(10)
    print fib(10)

if __name__ == "__main__":
    main()
