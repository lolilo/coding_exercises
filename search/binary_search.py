def binary_search(l, t):
    found = False
    while not found and len(l) > 0:
        i = len(l)//2
        if t > i: 
            l = l[i+1:]
        elif t < i:
            l = l[:i]
        else:
            found = True
    return found


l = range(5)

print binary_search(l, 2)
