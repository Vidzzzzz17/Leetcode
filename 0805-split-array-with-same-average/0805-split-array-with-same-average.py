from collections import defaultdict

class Solution:
    def splitArraySameAverage(self, nums: list[int]) -> bool:
        n = len(nums)
        if n == 1:
            return False
            
        total_sum = sum(nums)
        
        # Transform each element: x -> x * n - total_sum
        transformed = [x * n - total_sum for x in nums]
        
        m = n // 2
        left = transformed[:m]
        right = transformed[m:]
        
        # Helper to generate all subset sums grouped by subset size (count)
        def get_subsets(arr):
            res = defaultdict(list)
            k = len(arr)
            for i in range(1 << k):
                s = 0
                cnt = 0
                for j in range(k):
                    if (i >> j) & 1:
                        s += arr[j]
                        cnt += 1
                res[cnt].append(s)
            return res
            
        left_subsets = get_subsets(left)
        right_subsets = get_subsets(right)
        
        # Check if any subset entirely in left or right sums to 0 with valid size
        for cnt, sums in left_subsets.items():
            if cnt == 0:
                continue
            for s in sums:
                if s == 0 and cnt < n:
                    return True
                    
        for cnt, sums in right_subsets.items():
            if cnt == 0:
                continue
            for s in sums:
                if s == 0 and cnt < n:
                    return True
                    
        # Store left subset sums in sets keyed by their subset count for O(1) lookup
        left_sets = {cnt: set(sums) for cnt, sums in left_subsets.items()}
        
        # Combine left and right subsets
        for r_cnt, r_sums in right_subsets.items():
            for s2 in r_sums:
                target = -s2
                # Valid total count c1 + r_cnt must be between 1 and n - 1
                min_c1 = max(0, 1 - r_cnt)
                max_c1 = min(len(left), n - 1 - r_cnt)
                for c1 in range(min_c1, max_c1 + 1):
                    if c1 in left_sets and target in left_sets[c1]:
                        return True
                        
        return False