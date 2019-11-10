def merge_intervals(intervals):
    len_intervals = len(intervals)
    if len_intervals < 1:
        return
    
    sorted_intervals = sorted(intervals, key=lambda interval: interval[0])
    out = [sorted_intervals[0]]

    for interval_index in xrange(1, len_intervals):
        interval = sorted_intervals[interval_index]
        first_num_of_interval = interval[0]
        last_num_of_interval = interval[-1]
        last_num_of_last_interval_of_output_entry = out[-1][-1]
        if first_num_of_interval <= last_num_of_last_interval_of_output_entry:
            # merge interval
            out[-1][-1] = max(last_num_of_last_interval_of_output_entry, last_num_of_interval)
        else:
            out += [interval]
    return out

print merge_intervals([[1,3],[2,6],[8,10],[15,18]]) == [[1,6],[8,10],[15,18]]
print merge_intervals([[1,4],[4,5]]) == [[1,5]]
print merge_intervals([[1,4],[0,1]]) == [[0,4]]