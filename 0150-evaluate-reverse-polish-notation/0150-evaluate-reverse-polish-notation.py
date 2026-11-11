from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t == '+':
                b, a = stack.pop(), stack.pop()
                stack.append(a + b)
            elif t == '-':
                b, a = stack.pop(), stack.pop()
                stack.append(a - b)
            elif t == '*':
                b, a = stack.pop(), stack.pop()
                stack.append(a * b)
            elif t == '/':
                b, a = stack.pop(), stack.pop()
                stack.append(int(a / b))  # truncate toward zero
            else:
                stack.append(int(t))
        return stack[0]