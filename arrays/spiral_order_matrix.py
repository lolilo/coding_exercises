# Given a matrix of m * n elements (m rows, n columns), 
# return all elements of the matrix in spiral order.

class Solution:
    # @param A : tuple of list of integers
    # @return a list of integers
    def spiralOrder(self, A):
        num_of_arrays = len(A)
        len_A = len(A[0])
        
        curr_first_array_index = 0
        curr_last_array_index = num_of_arrays - 1
        curr_first_index = 0
        curr_last_index = len_A - 1
        
        spiral_array = []
        direction = 0
        
        while curr_first_array_index <= curr_last_array_index and curr_first_index <= curr_last_index:
            if direction == 0:
                for index in xrange(curr_first_index, curr_last_index + 1):
                    spiral_array.append(A[curr_first_array_index][index])
                curr_first_array_index += 1
                direction = 1
            elif direction == 1:
                for array in xrange(curr_first_array_index, curr_last_array_index + 1):
                    spiral_array.append(A[array][curr_last_index])
                curr_last_index -= 1
                direction = 2
            elif direction == 2:
                for index in xrange(curr_last_index, curr_first_index - 1, -1):
                    spiral_array.append(A[curr_last_array_index][index])
                curr_last_array_index -= 1
                direction = 3
            elif direction == 3:
                for array_index in xrange(curr_last_array_index, curr_first_array_index - 1, -1):
                    spiral_array.append(A[array_index][curr_first_index])
                curr_first_index += 1
                direction = 0
        
        return spiral_array

import unittest

class Test(unittest.TestCase):
    def test_spiralOrder(self):
        sol = Solution()
        self.assertEqual(sol.spiralOrder([[1]]), [1])
        self.assertEqual(sol.spiralOrder(
            [
                [1, 2],
                [3, 4],
                [5, 6]
            ]
            ), [1, 2, 4, 6, 5, 3])


unittest.main()
