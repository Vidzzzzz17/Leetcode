class Solution:
    def restoreIpAddresses(self, s: str):
        n = len(s)
        if n < 4 or n > 12:
            return []

        res = []
        path = []

        def backtrack(start: int):
            segs_left = 4 - len(path)
            remaining = n - start

            # Prune: remaining digits must fit in the remaining segments
            if remaining < segs_left or remaining > 3 * segs_left:
                return

            if segs_left == 0:
                res.append(".".join(path))
                return

            for length in range(1, 4):
                if start + length > n:
                    break
                seg = s[start:start + length]
                if len(seg) > 1 and seg[0] == '0':
                    break  # leading zero: longer segments also invalid
                if int(seg) > 255:
                    break
                path.append(seg)
                backtrack(start + length)
                path.pop()

        backtrack(0)
        return res