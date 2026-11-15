class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        cur_max = cur_min = result = nums[0]

        for x in nums[1:]:
            # Compute all three candidates before assigning, since cur_max is used twice
            candidates = (x, cur_max * x, cur_min * x)
            cur_max = max(candidates)
            cur_min = min(candidates)
            result = max(result, cur_max)

        return result