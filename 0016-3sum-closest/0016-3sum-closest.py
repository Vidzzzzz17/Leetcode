class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        closest_sum = nums[0] + nums[1] + nums[2]  # initialize with first triplet
        
        for i in range(n - 2):
            # Skip duplicate values for the first element (optimization, not required for correctness)
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            left, right = i + 1, n - 1
            
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                
                # Update closest_sum if this one is nearer to target
                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum
                
                if current_sum == target:
                    return current_sum  # can't get any closer than exact match
                elif current_sum < target:
                    left += 1
                else:
                    right -= 1
        
        return closest_sum
        