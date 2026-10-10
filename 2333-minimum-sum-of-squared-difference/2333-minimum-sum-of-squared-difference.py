from typing import List

class Solution:
    def minSumSquareDiff(self, nums1: List[int], nums2: List[int], k1: int, k2: int) -> int:
        k = k1 + k2
        d = sorted((abs(a - b) for a, b in zip(nums1, nums2)), reverse=True)
        if sum(d) <= k:
            return 0

        n = len(d)
        d.append(0)  # sentinel
        cnt = 1
        i = 0
        # d[0..i] are all leveled to value d[i]
        while i < n:
            cur = d[i]
            nxt = d[i + 1]
            cost = cnt * (cur - nxt)
            if cost <= k:
                k -= cost
                cnt += 1
                i += 1
            else:
                break

        # Top cnt elements currently equal d[i]  (cnt == i + 1)
        level = d[i]
        q, r = divmod(k, cnt)
        base = level - q          # value of most of the top group
        # r elements are one lower (base - 1), the rest at base
        total = r * (base - 1) ** 2 + (cnt - r) * base ** 2
        for j in range(i + 1, n):
            total += d[j] ** 2
        return total