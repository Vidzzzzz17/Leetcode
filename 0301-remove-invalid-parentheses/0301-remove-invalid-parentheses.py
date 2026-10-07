from typing import List

class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        left_rem = right_rem = 0
        for ch in s:
            if ch == '(':
                left_rem += 1
            elif ch == ')':
                if left_rem == 0:
                    right_rem += 1
                else:
                    left_rem -= 1

        res = set()
        path = []
        n = len(s)

        def dfs(i, l, r, open_cnt, close_cnt):
            if i == n:
                if l == 0 and r == 0:
                    res.add("".join(path))
                return

            ch = s[i]

            # Remove current char
            if ch == '(' and l > 0:
                dfs(i + 1, l - 1, r, open_cnt, close_cnt)
            elif ch == ')' and r > 0:
                dfs(i + 1, l, r - 1, open_cnt, close_cnt)

            # Keep current char
            path.append(ch)
            if ch == '(':
                dfs(i + 1, l, r, open_cnt + 1, close_cnt)
            elif ch == ')':
                if close_cnt < open_cnt:
                    dfs(i + 1, l, r, open_cnt, close_cnt + 1)
            else:
                dfs(i + 1, l, r, open_cnt, close_cnt)
            path.pop()

        dfs(0, left_rem, right_rem, 0, 0)
        return list(res)