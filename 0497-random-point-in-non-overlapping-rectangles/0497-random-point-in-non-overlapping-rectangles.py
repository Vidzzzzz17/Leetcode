import random
import bisect

class Solution:
    def __init__(self, rects):
        self.rects = rects
        self.prefix = []
        total = 0
        for a, b, x, y in rects:
            total += (x - a + 1) * (y - b + 1)
            self.prefix.append(total)
        self.total = total

    def pick(self):
        r = random.randint(1, self.total)
        i = bisect.bisect_left(self.prefix, r)
        a, b, x, y = self.rects[i]
        return [random.randint(a, x), random.randint(b, y)]