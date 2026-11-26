import random
from collections import Counter
from typing import List

class Solution:
    def smallestUniqueSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        M = (1 << 61) - 1
        B = random.randrange(10**6, M - 1)

        h = [0] * (n + 1)
        pw = [1] * (n + 1)
        for i, x in enumerate(nums):
            h[i + 1] = (h[i] * B + x) % M
            pw[i + 1] = pw[i] * B % M

        def has_unique(L: int) -> bool:
            cnt = Counter()
            pL = pw[L]
            for i in range(n - L + 1):
                cnt[(h[i + L] - h[i] * pL) % M] += 1
            return any(v == 1 for v in cnt.values())

        lo, hi = 1, n  # length n is always unique
        while lo < hi:
            mid = (lo + hi) // 2
            if has_unique(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo