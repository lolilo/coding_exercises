# time complexity: O(nlogn) 
# space complexity: 
def merge_sort_in_place(original_list):
    if len(original_list) > 1:
        mid = len(original_list)//2
        left_half = original_list[:mid]
        right_half = original_list[mid:]

        merge_sort_in_place(left_half)
        merge_sort_in_place(right_half)

        left_index = 0
        right_index = 0
        original_list_index = 0

        while left_index < len(left_half) and right_index < len(right_half):
            if left_half[left_index] < right_half[right_index]:
                original_list[original_list_index] = left_half[left_index]
                left_index = left_index + 1
            else:
                original_list[original_list_index] = right_half[right_index]
                right_index = right_index + 1
            original_list_index = original_list_index + 1

        original_list_index, original_list = place_remaining_list_elements(left_index, left_half, original_list_index, original_list)
        _, original_list = place_remaining_list_elements(right_index, right_half, original_list_index, original_list)

    return original_list

def place_remaining_list_elements(index, half_list, original_list_index, original_list):
    while index < len(half_list):
        original_list[original_list_index] = half_list[index]
        index = index + 1
        original_list_index = original_list_index + 1
    return original_list_index, original_list


import unittest

class Test(unittest.TestCase):
    def test_merge_sort_in_place(self):
        self.assertEqual(merge_sort_in_place([54, 26, 93, 17, 77, 31, 44, 55, 20]), [17, 20, 26, 31, 44, 54, 55, 77, 93])
        self.assertEqual(merge_sort_in_place([20]), [20])
        self.assertEqual(merge_sort_in_place([]), [])

unittest.main()
