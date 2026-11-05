from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Phase 1: find a meeting point inside the cycle
        slow = fast = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        # Phase 2: find the cycle entrance
        slow = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow