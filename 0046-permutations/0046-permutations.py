class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        result = []
        n = len(nums)
        
        def backtrack(current: list[int], used: set[int]) -> None:
            if len(current) == n:
                result.append(current[:])  # copy, since current is mutated afterward
                return
            
            for num in nums:
                if num in used:
                    continue
                
                current.append(num)
                used.add(num)
                
                backtrack(current, used)
                
                current.pop()
                used.remove(num)
        
        backtrack([], set())
        return result