class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        m, M = min(need1, need2), max(need1, need2)
        a = need1 * cost1 + need2 * cost2
        b = m * costBoth + (need1 - m) * cost1 + (need2 - m) * cost2
        c = M * costBoth
        return min(a, b, c)