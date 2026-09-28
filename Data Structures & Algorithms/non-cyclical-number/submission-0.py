class Solution:
    def isHappy(self, n: int) -> bool:
        
        seen = set()
        while n not in seen: 

            # Condizione di non cilicità
            if n == 1: return True

            # Aggiungo il numero corrente a quelli visti 
            seen.add(n)

            # Scompongo il numero in cifre
            digits = []
            while n > 0: 
                digits.append(digit := (n % 10))
                n = (n - digit) // 10
            print(digits)

            # Nuovo numero 
            n = 0
            for d in digits:
                n += d * d    

        # Uscito perché già visto 
        return False