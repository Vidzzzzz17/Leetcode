from typing import List

class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        nums.sort(key=lambda s: (len(s), s))
        return nums[-k]