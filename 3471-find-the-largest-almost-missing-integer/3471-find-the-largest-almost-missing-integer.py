class Solution:

  def largestInteger(self, nums: list[int], k: int) -> int:
    from collections import Counter, defaultdict

    n = len(nums)
    subarray_counts = defaultdict(set)

    # Count how many distinct subarrays of size k contain each element
    for i in range(n - k + 1):
      subarray = nums[i : i + k]
      for num in set(subarray):
        subarray_counts[num].add(i)

    # Filter elements that appear in exactly 1 subarray
    candidates = [
        num for num, indices in subarray_counts.items() if len(indices) == 1
    ]

    return max(candidates) if candidates else -1
    