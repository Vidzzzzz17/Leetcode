class Solution:
    def partition(self, s: str) -> list[list[str]]:
        n = len(s)
        is_pal = [[False] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i < 2 or is_pal[i + 1][j - 1]):
                    is_pal[i][j] = True

        res, path = [], []

        def dfs(start: int) -> None:
            if start == n:
                res.append(path[:])
                return
            for end in range(start, n):
                if is_pal[start][end]:
                    path.append(s[start:end + 1])
                    dfs(end + 1)
                    path.pop()

        dfs(0)
        return res