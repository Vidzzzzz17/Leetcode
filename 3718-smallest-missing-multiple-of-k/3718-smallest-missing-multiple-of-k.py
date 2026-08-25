class Solution:
    def missingMultiple(self, nums: list[int], k: int) -> int:
        num_set = set(nums)
        target = k
        
        while target in num_set:
            target += k
            
        return target
        