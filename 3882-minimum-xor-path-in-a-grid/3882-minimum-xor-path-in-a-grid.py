from typing import List

class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        # dp[j] is a bitmask (Python int) of reachable XOR values at column j
        dp = [0] * n

        def shift_xor(mask: int, v: int) -> int:
            # Map every set bit x in mask to bit (x ^ v)
            res = 0
            while mask:
                low = mask & -mask
                x = low.bit_length() - 1
                res |= 1 << (x ^ v)
                mask ^= low
            return res

        for i in range(m):
            for j in range(n):
                v = grid[i][j]
                if i == 0 and j == 0:
                    dp[0] = 1 << v
                    continue
                prev = 0
                if i > 0:
                    prev |= dp[j]        # from above
                if j > 0:
                    prev |= dp[j - 1]    # from left
                dp[j] = shift_xor(prev, v)

        mask = dp[n - 1]
        return (mask & -mask).bit_length() - 1