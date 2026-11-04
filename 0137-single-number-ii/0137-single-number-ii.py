from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for bit in range(32):
            count = 0
            for n in nums:
                count += (n >> bit) & 1
            if count % 3:
                result |= 1 << bit
        # interpret as signed 32-bit
        if result >= 1 << 31:
            result -= 1 << 32
        return result