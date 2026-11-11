from math import gcd
from collections import defaultdict
from typing import List

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n <= 2:
            return n

        best = 2
        for i in range(n):
            xi, yi = points[i]
            slopes = defaultdict(int)
            for j in range(i + 1, n):
                dx = points[j][0] - xi
                dy = points[j][1] - yi
                g = gcd(dx, dy)  # always positive here since points are unique
                dx //= g
                dy //= g
                if dx < 0 or (dx == 0 and dy < 0):
                    dx, dy = -dx, -dy
                slopes[(dx, dy)] += 1
            if slopes:
                best = max(best, max(slopes.values()) + 1)
        return best
              