class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        result = []
        
        def backtrack(current_str, open_count, close_count):
            # Base Case: complete combination found
            if len(current_str) == 2 * n:
                result.append(current_str)
                return
            
            # Can we add an open parenthesis?
            if open_count < n:
                backtrack(current_str + "(", open_count + 1, close_count)
                
            # Can we add a close parenthesis?
            if close_count < open_count:
                backtrack(current_str + ")", open_count, close_count + 1)
                
        backtrack("", 0, 0)
        return result