import random

class Solution:
    def __init__(self, m, n):
        self.m, self.n = m, n
        self.total = m * n
        self.remaining = self.total
        self.swap = {}

    def flip(self):
        r = random.randint(0, self.remaining - 1)
        self.remaining -= 1
        idx = self.swap.get(r, r)
        self.swap[r] = self.swap.get(self.remaining, self.remaining)
        return [idx // self.n, idx % self.n]

    def reset(self):
        self.remaining = self.total
        self.swap.clear()