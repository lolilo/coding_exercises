def insert(intervals, newInterval):
    """
    :type intervals: List[List[int]]
    :type newInterval: List[int]
    :rtype: List[List[int]]
    """

    start_of_new_interval, end_of_new_interval = newInterval[0], newInterval[-1]
    left_of_new_interval = [interval for interval in intervals if interval[-1] < start_of_new_interval]
    right_of_new_interval = [interval for interval in intervals if interval[0] > end_of_new_interval]
    
    len_left_of_new_interval = len(left_of_new_interval)
    len_right_of_new_interval = len(right_of_new_interval)
    if len_left_of_new_interval + len_right_of_new_interval != len(intervals):
        # merge
        start_of_new_interval = min(start_of_new_interval, intervals[len_left_of_new_interval][0])
        end_of_new_interval = max(end_of_new_interval, intervals[(-len_right_of_new_interval - 1)][-1])
    return left_of_new_interval + [[start_of_new_interval, end_of_new_interval]] + right_of_new_interval


print insert([[1, 3], [6, 9]], [2, 5]) == [[1, 5], [6, 9]]
print insert([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]) == [[1, 2], [3, 10], [12, 16]]

