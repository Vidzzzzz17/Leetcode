from typing import List
import bisect

class Solution:
    def countNonDecreasingSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        # Reverse trick: process from the right with monotonic stack,
        # sliding window where we shrink from the right end.
        # Reverse the problem: for fixed l, maximal r is monotone in l.
        # Use a two-pointer with a deque over the window, processing l from right to left.
        from collections import deque
        ans = 0
        # Walk l from n-1 down to 0; window is [l, r]; r shrinks as l decreases.
        # cost(l, r) = sum_{i=l..r}(prefmax - nums[i]).
        # Adding l on the left: new element becomes the start; elements after it
        # up to next greater element get raised to nums[l].
        # Maintain a stack of segments (value, count) from l going right.
        dq = deque()  # segments: [value, count, rightmost index of segment]
        total = 0     # current sum of prefix maxes over window
        sumv = 0      # sum of nums over window
        pre = [0] * (n + 1)
        for i in range(n):
            pre[i + 1] = pre[i] + nums[i]
        r = n - 1
        # segments stored as a list where index 0 is the leftmost segment
        # we push/pop at the left, and trim from the right.
        seg = deque()  # (value, start, end) leftmost first
        for l in range(n - 1, -1, -1):
            # add l on the left
            start, end = l, l
            cnt_total_add = nums[l]
            # absorb segments whose value <= nums[l]
            while seg and seg[0][0] <= nums[l]:
                v, s, e = seg.popleft()
                total -= v * (e - s + 1)
                end = e
            seg.appendleft((nums[l], l, end))
            total += nums[l] * (end - l + 1)
            # shrink window from the right while cost too large
            while True:
                cost = total - (pre[r + 1] - pre[l])
                if cost <= k:
                    break
                v, s, e = seg[-1]
                total -= v
                if e == s:
                    seg.pop()
                else:
                    seg[-1] = (v, s, e - 1)
                r -= 1
            ans += r - l + 1
        return ans