class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # Edge case: integer overflow
        MAX_INT = 2**31 - 1
        MIN_INT = -2**31
        
        if dividend == MIN_INT and divisor == -1:
            return MAX_INT
        
        # Determine the sign of the result
        negative = (dividend < 0) ^ (divisor < 0)
        
        # Work with positive values
        a, b = abs(dividend), abs(divisor)
        quotient = 0
        
        # Shift b left to find the largest multiple
        while a >= b:
            temp_b = b
            count = 1
            while a >= (temp_b << 1):
                temp_b <<= 1
                count <<= 1
            
            a -= temp_b
            quotient += count
            
        return -quotient if negative else quotient
        