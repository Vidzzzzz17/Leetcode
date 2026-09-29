class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        m, n = len(grid), len(grid[0])
        
        # A valid path length must be even
        if (m + n - 1) % 2 != 0:
            return False
        
        # Path must start with '(' and end with ')'
        if grid[0][0] == ')' or grid[m - 1][n - 1] == '(':
            return False
        
        # Memoization set: (row, col, balance)
        visited = set()
        
        def dfs(r: int, c: int, balance: int) -> bool:
            # Adjust balance for the current cell
            balance += 1 if grid[r][c] == '(' else -1
            
            # If balance drops below 0, the prefix is invalid
            if balance < 0:
                return False
            
            # If balance exceeds max remaining steps, we can't reach 0 at the end
            remaining_steps = (m - 1 - r) + (n - 1 - c)
            if balance > remaining_steps:
                return False
            
            # Reached destination: check if balance is exactly 0
            if r == m - 1 and c == n - 1:
                return balance == 0
            
            state = (r, c, balance)
            if state in visited:
                return False
            visited.add(state)
            
            # Explore moving right and moving down
            if c + 1 < n and dfs(r, c + 1, balance):
                return True
            if r + 1 < m and dfs(r + 1, c, balance):
                return True
            
            return False

        return dfs(0, 0, 0)