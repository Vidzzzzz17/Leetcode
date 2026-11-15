class MinStack:

    def __init__(self):
        # Each entry is a pair: (value, minimum of the stack up to and including this value)
        self.stack = []

    def push(self, value: int) -> None:
        current_min = min(value, self.stack[-1][1]) if self.stack else value
        self.stack.append((value, current_min))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]