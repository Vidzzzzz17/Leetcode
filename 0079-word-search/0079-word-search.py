class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        
        def backtrack(r, c, idx):
            if idx == len(word):
                return True
            if r < 0 or r >= m or c < 0 or c >= n or board[r][c] != word[idx]:
                return False
            
            temp = board[r][c]
            board[r][c] = '#'  # mark as visited
            
            found = (backtrack(r + 1, c, idx + 1) or
                     backtrack(r - 1, c, idx + 1) or
                     backtrack(r, c + 1, idx + 1) or
                     backtrack(r, c - 1, idx + 1))
            
            board[r][c] = temp  # restore
            return found
        
        for i in range(m):
            for j in range(n):
                if backtrack(i, j, 0):
                    return True
        
        return False