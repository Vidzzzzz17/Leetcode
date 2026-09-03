class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        min_val = min(nums1)
        
        # If the smallest element is odd, we can turn all even numbers into odd numbers
        if min_val % 2 != 0:
            return True
        
        # If the minimum element is even, we can only succeed if all numbers are already even
        return all(x % 2 == 0 for x in nums1)      