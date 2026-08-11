class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        result = []
        path = []
        
        def backtrack(start):
            if len(path) == k:
                result.append(path[:])
                return
            
            # Pruning: not enough numbers left to reach size k
            remaining_needed = k - len(path)
            for i in range(start, n - remaining_needed + 2):
                path.append(i)
                backtrack(i + 1)
                path.pop()
        
        backtrack(1)
        return result