class Solution:
    def canJump(self, nums: list[int]) -> bool:
        max_reachable = 0
        
        for i, jump in enumerate(nums):
            # If the current index is beyond our max reachable position, we can't proceed
            if i > max_reachable:
                return False
            
            # Update the furthest index we can reach
            max_reachable = max(max_reachable, i + jump)
            
            # Optimization: If we can reach or pass the last index, return True early
            if max_reachable >= len(nums) - 1:
                return True
                
        return True