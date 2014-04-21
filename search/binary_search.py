def binary_search(l, t):
    found = False
    while not found and len(l) > 0:
        i = len(l)//2
        if t > i: 
            l = l[i+1:] #why doesn't this give an index error
        elif t < i:
            l = l[:i]
        else:
            found = True
    return found



def binary_search2(l, t):
    while len(l) > 0:
        i = len(l)//2
        if t > i: 
            l = l[i+1:] #why doesn't this give an index error
        elif t < i:
            l = l[:i]
        else:
            return True
    return False

l = range(5)

print binary_search(l, 20)
