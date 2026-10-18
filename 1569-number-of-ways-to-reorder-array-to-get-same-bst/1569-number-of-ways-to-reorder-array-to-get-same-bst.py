from typing import List

class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)

        # Pascal's triangle for binomial coefficients mod p
        C = [[0] * (n + 1) for _ in range(n + 1)]
        for i in range(n + 1):
            C[i][0] = 1
            for j in range(1, i + 1):
                C[i][j] = (C[i - 1][j - 1] + C[i - 1][j]) % MOD

        def ways(arr: List[int]) -> int:
            m = len(arr)
            if m <= 2:
                return 1
            root = arr[0]
            left = [x for x in arr if x < root]
            right = [x for x in arr if x > root]
            return (C[m - 1][len(left)] * ways(left) % MOD) * ways(right) % MOD

        return (ways(nums) - 1) % MOD