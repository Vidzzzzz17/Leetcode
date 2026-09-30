class Solution:
    def grayCode(self, n: int) -> list[int]:
        # Generate 2^n elements where G(i) = i ^ (i >> 1)
        return [i ^ (i >> 1) for i in range(1 << n)]