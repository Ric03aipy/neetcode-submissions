class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # trivial solution O(n^2)
        max_profit = 0
        i = 0 
        for i, buy in enumerate(prices):
            for j in range(i+1, len(prices)):
                profit = prices[j] - buy
                max_profit = max(max_profit, profit)
        return max_profit
        


