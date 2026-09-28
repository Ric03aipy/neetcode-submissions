class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0    # puntatore
        max_len = 0 # risultato
        window = {} # stato
        for right in range(len(s)):
            # aggiorno lo stato 
            window[s[right]] = window.get(s[right], 0) + 1
            # info per verificare la condizione
            max_freq = max(window.values())
            win_len = right - left + 1  # [] QUI potrebbe essere valida o no...
            # while **condizione_non_valida**(stato)
            while win_len - max_freq > k: 
                # aggiorno lo stato 
                window[s[left]] -= 1 # non serve rimuoverlo perché al minimo può diventare 0
                # aggiorno il puntatore
                left += 1
                # aggiorno la variabile di loop
                win_len = right - left + 1
            # ... [] QUI è sicuramente valida
            max_len = max(max_len, right - left + 1)
        return max_len