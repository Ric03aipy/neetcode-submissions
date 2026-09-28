class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""
        
        # 1. Crea t_freq SOLO con le lettere di t
        t_freq = {}
        for c in t: t_freq[c] = t_freq.get(c, 0) + 1
        
        win = {} # conterrà solo le lettere utili che incontriamo
        have = 0 # quante condizioni uniche (numero di elementi) soddisfatte
        need = len(t_freq) # numero di condizioni uniche da soddisfare
        
        res = [-1, -1] # [inizio, fine] della migliore finestra trovata
        res_len = float("inf")
        
        left = 0
        for right in range(len(s)):
            c = s[right]
            # 2. Se 'c' è in t_freq, lo aggiungi a 'window'
            # 3. Se window[c] == t_freq[c], allora have += 1
            if c in t_freq: 
                win[c] = win.get(c, 0) + 1
                if win[c] == t_freq[c]: 
                    have += 1
            # 4. RESTRINGI: finché la finestra è valida
            while have == need:
                # 4a. Se l'attuale finestra è più piccola di res_len, aggiorna res e res_len
                curr_len = right - left + 1
                if curr_len < res_len: 
                    res = [left, right]
                    res_len = curr_len
                # 4b. Rimuovi s[left] da 'window'
                # 4c. Se s[left] era utile e ora window[s[left]] < t_freq[s[left]], fai have -= 1
                # 4d. left += 1
                if s[left] in win:
                    win[s[left]] -= 1
                if s[left] in t_freq and win[s[left]] < t_freq[s[left]]:
                    have -= 1
                left += 1
                
        # Alla fine, se res_len è ancora infinito, ritorna ""
        # Altrimenti ritorna s[res[0]:res[1]+1]

        if res_len == float('inf'): return ""
        return s[res[0]: res[1]+1]

