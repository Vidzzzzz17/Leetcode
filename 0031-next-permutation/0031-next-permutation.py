class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        n = len(nums)
        
        # Step 1: find the rightmost index i such that nums[i] < nums[i + 1]
        i = n - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        
        # Step 2: if such an index exists, find the rightmost element greater than nums[i]
        # and swap them
        if i >= 0:
            j = n - 1
            while nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        
        # Step 3: reverse the suffix starting at i + 1
        # (if i == -1, this reverses the entire array, giving the lowest permutation)
        left, right = i + 1, n - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1