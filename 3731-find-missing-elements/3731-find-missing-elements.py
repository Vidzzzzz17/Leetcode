class Solution:
    def findMissingElements(self, nums: list[int]) -> list[int]:
        num_set = set(nums)
        low, high = min(nums), max(nums)
        
        return [n for n in range(low, high + 1) if n not in num_set]