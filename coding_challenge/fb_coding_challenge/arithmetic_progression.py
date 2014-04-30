
# user_input = raw_input()

n = "5"
ap = "1 11 31 41 51"

# arithmetic progression. 
# two lines of raw input (stdin), first one being length of given progression, second the arithmetic progression
# find the missing number and print it to stdout

# ap = ap.split()
# print ap

def find_missing(n, ap):
    ap = ap.split()
    for i in range(len(ap)):
        ap[i] = int(ap[i])
        # print type(ap[0])

    prev = ap[1] - ap[0]
    curr = 0

    for i in range(int(n)):
        # print type(ap[i+1]), type(ap[i])
        curr = ap[i + 1] - ap[i]
        if curr != prev:
            if ap[i+1] > ap[i]:
                if prev < curr:
                    return ap[i] + prev
                else:
                    return ap[i] + curr
            else:
                if prev > curr:
                    return ap[i] + prev
                else:
                    return ap[i] + curr    

print find_missing(n, ap)



# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(raw_input())

#user_input = user_input.split('\n')

#print n

ap = raw_input()
# print ap

def find_missing(n, ap):

    ap = ap.split()
    for i in range(len(ap)):
        ap[i] = int(ap[i])
        # print type(ap[0])

    prev = ap[1] - ap[0]
    curr = 0

    for i in range(int(n)):
        # print type(ap[i+1]), type(ap[i])
        curr = ap[i + 1] - ap[i]
        if curr != prev:
            if ap[i+1] > ap[i]:
                if prev < curr:
                    return ap[i] + prev
                else:
                    return ap[i] + curr
            else:
                if prev > curr:
                    return ap[i] + prev
                else:
                    return ap[i] + curr


print find_missing(n, ap)


# 45 minutes. Finished with 18 minutes to spare. 7 test cases. Didn't consider decreasing progression at first, so passed 5/7 tests. 
# Fixed easily enough.