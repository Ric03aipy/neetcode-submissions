class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # ==========================
        # ripetizione #2
        # ==========================

        win = {}
        left = 0 
        max_freq = 0
        max_len = 0

        for right in range(len(s)): 
        
            # --- finestra mobile dinamica --- 

            # estendo a destra
            win[s[right]] = win.get(s[right], 0) + 1
            max_freq = max(max_freq, win[s[right]])
            
            # se sgarro stringo a sinistra (il carattere più frequente è quello che NON voglio sostituire)
            while (right - left + 1) - max_freq > k:
                win[s[left]] -= 1
                left += 1

            # qui la finestra è sicuramente valida 
            winlen = right - left + 1
            max_len = max(max_len, winlen)

        return max_len
