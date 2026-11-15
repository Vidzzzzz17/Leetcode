class Solution:
    def findMin(self, nums: list[int]) -> int:
        lo, hi = 0, len(nums) - 1

        while lo < hi:
            mid = (lo + hi) // 2

            if nums[mid] > nums[hi]:
                # Rotation point (the minimum) is strictly to the right of mid
                lo = mid + 1
            else:
                # nums[mid] < nums[hi]: right half is sorted, so the minimum
                # is at mid or to its left
                hi = mid

        return nums[lo]