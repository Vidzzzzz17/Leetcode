class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        
        for char in s:
            if char == ')':
                # Collect characters inside the current pair of parentheses
                temp = []
                while stack and stack[-1] != '(':
                    temp.append(stack.pop())
                
                # Remove the matching opening parenthesis '('
                if stack:
                    stack.pop()
                
                # Push the reversed characters back to the stack
                stack.extend(temp)
            else:
                stack.append(char)
                
        return "".join(stack)
        