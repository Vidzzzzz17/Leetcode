class Solution:
    def minimumDeletions(self, nums: list[int]) -> int:
        n = len(nums)
        if n == 1:
            return 1

        min_idx = nums.index(min(nums))
        max_idx = nums.index(max(nums))

        a = min(min_idx, max_idx)
        b = max(min_idx, max_idx)

        # Option 1: Remove both from front
        op1 = b + 1
        # Option 2: Remove both from back
        op2 = n - a
        # Option 3: Remove one from front, one from back
        op3 = (a + 1) + (n - b)

        return min(op1, op2, op3)