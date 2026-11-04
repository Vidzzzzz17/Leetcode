from typing import List

class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return 0

        lo, hi = min(nums), max(nums)
        if lo == hi:
            return 0

        size = max(1, (hi - lo) // (n - 1))   # bucket width
        count = (hi - lo) // size + 1         # number of buckets

        bucket_min = [None] * count
        bucket_max = [None] * count

        for x in nums:
            b = (x - lo) // size
            if bucket_min[b] is None:
                bucket_min[b] = bucket_max[b] = x
            else:
                bucket_min[b] = min(bucket_min[b], x)
                bucket_max[b] = max(bucket_max[b], x)

        best = 0
        prev_max = lo
        for b in range(count):
            if bucket_min[b] is None:
                continue
            best = max(best, bucket_min[b] - prev_max)
            prev_max = bucket_max[b]
        return best