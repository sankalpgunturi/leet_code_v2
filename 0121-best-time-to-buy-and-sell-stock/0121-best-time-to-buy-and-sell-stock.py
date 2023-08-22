class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0

        l, r = 0, 1
        profit = 0

        while l < r and l < len(prices) and r < len(prices):
            profit = max(profit, prices[r] - prices[l])
            print(l, r)
            if prices[r] < prices[l]:
                l = r
                r += 1
            else:
                r += 1
        return profit
