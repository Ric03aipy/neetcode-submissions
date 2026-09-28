class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # ======================
        # ripetizione #2
        # ======================

        res = "" # risultato da ritornare
        minlen = float('inf')

        # caratteri nel numero esatto che mi servono
        t_freq = {} 
        for c in t: t_freq[c] = t_freq.get(c, 0) + 1

        have = 0 # caratteri unici di cui ho raggiunto la giusta frequenza
        need = len(t_freq.keys()) # caratteri unici richiesti

        win = {} # caratteri osservati

        left = 0
        for right in range(len(s)): 

            win[s[right]] = win.get(s[right], 0) + 1
            if s[right] in t_freq and win[s[right]] == t_freq[s[right]]: have += 1

            # forzo la finestra a essere minima
            # while valida: riduco; poiché sono sicuro che qui dentro è valida, calcolo il risultato di volta in volta; 
            # calcolo il risutlato prima di aggiornare left perché non so se post aggiornamento la validità resta
            while have == need: 
                if right-left+1 < minlen: 
                    res = s[left:right+1]
                    minlen = right-left+1
                win[s[left]] -= 1
                if s[left] in t_freq and win[s[left]] < t_freq[s[left]]: have -= 1
                left += 1
            
        return res


            
