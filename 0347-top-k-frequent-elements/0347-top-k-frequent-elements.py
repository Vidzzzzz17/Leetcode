from collections import Counter
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        buckets = [[] for _ in range(len(nums) + 1)]
        for val, freq in count.items():
            buckets[freq].append(val)

        result = []
        for freq in range(len(nums), 0, -1):
            for val in buckets[freq]:
                result.append(val)
                if len(result) == k:
                    return result
        return result