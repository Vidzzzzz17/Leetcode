from typing import List

class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        def count_islands() -> int:
            seen = [[False] * n for _ in range(m)]
            islands = 0
            for i in range(m):
                for j in range(n):
                    if grid[i][j] == 1 and not seen[i][j]:
                        islands += 1
                        seen[i][j] = True
                        stack = [(i, j)]
                        while stack:
                            x, y = stack.pop()
                            for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                                nx, ny = x + dx, y + dy
                                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1 and not seen[nx][ny]:
                                    seen[nx][ny] = True
                                    stack.append((nx, ny))
            return islands

        if count_islands() != 1:
            return 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    islands = count_islands()
                    grid[i][j] = 1
                    if islands != 1:
                        return 1

        return 2