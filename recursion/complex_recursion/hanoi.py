def hanoi(n, source, dest, helper):
    if n > 0:
        hanoi(n-1, source, helper, dest)
        ring = source.pop()
        dest.append(ring)
        hanoi(n-1, helper, dest, source)

t1 = [5, 4, 3, 2, 1]
t2 = []
t3 = []
hanoi(len(t1), t1, t2, t3)

print t1,t2,t3
