from typing import List

class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        result = [0] * k
        cnt = [0] * k  # subarrays ending at the previous index, by product mod k
        for v in nums:
            v %= k
            new = [0] * k
            for r in range(k):
                if cnt[r]:
                    new[(r * v) % k] += cnt[r]
            new[v % k] += 1  # subarray consisting of just this element
            cnt = new
            for r in range(k):
                result[r] += cnt[r]
        return result