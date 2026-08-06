class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        def digit_product(num: int) -> int:
            product = 1
            for digit in str(num):
                product *= int(digit)
            return product
        
        candidate = n
        while digit_product(candidate) % t != 0:
            candidate += 1
        
        return candidate   