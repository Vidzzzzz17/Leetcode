class Solution:
    def uniquePaths(self, grid):
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])
        R = [[0] * (n + 1) for _ in range(m + 1)]
        D = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m):
            for j in range(n):
                if i == m - 1 and j == n - 1:
                    break
                if grid[i][j] == 0:
                    total = 1 if (i == 0 and j == 0) else (R[i][j] + D[i][j]) % MOD
                    if total:
                        if j + 1 < n:
                            R[i][j + 1] = (R[i][j + 1] + total) % MOD
                        if i + 1 < m:
                            D[i + 1][j] = (D[i + 1][j] + total) % MOD
                else:
                    # entered moving right -> turned down
                    if R[i][j] and i + 1 < m:
                        D[i + 1][j] = (D[i + 1][j] + R[i][j]) % MOD
                    # entered moving down -> turned right
                    if D[i][j] and j + 1 < n:
                        R[i][j + 1] = (R[i][j + 1] + D[i][j]) % MOD

        return (R[m - 1][n - 1] + D[m - 1][n - 1]) % MOD