class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # ==============
        # ripetizione #2
        # ==============

        # [2,1,5,6,2,3]
        # 
        #        # 
        #      # #
        #      # #
        #      # #   #
        #  #   # # # #
        #  # # # # # #

        """ EFFICIENT ALGORITHM """
    
        max_area = 0
        stack = [] # (indice, altezza)

        for i, h in enumerate(heights): 

            # Stack monotonica crescente
            idx = i
            while stack and h <= stack[-1][1]: 
                # Quando estraggo qualcosa, per far propagare all'indietro l'altezza corrente devo sapere quale è l'indice
                # a cui fermarmi
                idx, old_h = stack.pop()
                # Qundo faccio il pop perdo per sempre questo valore quindi volgio calcolare l'area qui 
                # All'indice corrente la barra più alta non può espandersi 
                area = old_h * (i - idx)
                max_area = max(area, max_area)

            # La PROPAGAZIONE ALL'INDIETRO finisce qui

            # In pila va l'indice non attuale ma il più a sinistra possibile per il valore attuale di altezza
            stack.append((idx, h))
            


        # Qui si fa solo PROPAGAZIONE IN AVANTI
        for idx, h in stack: 
            area = (len(heights) - idx) * h
            max_area = max(area, max_area)
            


        return max_area


        """ BRUTE FORCE """
        """
        max_area = 0 
        # Per ogni barra
        for i, h1 in enumerate(heights): 
            area = heights[i]
            # Quale è il limite vedendo dietro? 
            for j in range(i - 1, -1, -1): 
                if heights[j] >= h1: area += h1
                else: break
            # Quale è il limite vedendo avanti?
            for j in range(i + 1, len(heights)): 
                if heights[j] >= h1: area += h1
                else: break
            max_area = max(area, max_area)
        return max_area
        """