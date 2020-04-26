"""
Given a set of possible scores in a game and a total target score, 
print out all the possible ways to arrive at that target score.

([2, 6, 10], 10) -> [[2, 2, 2, 2, 2], [6, 2, 2], [10]]
"""

def combinationSum(scores, index, target):
    if target == 0:
        return [[]]

    curr_res = []
    for curr_i in range(index, len(scores)):
        if target < scores[curr_i]:
            break
        next_res = combinationSum(scores, curr_i, target - scores[curr_i])

        if next_res != []:
            for array in next_res: 
                curr_res.append(array + [scores[curr_i]])
    return curr_res

print combinationSum([2, 3, 6, 7], 0, 7) == [[3, 2, 2], [7]]
print combinationSum([2, 6, 10], 0, 10) == [[2, 2, 2, 2, 2], [6, 2, 2], [10]]


class Solution:
    def combinationSum(self, candidates, target):
        # candidates.sort()
        return self.combinationSumHelper(candidates, 0, target)
    
    def combinationSumHelper(self, candidates, idx, target):
        if target == 0:
            return [[]]
        
        cur_res = []
        for i in range(idx, len(candidates)):
            if target < candidates[i]:
                break
            nxt_res = self.combinationSumHelper(candidates, i, target - candidates[i])
            
            if nxt_res != []:
                for s in nxt_res:
                    cur_res.append(s + [candidates[i]])
        return cur_res

print Solution().combinationSum([2, 3, 6, 7], 7) == [[3, 2, 2], [7]]
print Solution().combinationSumHelper([2, 3, 6, 7], 0, 7) == [[3, 2, 2], [7]]
print Solution().combinationSum([2, 6, 10], 10) == [[2, 2, 2, 2, 2], [6, 2, 2], [10]]
