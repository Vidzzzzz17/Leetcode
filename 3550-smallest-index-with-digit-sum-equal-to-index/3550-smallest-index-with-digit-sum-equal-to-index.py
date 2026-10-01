from typing import List

class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i, x in enumerate(nums):
            total = 0
            while x:
                total += x % 10
                x //= 10
            if total == i:
                return i
        return -1