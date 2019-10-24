# You are in an infinite 2D grid where you can move in any of the 8 directions :

#  (x,y) to 
#     (x+1, y), 
#     (x - 1, y), 
#     (x, y+1), 
#     (x, y-1), 
#     (x-1, y-1), 
#     (x+1,y+1), 
#     (x-1,y+1), 
#     (x+1,y-1) 

# You are given a sequence of points and the order in which you need to cover the points. 
# Give the minimum number of steps in which you can achieve it. 
# You start from the first point.

# Given two integer arrays A and B, where A[i] is x coordinate and B[i] is y coordinate of ith point respectively.
# Return an Integer, i.e minimum number of steps.

def min_steps_in_infinite_grid(x_array, y_array):
	step_count = 0
	len_x = len(x_array)

	i = 0
	while i < len_x - 1:
		curr_position = (x_array[i], y_array[i])
		destination_position = (x_array[i + 1], y_array[i + 1])

		step_count += steps_between_points(curr_position, destination_position)
		i += 1

	return step_count

def steps_between_points(curr_position, destination_position):
	return max(abs(destination_position[0] - curr_position[0]), abs(destination_position[1] - curr_position[1]))

# [(0, 0), (1, 1), (1, 2)]
print min_steps_in_infinite_grid([0, 1, 1], [0, 1, 2]) == 2
print min_steps_in_infinite_grid([0], [0]) == 0
print min_steps_in_infinite_grid([], []) == 0
