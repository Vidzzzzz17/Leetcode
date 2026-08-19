from collections import defaultdict

class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: list[list[int]]) -> int:
        reserved_rows = defaultdict(int)
        
        for row, col in reservedSeats:
            if 2 <= col <= 9:
                reserved_rows[row] |= (1 << col)
                
        left_mask   = (1 << 2) | (1 << 3) | (1 << 4) | (1 << 5)
        mid_mask    = (1 << 4) | (1 << 5) | (1 << 6) | (1 << 7)
        right_mask  = (1 << 6) | (1 << 7) | (1 << 8) | (1 << 9)
        
        total_groups = 0
        
        for row_mask in reserved_rows.values():
            left_free  = (row_mask & left_mask) == 0
            right_free = (row_mask & right_mask) == 0
            mid_free   = (row_mask & mid_mask) == 0
            
            if left_free and right_free:
                total_groups += 2
            elif left_free or right_free or mid_free:
                total_groups += 1
                
        total_groups += (n - len(reserved_rows)) * 2
        return total_groups