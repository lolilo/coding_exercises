# user_input = raw_input()

# arithmetic progression. 
# two lines of raw input (stdin), first one being length of given progression, second the arithmetic progression
# find the missing number and print it to stdout

# Enter your code here. Read input from STDIN. Print output to STDOUT

#user_input = user_input.split('\n')
#print n


# We're given the length of the given progression...how can I better use this information? 
# Do I not need to transform stuff to an int list?
# How can I reduce time complexity?
def find_missing(n, ap):
    length_of_progression = int(n)
    ap = ap.split()
    # create a list of int
    for i in range(length_of_progression):
        ap[i] = int(ap[i])

    init_diff = ap[1] - ap[0]

    for i in range(length_of_progression-1):
        this = ap[i]
        next = ap[i+1]
        curr_diff = next - this

        if curr_diff != init_diff:
            if next > this: # progression increasing
                if init_diff < curr_diff: # insert @ curr_diff
                    return this + init_diff
                else: 
                    return ap[0] + curr_diff
            else: # progression decreasing
                if init_diff < curr_diff: # abs(init_diff) > abs(curr_diff), insert @ init_diff
                    return ap[0] + curr_diff
                else: # missing number @ curr_diff
                    return this + init_diff

def loop():
    while True:
        n = int(raw_input('n > '))
        ap = raw_input('arithmetic progression > ')
        print find_missing(n, ap)

def main():
    # loop()
    print find_missing(n, ap)

if __name__ == "__main__":
    n = "5"
    ap = "1 21 31 41 51"
    main()

# 45 minutes. Finished with 18 minutes to spare. 7 test cases. 
# Didn't consider decreasing progression at first, so passed 5/7 tests. 
# Fixed easily enough.
