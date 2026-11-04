class Solution:
    def minKBitFlips(self, nums: list[int], k: int) -> int:
        n = len(nums)
        flipped = [0] * n
        valid_flips = 0
        ans = 0
        
        for i in range(n):
            # Remove the effect of a flip that is now out of the window [i - k + 1, i]
            if i >= k:
                valid_flips ^= flipped[i - k]
            
            # Check if the current bit is effectively 0
            # nums[i] ^ valid_flips tells us the current state after previous overlapping flips
            if nums[i] ^ valid_flips == 0:
                # If we need a flip but there aren't enough elements left, it's impossible
                if i + k > n:
                    return -1
                
                flipped[i] = 1
                valid_flips ^= 1
                ans += 1
                
        return ans