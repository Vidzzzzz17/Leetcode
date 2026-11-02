class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min_price = float("inf")
        best = 0
        for p in prices:
            if p < min_price:
                min_price = p
            else:
                best = max(best, p - min_price)
        return best