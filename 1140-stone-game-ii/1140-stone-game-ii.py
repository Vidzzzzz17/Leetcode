class Solution:
    def stoneGameII(self, piles):
        n = len(piles)
        # suffix sums
        suffix = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix[i] = suffix[i + 1] + piles[i]
        
        from functools import lru_cache
        
        @lru_cache(maxsize=None)
        def dp(i, m):
            if i >= n:
                return 0
            if i + 2 * m >= n:
                return suffix[i]  # take everything left
            best = 0
            for X in range(1, 2 * m + 1):
                if i + X > n:
                    break
                best = max(best, suffix[i] - dp(i + X, max(m, X)))
            return best
        
        result = dp(0, 1)
        dp.cache_clear()  # good practice: avoids stale cache across test cases
        return result