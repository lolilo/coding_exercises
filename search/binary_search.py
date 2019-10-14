def binary_search(l, target):
    start_index, end_index = 0, len(l) - 1

    while start_index <= end_index:
        mid_index = start_index + (end_index - start_index) // 2
        value = l[mid_index]

        if value == target:
            return mid_index
        elif value < target:
            start_index = mid_index + 1
        else:
            end_index = mid_index -1 

    return -1

def recursive_binary_search(l, target):
    if len(l) < 1:
        return False

    mid_index = len(l)//2
    value = l[mid_index]

    if value == target:
        return True
    if target > value:
        return recursive_binary_search(l[mid_index + 1:], target)
    elif target < value:
        return recursive_binary_search(l[:mid_index], target)


import unittest

class Test(unittest.TestCase):
    def test_binary_search(self):
        self.assertEqual(binary_search(range(5), 3), 3)
        self.assertEqual(binary_search(range(5), 5), -1)

    def test_recursive_binary_search(self):             
        self.assertEqual(recursive_binary_search(range(5), 3), True)

unittest.main()

# l = range(5)
# print recursive_binary_search(l, 0)