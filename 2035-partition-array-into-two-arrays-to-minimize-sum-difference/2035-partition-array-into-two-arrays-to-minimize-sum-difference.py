import bisect

class Solution:
    def minimumDifference(self, nums: list[int]) -> int:
        total_sum = sum(nums)
        n = len(nums) // 2
        
        left = nums[:n]
        right = nums[n:]
        
        # Helper function to generate subset sums grouped by size (count)
        def get_subset_sums(arr):
            res = [[] for _ in range(len(arr) + 1)]
            res[0] = [0]
            for x in arr:
                for i in range(len(arr) - 1, -1, -1):
                    for s in res[i]:
                        res[i + 1].append(s + x)
            return res
            
        left_subsets = get_subset_sums(left)
        right_subsets = get_subset_sums(right)
        
        # Sort right subsets for binary search
        for i in range(len(right_subsets)):
            right_subsets[i].sort()
            
        min_diff = float('inf')
        half_total = total_sum / 2
        
        for k in range(n + 1):
            if not left_subsets[k] or not right_subsets[n - k]:
                continue
            r_list = right_subsets[n - k]
            for s_left in left_subsets[k]:
                target = half_total - s_left
                idx = bisect.bisect_left(r_list, target)
                
                if idx < len(r_list):
                    s_right = r_list[idx]
                    current_sum = s_left + s_right
                    min_diff = min(min_diff, abs(total_sum - 2 * current_sum))
                if idx > 0:
                    s_right = r_list[idx - 1]
                    current_sum = s_left + s_right
                    min_diff = min(min_diff, abs(total_sum - 2 * current_sum))
                    
        return min_diff