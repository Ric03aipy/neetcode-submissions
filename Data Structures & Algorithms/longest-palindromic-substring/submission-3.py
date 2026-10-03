class Solution:
    def longestPalindrome(self, s: str) -> str:
    
        def wave_propagation(left, right): 
            # Propago i due puntatori a sinistra e a destra della stessa quantità 
            while left >= 0 and right < len(s) and s[left] == s[right]: 
                left -= 1 
                right += 1 
            # Ritorno il valore prima che la condizione si rompesse
            return left + 1, right - 1

        res_left, res_right = 0, 0
        max_dist = 0
        for i in range(len(s)):
            # Espando assumendo che sia un centro dispari
            odd_left, odd_right = wave_propagation(i, i)
            # Espando assumendo che sia un centro pari
            even_left, even_right = wave_propagation(i, i + 1)
            
            for curr_left, curr_right in ((odd_left, odd_right), (even_left, even_right)): 
                if curr_right - curr_left + 1 > max_dist: 
                    max_dist = curr_right - curr_left + 1
                    res_left, res_right = curr_left, curr_right

        return s[res_left:res_right + 1]
            
            



