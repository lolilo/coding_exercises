# in place
def quick_sort(l):
    def quicksort_helper(l, first, last):
        if first < last: 
            pivot = sort_list_and_return_pivot(l, first, last)
            # print l
            # pivot is in place, so don't need to touch it anymore
            quicksort_helper(l, first, pivot - 1)
            quicksort_helper(l, pivot + 1, last)

    # sorts l between first and last and returns a new pivot
    def sort_list_and_return_pivot(l, first, last): 
        # somewhat arbitrary pivot point selection
        # choosing the first value means O(n^2) for a reversely sorted list. Each chosen pivot will always be the largest value. 

        # median of three is one such method
        # https://www.quora.com/What-is-the-best-way-to-choose-a-pivot-element-in-Quicksort

        # Here we will choose the first element
        
        pivot_val = l[first] 
        left_i = first + 1 # left index
        right_i = last # right index

        while left_i <= right_i:
            while l[left_i] <= pivot_val and left_i <= right_i:
                left_i += 1
            while l[right_i] >= pivot_val and left_i <= right_i:
                right_i -= 1
            # at this point, left_i and right_i are pointing to values that should be swapped
            # or left_i > right_i
            
            if left_i < right_i:
                l[left_i], l[right_i] = l[right_i], l[left_i]

                left_i += 1
                right_i -= 1
        
        # at this point, left_i > right_i. 
        # right_i is pointing to an element smaller than the first element
        # Place in the pivot value, then return new pivot index. 

        l[right_i], l[first] = l[first], l[right_i]
        return right_i # return an index value

    quicksort_helper(l, 0, len(l) - 1)
    return l

# this takes up extra space for the lists
# returns a new list, sorted. original list unchanged. 
def recursive_sort(array):
    less_than_pivot = []
    equal_to_pivot = []
    greater_than_pivot = []
    new_list = []

    if len(array) > 1:
        pivot_val = array[0]
        for x in array:
            if x < pivot_val:
                less_than_pivot.append(x)
            if x == pivot_val:
                equal_to_pivot.append(x)
            if x > pivot_val:
                greater_than_pivot.append(x)
        return recursive_sort(less_than_pivot) + equal_to_pivot + recursive_sort(greater_than_pivot)
    else:  
    # At the end of the recursion, when you only have one element in your array, 
    # return the array.
        return array

def main():
    a = [12, 4, 5, 6, 7, 3, 1, 15]
    sorted_a = [1, 3, 4, 5, 6, 7, 12, 15]

    print quick_sort(a) == sorted(a)
    print recursive_sort(a) == sorted(a)


if __name__ == "__main__":
    main()
