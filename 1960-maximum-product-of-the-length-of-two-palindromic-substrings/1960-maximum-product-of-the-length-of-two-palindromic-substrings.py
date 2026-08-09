class Solution:
    def maxProduct(self, s: str) -> int:
        n = len(s)
        if n < 2:
            return 0
        
        # Manacher's algorithm for odd-length palindromes
        p = [1] * n
        l, r = 0, -1
        for i in range(n):
            k = 1 if i > r else min(p[l + r - i], r - i + 1)
            while i - k >= 0 and i + k < n and s[i - k] == s[i + k]:
                k += 1
            p[i] = k
            if i + k - 1 > r:
                l = i - k + 1
                r = i + k - 1
        
        # minC[j]: smallest center c whose palindrome can be truncated to end exactly at j
        minC = [0] * n
        pointer = 0
        for c in range(n):
            reach = c + p[c] - 1
            if reach < pointer:
                continue
            start_paint = max(c, pointer)
            for e in range(start_paint, reach + 1):
                minC[e] = c
            pointer = reach + 1
            if pointer >= n:
                break
        
        preMax = [0] * n
        best = 0
        for j in range(n):
            ramp = 2 * (j - minC[j]) + 1
            best = max(best, ramp)
            preMax[j] = best
        
        # Mirror: maxC[j] = largest center whose palindrome can be truncated to start exactly at j
        maxC = [0] * n
        pointer = n - 1
        for c in range(n - 1, -1, -1):
            reach = c - p[c] + 1
            if reach > pointer:
                continue
            start_paint = min(c, pointer)
            for st in range(reach, start_paint + 1):
                maxC[st] = c
            pointer = reach - 1
            if pointer < 0:
                break
        
        sufMax = [0] * n
        best = 0
        for j in range(n - 1, -1, -1):
            ramp = 2 * (maxC[j] - j) + 1
            best = max(best, ramp)
            sufMax[j] = best
        
        ans = 0
        for i in range(n - 1):
            ans = max(ans, preMax[i] * sufMax[i + 1])
        return ans