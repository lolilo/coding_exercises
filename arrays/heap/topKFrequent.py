import heapq

def topKFrequentFailure(words, k):
    count = {}
    for word in words:
        if word in count:
            count[word] += 1
        else:
            count[word] = 1
    
    # heapq,
    # This module provides an implementation of the heap queue algorithm, 
    # also known as the priority queue algorithm.

    heap = []
    for word, freq in count.items():
        curr_heap_item = (freq, word)
        if len(heap) < k:
            heapq.heappush(heap, curr_heap_item)
        else:
            if heap[0][0] <= curr_heap_item[0] and curr_heap_item[1] < heap[0][1]:
                heapq.heapreplace(heap, curr_heap_item)

    return [heap_item[1] for heap_item in sorted(heap, key=lambda x: (-x[0], x[1]))]

def topKFrequent(words, k):
    count = {}
    for word in words:
        if word in count:
            count[word] += 1
        else:
            count[word] = 1
    
    heap = [(-freq, word) for word, freq in count.items()]
    
    # heapq,
    # This module provides an implementation of the heap queue algorithm, 
    # also known as the priority queue algorithm.
    
    # heapq.heapify(x)
    # Transform list x into a heap, in-place, in linear time.
    heapq.heapify(heap)

    # heapq.heappop(heap)
    # Pop and return the smallest item from the heap, maintaining the heap invariant. 
    return [heapq.heappop(heap)[1] for _ in range(k)]

import unittest

class Test(unittest.TestCase):
    def test_topKFrequent(self):
        self.assertEqual(
            topKFrequent(["i", "love", "leetcode", "i", "love", "coding"], 2), 
            ["i", "love"]
            )
        self.assertEqual(
            topKFrequent(["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], 4), 
            ["the","is","sunny","day"]
            )
        self.assertEqual(
            topKFrequent(["i", "love", "leetcode", "i", "love", "coding"], 1), 
            ["i"]
            )
        self.assertEqual(
            topKFrequent(["aaa","aa","a"], 2), 
            ["a", "aa"]
            )


unittest.main(exit=False)
