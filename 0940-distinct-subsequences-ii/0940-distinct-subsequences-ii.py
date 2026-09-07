class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD = 10**9 + 7
        n = len(s)
        
        # dp[i] stores count of distinct subsequences using s[:i]
        dp = [0] * (n + 1)
        dp[0] = 1  # Empty subsequence
        
        # Tracks the 1-based last seen index for each character 'a' through 'z'
        last_seen = {}
        
        for i in range(1, n + 1):
            char = s[i - 1]
            dp[i] = (2 * dp[i - 1]) % MOD
            
            # Subtract duplicates if character was seen before
            if char in last_seen:
                prev_index = last_seen[char]
                dp[i] = (dp[i] - dp[prev_index - 1] + MOD) % MOD
                
            last_seen[char] = i

        # Subtract 1 to exclude the empty subsequence
        return (dp[n] - 1 + MOD) % MOD