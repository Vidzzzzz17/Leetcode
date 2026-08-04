class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]  # base marker for calculating lengths
        max_len = 0
        
        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            else:  # char == ')'
                stack.pop()
                if not stack:
                    # no matching '(' available -> this ')' becomes the new base
                    stack.append(i)
                else:
                    # valid substring found; length = current index - new top
                    max_len = max(max_len, i - stack[-1])
        
        return max_len