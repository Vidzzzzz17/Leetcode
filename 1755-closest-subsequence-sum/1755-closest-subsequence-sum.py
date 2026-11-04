import bisect

class Solution:
    def minAbsDifference(self, nums: list[int], goal: int) -> int:
        n = len(nums)
        mid = n // 2
        
        # Helper function to generate all possible subsequence sums
        def get_sums(arr):
            res = [0]
            for x in arr:
                res += [s + x for s in res]
            return sorted(set(res))
            
        left_sums = get_sums(nums[:mid])
        right_sums = get_sums(nums[mid:])
        
        min_diff = float('inf')
        
        for l in left_sums:
            target = goal - l
            idx = bisect.bisect_left(right_sums, target)
            
            # Check the closest elements around the insertion point
            if idx < len(right_sums):
                min_diff = min(min_diff, abs(l + right_sums[idx] - goal))
            if idx > 0:
                min_diff = min(min_diff, abs(l + right_sums[idx - 1] - goal))
                
        return min_diff