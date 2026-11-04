from typing import List

class Solution:
    def smallestTrimmedNumbers(self, nums: List[str], queries: List[List[int]]) -> List[int]:
        n = len(nums)
        ans = []
        for k, trim in queries:
            order = sorted(range(n), key=lambda i: (nums[i][-trim:], i))
            ans.append(order[k - 1])
        return ans