class Solution:

  def longestSubsequence(self, nums: list[int]) -> int:
    total_xor = 0
    has_non_zero = False

    for num in nums:
      total_xor ^= num
      if num != 0:
        has_non_zero = True

    # Case 1: All elements are 0
    if not has_non_zero:
      return 0

    # Case 2: Total XOR is non-zero
    if total_xor != 0:
      return len(nums)

    # Case 3: Total XOR is 0, but non-zero elements exist
    return len(nums) - 1