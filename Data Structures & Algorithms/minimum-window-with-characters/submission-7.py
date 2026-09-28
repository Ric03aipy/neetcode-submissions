class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # ======================
        # ripetizione #3
        # ======================

        if len(t) > len(s): return ""

        t_freq = {}
        for char in t: t_freq[char] = t_freq.get(char, 0) + 1

        min_win_left, min_win_right = 0, -1

        chars_to_satisfy = len(t_freq)
        chars_satisfied = 0

        left = 0
        curr_win = {}
        minlen = float('inf')
        for right, char in enumerate(s): 

            # Estendo la finestra corrente
            curr_win[char] = curr_win.get(char, 0) + 1

            # Quando diveta ">" non mi importa. Ma devo contarlo una volta sola, quando diventa uguale 
            if char in t_freq and curr_win[char] == t_freq[char]: chars_satisfied += 1

            # Accorcio se posso
            while chars_satisfied == chars_to_satisfy:
                
                char_to_drop = s[left]

                # Qui la finestra è valida con certezza -> comparazione per risultato minimo
                if right - left + 1 < minlen: 
                    minlen = right - left + 1
                    min_win_left = left
                    min_win_right = right
                
                curr_win[char_to_drop] -= 1
                left += 1
                
                if char_to_drop in t_freq and curr_win[char_to_drop] < t_freq[char_to_drop]: chars_satisfied -= 1
    

        return s[min_win_left: min_win_right + 1]


                    
            

