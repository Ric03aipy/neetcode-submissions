class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # ===================
        # ripetizione #2
        # ===================

        # Caso base: nessuna transizione
        if len(prices) < 2: return 0

        max_profit = 0
        buy, sell = prices[0], prices[1]
        for price in prices: 
            sell = max(sell, price)
            max_profit = max(max_profit, sell - buy)
            if price < buy: 
                sell = 0
                buy = price
        
        return max_profit