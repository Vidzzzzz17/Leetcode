from typing import List

class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        res = -1  # all bits set
        for i, v in enumerate(nums):
            if v != i:
                res &= v
        return 0 if res == -1 else res