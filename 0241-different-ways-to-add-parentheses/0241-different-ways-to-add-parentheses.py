from functools import lru_cache

class Solution:
    def diffWaysToCompute(self, expression: str):
        @lru_cache(maxsize=None)
        def solve(lo, hi):
            res = []
            for i in range(lo, hi):
                c = expression[i]
                if c in '+-*':
                    left = solve(lo, i)
                    right = solve(i + 1, hi)
                    for a in left:
                        for b in right:
                            if c == '+':
                                res.append(a + b)
                            elif c == '-':
                                res.append(a - b)
                            else:
                                res.append(a * b)
            if not res:
                res.append(int(expression[lo:hi]))
            return tuple(res)

        return list(solve(0, len(expression)))