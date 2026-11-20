from collections import defaultdict
from typing import List

class Solution:
    def maxSelectedElements(self, nums: List[int]) -> int:
        nums.sort()
        dp = defaultdict(int)
        ans = 1
        for x in nums:
            dp[x + 1] = dp[x] + 1   # use x as x+1
            dp[x] = dp[x - 1] + 1   # use x as x
            ans = max(ans, dp[x], dp[x + 1])
        return ans