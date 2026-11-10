class Solution:
    def longestDupSubstring(self, s: str) -> str:
        n = len(s)
        nums = [ord(c) - 97 for c in s]
        base = 26
        mod = (1 << 61) - 1

        def search(L):
            """Return start index of a duplicate substring of length L, or -1."""
            h = 0
            for i in range(L):
                h = (h * base + nums[i]) % mod
            seen = {h: [0]}
            power = pow(base, L, mod)
            for i in range(1, n - L + 1):
                h = (h * base - nums[i - 1] * power + nums[i + L - 1]) % mod
                if h in seen:
                    sub = s[i:i + L]
                    for j in seen[h]:
                        if s[j:j + L] == sub:
                            return i
                    seen[h].append(i)
                else:
                    seen[h] = [i]
            return -1

        lo, hi = 1, n - 1
        start, best = -1, 0
        while lo <= hi:
            mid = (lo + hi) // 2
            idx = search(mid)
            if idx != -1:
                start, best = idx, mid
                lo = mid + 1
            else:
                hi = mid - 1

        return s[start:start + best] if start != -1 else ""