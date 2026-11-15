class Solution:
    def findMin(self, nums: list[int]) -> int:
        lo, hi = 0, len(nums) - 1

        while lo < hi:
            mid = (lo + hi) // 2

            if nums[mid] > nums[hi]:
                # Minimum is strictly to the right of mid
                lo = mid + 1
            elif nums[mid] < nums[hi]:
                # mid could be the minimum, so keep it
                hi = mid
            else:
                # nums[mid] == nums[hi]: can't tell which side holds the minimum,
                # but nums[hi] is safe to discard because nums[mid] is an equal copy
                hi -= 1

        return nums[lo]