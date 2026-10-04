class Solution:
    def checkValidString(self, s: str) -> bool:
        lo = hi = 0
        for c in s:
            if c == '(':
                lo += 1
                hi += 1
            elif c == ')':
                lo -= 1
                hi -= 1
            else:  # '*'
                lo -= 1
                hi += 1
            if hi < 0:          # too many ')' even using all '*' as '('
                return False
            lo = max(lo, 0)     # '*' can act as empty, so lo never goes below 0
        return lo == 0    