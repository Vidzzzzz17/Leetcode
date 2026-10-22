class Solution:
    def minOperations(self, nums):
        n = len(nums)
        k = nums[0]
        best = float('inf')

        # Case A: rotation of the sorted array, nums[i] = (k + i) % n
        if all(nums[i] == (k + i) % n for i in range(n)):
            best = 0 if k == 0 else min(n - k, k + 2)

        # Case B: rotation of the reversed sorted array, nums[i] = (k - i) % n
        if all(nums[i] == (k - i) % n for i in range(n)):
            a = (k + 1) % n          # rotate left a times, then reverse
            b = (n - k - 1) % n      # reverse, then rotate left b times
            best = min(best, min(a, b) + 1)

        return -1 if best == float('inf') else best