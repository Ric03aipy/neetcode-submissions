class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        gain = 0
        min_price = prices[0]
        # I need to know the current price, and the minimum seen so far (the minimum of the subarray)
        for i in range(n):
            current_gain = prices[i] - min_price
            if prices[i] < min_price: min_price = prices[i]
            if current_gain > gain: gain = current_gain
        return gain


