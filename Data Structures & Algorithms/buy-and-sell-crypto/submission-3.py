class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # l'esempio che mi ha fatto sbloccare è [3,4,7,1,9] confrontato con [3,4,7,6,9]
        # nel primo caso quando vedo 1 ho una perdita in acquisto --> salto direttamente lì, perché
        # SE dovesse esserci un prezzo di vendita maggiore, allora c'è un intero intervallo migliore, in
        # quanto anche il prezzo di acquisto è inferiore
        #
        # mentre nel secondo, quando vedo 6, ho una inefficienza di vendita --> continuo a vedere se 
        # esiste un valore di vendita migliore, altrimenti so quale è il massimo che posso fare
        
        left = prices[0] # non un puntatore, in questo caso mi basta direttamente il valore
        max_profit = 0
        for right in prices: 
            profit = right - left
            if profit < 0:
                left = right
            max_profit = max(max_profit, profit)
        return max_profit
        