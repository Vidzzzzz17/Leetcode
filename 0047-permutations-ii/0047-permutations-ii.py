class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        n = len(nums)
        result = []
        used = [False] * n
        
        def backtrack(current: list[int]) -> None:
            if len(current) == n:
                result.append(current[:])
                return
            
            for i in range(n):
                if used[i]:
                    continue
                
                # Skip duplicates: only use nums[i] if it's the first "unused" 
                # occurrence among equal values at this position
                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue
                
                used[i] = True
                current.append(nums[i])
                
                backtrack(current)
                
                current.pop()
                used[i] = False
        
        backtrack([])
        return result