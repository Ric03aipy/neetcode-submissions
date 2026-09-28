class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # I numeri possibili vanno da 1 a n. 
        # La lunghezza dell'array è n + 1.
        low = 1
        high = len(nums) - 1
        
        while low < high:
            mid = low + (high - low) // 2
            
            # Contiamo quanti numeri nell'array sono minori o uguali a 'mid'
            count = 0
            for num in nums:
                if num <= mid:
                    count += 1
                    
            # PRINCIPIO DEI CASSETTI:
            # Se ci sono più di 'mid' numeri che sono <= 'mid', 
            # il duplicato deve per forza trovarsi nella metà inferiore (tra low e mid).
            # Esempio: se mid = 3, e ci sono 4 numeri <= 3... uno di loro è ripetuto!
            if count > mid:
                high = mid
            else:
                # Altrimenti, il duplicato si nasconde nella metà superiore.
                low = mid + 1
                
        # Quando low == high, abbiamo isolato il nostro valore duplicato
        return low