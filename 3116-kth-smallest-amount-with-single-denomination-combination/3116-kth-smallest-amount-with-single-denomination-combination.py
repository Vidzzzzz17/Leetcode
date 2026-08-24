import math
from typing import List

class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        n = len(coins)
        
        def count_valid(amount: int) -> int:
            """Counts how many values <= amount are divisible by at least one coin using Inclusion-Exclusion."""
            total = 0
            # Enumerate all non-empty subsets via bitmask
            for mask in range(1, 1 << n):
                lcm_val = 1
                bits = 0
                for i in range(n):
                    if (mask >> i) & 1:
                        bits += 1
                        lcm_val = math.lcm(lcm_val, coins[i])
                        # Early exit if LCM exceeds amount
                        if lcm_val > amount:
                            break
                
                if lcm_val <= amount:
                    if bits % 2 == 1:
                        total += amount // lcm_val
                    else:
                        total -= amount // lcm_val
            return total

        # Binary search range
        left = 1
        right = k * min(coins)
        ans = right

        while left <= right:
            mid = (left + right) // 2
            if count_valid(mid) >= k:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1

        return ans