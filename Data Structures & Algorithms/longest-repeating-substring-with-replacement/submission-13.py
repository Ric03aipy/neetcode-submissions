class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        # =======================
        # ripetizione #3
        # =======================

        # Frequenze dei caratteri nella finestra
        # m = numero di caratteri unici è al più 26
        # O(m) è una versione ottimizzata di O(26) in memoria
        # Ma ciclare su un O(m) limitata da una costante significa ciclare con costo unitario in tempo O(1)
        freq = {}
        max_freq = 0
        max_len = 0
        left = 0 
        for right, c in enumerate(s): 
            
            # Leggo un nuovo carattere e controllo se è una nuova massima frequenza
            freq[c] = freq.get(c, 0) + 1
            max_freq = max(max_freq, freq[c])

            # Se nella finestra ci sono più di k caratteri oltre il carattere più frequente allora la finestra è invalida
            while (right - left + 1) - max_freq > k: 
                freq[s[left]] -= 1
                left += 1

            # Qui sono sicuro che la finestra sia valida
            max_len = max(max_len, right - left + 1)
        
        return max_len




        """
        # ==========================
        # ripetizione #2 - prima volta che viene in maniera abbastanza tranquilla
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

        """