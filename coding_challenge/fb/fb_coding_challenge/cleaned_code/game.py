import re

def get_test_cases():
    T = int(raw_input())
    testcases = []
    for i in xrange(T):
        testcase = raw_input()
        testcases.append(testcase)
    return testcases

# convert number to binary
# check if a positive integer exists such that 2^k < n and n-2^k in binary
# has the same number of 1's as n

def print_who_wins(l):
    for i in l:
        n = int(i)
        binary_n = bin(n)
        k = 0

        winner = "Second Player"

        while 2**k < n:
            new_n_binary = bin(n - 2**k)

            if re.findall('[1]', new_n_binary) == re.findall('[1]', binary_n):

                if winner == "Second Player":
                    winner = "First Player"
                else: # winner = First Player
                    winner = "Second Player"
                n = n - 2**k
                k = 0
                continue

            k += 1

        print winner

def main():
    print_who_wins(get_test_cases())

if __name__ == "__main__":
    main()
