
# open and read the file
# store IDs into a hash, key = ID, value = frequency of apperance

# use a heap to keep track of the top ten IDs as we are passing it into the hash

# otherwise, we could do one pass to store into the hash, 
# then iterate through all entries of the hash and keep track of highest values with a heap

# wrong stuff following
# or we could switch keys and values in the hash map and sort the keys, return the values mapping to the highest value keys
# THIS DOES NOT WORK FOR DUPLICATE VALUES. DON'T DO THIS. 
# new_d = {value:key for key,value in d.iteritems()}
# dictionary comprehension

import heap_module

f = open('IDs.txt')
id_list = [x.strip() for x in f]
f.close()

# print ID_list

d = {}
for item in id_list:
    if item in d:
        d[item] += 1
    else:
        d[item] = 1

# print d
# print len(d)

# min heap
top_ten = heap_module.Heap()

for key in d:
    frequency = d[key]
    if top_ten.size < 10:
        top_ten.insert(key)
    else: # already have ten things in the heap
        
        min_id_in_heap = top_ten.heap[1]
        min_frequency_in_heap = d[min_id_in_heap]

        if min_frequency_in_heap < frequency:
            top_ten.heap.popMin()
            top_ten.insert(key)

            # need to fix heap implementation if we want to do this. bah! 
            # currently, this heap only handles integers
            # I wanted to only store keys in the heap, and then look up keys in the dictionary
            # to see their frequency value.


