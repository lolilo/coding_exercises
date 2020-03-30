def mergeKLists(lists):    

    if not lists:
        return [] 
    merged_list = []

    first_list = lists[0]
    for list_index in xrange(len(lists) - 1):
        second_list = lists[list_index + 1]
        
        first_list = mergeLists(first_list, second_list)
    return first_list
    
    
def mergeLists(l1, l2):
    i = 0
    j = 0 
    
    merged_list = []
    
    while i < len(l1) and j < len(l2):
        if l1[i] < l2[j]:
            merged_list.append(l1[i])
            i += 1
        else:
            merged_list.append(l2[j])
            j += 1
    while i < len(l1):
        merged_list.append(l1[i])
        i += 1
    while j < len(l2):
        merged_list.append(l2[j])
        j += 1
    
    return merged_list


import unittest

class Test(unittest.TestCase):
    def test_mergeKLists(self):
        self.assertEqual(mergeKLists([[1, 4, 5], [1, 3, 4], [2, 6]]), [1, 1, 2, 3, 4, 4, 5, 6])
        self.assertEqual(mergeKLists([[20]]), [20])
        self.assertEqual(mergeKLists([]), [])

unittest.main()