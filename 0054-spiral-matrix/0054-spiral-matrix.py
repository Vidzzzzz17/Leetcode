class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        if not matrix:
            return []
        
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1
        result = []
        
        while left <= right and top <= bottom:
            # 1. Move left to right
            for col in range(left, right + 1):
                result.append(matrix[top][col])
            top += 1
            
            # 2. Move top to bottom
            for row in range(top, bottom + 1):
                result.append(matrix[row][right])
            right -= 1
            
            # 3. Move right to left (if remaining row exists)
            if top <= bottom:
                for col in range(right, left - 1, -1):
                    result.append(matrix[bottom][col])
                bottom -= 1
            
            # 4. Move bottom to top (if remaining column exists)
            if left <= right:
                for row in range(bottom, top - 1, -1):
                    result.append(matrix[row][left])
                left += 1
                
        return result