def max_subarray(l):
    curr_max, global_max = l[0], l[0]
    for i in xrange(1, len(l)):
    	num = l[i]
        curr_max = max(num, curr_max + num)
        global_max = max(global_max, curr_max)
    return global_max


l1 = [1, 2, 3, -20, 5]
l2 = [5, 5, -1, 4]
l3 = [5, 5, -1, -1, -20, 4]
l4 = [100, -1, 100]
l5 = [-500]
l6 = [-500, -400]

print max_subarray(l1) == 6
print max_subarray(l2) == 13
print max_subarray(l3) == 10
print max_subarray(l4) == 199
print max_subarray(l5) == -500
print max_subarray(l6) == -400
