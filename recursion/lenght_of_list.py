def length(l):
    if not l:
        return 0 
    return 1 + length(l[1:])

l = range(10)
print length(l)

def length_n00b(l, c):
    if l:
        return length_n00b(l[1:], c+1)
    return c

print length_n00b(l, 0)
