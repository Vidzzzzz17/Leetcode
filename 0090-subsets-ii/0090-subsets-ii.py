class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        nums.sort()  # Sort to group duplicates together
        res = []
        
        def backtrack(start: int, path: list[int]):
            # Append a copy of the current subset to results
            res.append(list(path))
            
            for i in range(start, len(nums)):
                # Skip duplicate elements at the same depth level
                if i > start and nums[i] == nums[i - 1]:
                    continue
                
                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()  # Backtrack
                
        backtrack(0, [])
        return res