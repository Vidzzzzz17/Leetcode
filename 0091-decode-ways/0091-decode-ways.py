class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0':
            return 0

        prev2, prev1 = 1, 1  # dp[i-2], dp[i-1]

        for i in range(2, len(s) + 1):
            cur = 0
            # Single-digit decode
            if s[i - 1] != '0':
                cur += prev1
            # Two-digit decode
            two = int(s[i - 2:i])
            if 10 <= two <= 26:
                cur += prev2
            prev2, prev1 = prev1, cur

            if cur == 0:  # no valid decoding possible from here on
                return 0

        return prev1
                