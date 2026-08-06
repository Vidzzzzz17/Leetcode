class Solution:
    def generateMatrix(self, n: int) -> list[list[int]]:
        # Initialize an n x n matrix filled with zeros
        matrix = [[0] * n for _ in range(n)]
        
        top, bottom = 0, n - 1
        left, right = 0, n - 1
        num = 1
        
        while num <= n * n:
            # 1. Fill top row (left to right)
            for col in range(left, right + 1):
                matrix[top][col] = num
                num += 1
            top += 1
            
            # 2. Fill right column (top to bottom)
            for row in range(top, bottom + 1):
                matrix[row][right] = num
                num += 1
            right -= 1
            
            # 3. Fill bottom row (right to left)
            for col in range(right, left - 1, -1):
                matrix[bottom][col] = num
                num += 1
            bottom -= 1
            
            # 4. Fill left column (bottom to top)
            for row in range(bottom, top - 1, -1):
                matrix[row][left] = num
                num += 1
            left += 1
            
        return matrix