class Solution:
    def missingInteger(self, nums: list[int]) -> int:
        n = len(nums)
        
        # Find longest sequential prefix
        i = 1
        while i < n and nums[i] == nums[i - 1] + 1:
            i += 1
        
        total = sum(nums[:i])
        
        num_set = set(nums)
        while total in num_set:
            total += 1
        
        return total