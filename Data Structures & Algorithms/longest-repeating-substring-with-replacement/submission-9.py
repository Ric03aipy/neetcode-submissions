class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # ==========================
        # ripetizione #1
        # ==========================
        
        left = 0        # puntatore
        max_len = 0     # risultato
        win = {}        # stato

        max_freq = 0    # ausiliaria

        for right in range(len(s)): 
            
            # aggiorna lo stato
            win[s[right]] = win.get(s[right], 0) + 1
            max_freq = max(max_freq, win[s[right]])

            # finché la condizione è valida restringi; quale è la condizione? 
            # "(lunghezza della finestra - massima frequenza) > k" rompe il limite dei k
            while right - left + 1 - max_freq > k: 
                win[s[left]] -= 1
                left += 1

            # la finestra qui è sicuramente valida, quindi possiamo aggiornare il risultato
            max_len = max(max_len, right - left + 1)
        
        return max_len

            