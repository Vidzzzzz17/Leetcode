import random
from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        target = len(nums) - k
        arr = nums

        while True:
            pivot = random.choice(arr)
            less = [v for v in arr if v < pivot]
            equal = [v for v in arr if v == pivot]
            greater = [v for v in arr if v > pivot]

            if target < len(less):
                arr = less
            elif target < len(less) + len(equal):
                return pivot
            else:
                target -= len(less) + len(equal)
                arr = greater