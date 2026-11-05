from typing import List

class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        w = valueDiff + 1
        buckets = {}

        for i, x in enumerate(nums):
            b = x // w  # floor division handles negatives correctly

            if b in buckets:
                return True
            if b - 1 in buckets and x - buckets[b - 1] <= valueDiff:
                return True
            if b + 1 in buckets and buckets[b + 1] - x <= valueDiff:
                return True

            buckets[b] = x

            # keep only the last indexDiff elements
            if i >= indexDiff:
                del buckets[nums[i - indexDiff] // w]

        return False