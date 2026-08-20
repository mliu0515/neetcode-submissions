class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 0
        profit = 0
        while r < len(prices):
            curProfit = prices[r] - prices[l]
            if curProfit < 0:
                l = r
            r = r + 1
            profit = max(profit, curProfit)

        return profit