def max_subarray(l):
    max_ending_here, max_so_far = 0, 0
    for x in l:
        max_ending_here = max(0, max_ending_here + x)
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far


l1 = [1,2,3,-20,5]
l2 = [5,5,-1,4]
l3 = [5,5,-1,-1,-20,4]
print max_subarray(l1)
print max_subarray(l2)
print max_subarray(l3)
