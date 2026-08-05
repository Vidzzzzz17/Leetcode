from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        
        def backtrack(start: int, remain: int, path: List[int]):
            if remain == 0:
                res.append(path[:])
                return
            if remain < 0:
                return
            
            for i in range(start, len(candidates)):
                # Pruning: since sorted, all later numbers are >= candidates[i]
                if candidates[i] > remain:
                    break
                
                path.append(candidates[i])
                # i (not i+1) because we can reuse the same element unlimited times
                backtrack(i, remain - candidates[i], path)
                path.pop()
        
        backtrack(0, target, [])
        return res