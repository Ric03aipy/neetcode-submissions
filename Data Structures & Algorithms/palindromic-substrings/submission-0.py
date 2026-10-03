class Solution:
    def countSubstrings(self, s: str) -> int:
        
        def wave_propagation(left, right): 
            local_count = 0
            # Propago i due puntatori a sinistra e a destra della stessa quantità 
            while left >= 0 and right < len(s) and s[left] == s[right]: 
                left -= 1 
                right += 1 
                local_count += 1
            # Ritorno il valore prima che la condizione si rompesse
            return local_count 

        global_count = 0
        for i in range(len(s)):
            # Espando assumendo che sia un centro dispari
            odd_count = wave_propagation(i, i)
            # Espando assumendo che sia un centro pari
            even_count = wave_propagation(i, i + 1)
            global_count = global_count + odd_count + even_count
            
        return global_count
            