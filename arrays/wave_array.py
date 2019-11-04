def wave_array(array):
	array.sort()
	len_array = len(array)
	for index in xrange(0, len_array, 2):
		if index + 1 >= len_array:
			break
		array[index], array[index + 1] = array[index + 1], array[index]

	return array


import unittest

class Test(unittest.TestCase):
    def test_wave_array(self):

        self.assertEqual(wave_array([1]), [1])
        self.assertEqual(
        	wave_array([1, 2, 3, 4]), 
        	[2, 1, 4, 3]
        )

        self.assertEqual(
        	wave_array([1, 2, 3, 4, 6]), 
        	[2, 1, 4, 3, 6]
        )

unittest.main()