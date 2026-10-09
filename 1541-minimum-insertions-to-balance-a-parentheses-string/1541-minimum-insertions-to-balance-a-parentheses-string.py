class Solution:
    def minInsertions(self, s: str) -> int:
        ans = 0
        need = 0  # right parentheses still needed
        for c in s:
            if c == '(':
                if need % 2 == 1:      # previous '(' has only one ')'
                    ans += 1
                    need -= 1
                need += 2
            else:
                need -= 1
                if need < 0:           # unmatched ')', insert a '('
                    ans += 1
                    need = 1
        return ans + need