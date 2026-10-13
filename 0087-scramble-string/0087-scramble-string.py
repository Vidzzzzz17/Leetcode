from functools import lru_cache
from collections import Counter

class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        n = len(s1)
        if n != len(s2):
            return False

        @lru_cache(maxsize=None)
        def f(i: int, j: int, length: int) -> bool:
            a = s1[i:i + length]
            b = s2[j:j + length]
            if a == b:
                return True
            if Counter(a) != Counter(b):
                return False

            for k in range(1, length):
                # No swap: first k chars match first k chars
                if f(i, j, k) and f(i + k, j + k, length - k):
                    return True
                # Swap: first k chars of s1 match last k chars of s2
                if f(i, j + length - k, k) and f(i + k, j, length - k):
                    return True
            return False

        return f(0, 0, n)