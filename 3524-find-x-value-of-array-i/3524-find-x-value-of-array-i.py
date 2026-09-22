class Solution:
    def resultArray(self, nums: list[int], k: int) -> list[int]:
        ans = [0] * k
        dp = [0] * k  # Tracks subarray product counts ending at previous index
        
        for num in nums:
            val = num % k
            next_dp = [0] * k
            
            # Start a new subarray with current element
            next_dp[val] += 1
            
            # Extend existing subarrays
            for rem in range(k):
                if dp[rem] > 0:
                    next_dp[(rem * val) % k] += dp[rem]
            
            # Accumulate results
            for rem in range(k):
                ans[rem] += next_dp[rem]
                
            dp = next_dp
            
        return ans