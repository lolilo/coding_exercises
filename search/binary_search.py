def binary_search(l, t):
    found = False
    while not found and len(l) > 0:
        i = l[len(l)//2]
        if t > i: 
            l = l[i+1:] #why doesn't this give an index error
        elif t < i:
            l = l[:i]
        else:
            found = True
    return found

# l = range(5)

# print binary_search(l, 20)

def binary_search2(l, t):
    while len(l) > 0:
        i = l[len(l)//2]
        if t > i: 
            l = l[i+1:] #why doesn't this give an index error
        elif t < i:
            l = l[:i]
        else:
            return True
    return False

# l = range(5)
# print binary_search2(l, 2)

def recursive_binary_search(l, t):
    if len(l) < 1:
        return False

    i = len(l)//2
    curr = l[i]

    if curr == t:
        return True
    if t > curr:
        return recursive_binary_search(l[i+1:], t)
    elif t < curr:
        return recursive_binary_search(l[:i], t)


l = range(5)
print recursive_binary_search(l, 0)