class Solution:
    def trap(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1
        max_l = height[i]
        max_r = height[j]

        max_water = 0
        while i < j:
            if max_l < max_r:
                # Il collo di bottiglia è a SINISTRA. Lavoriamo su 'i'.
                # 1. Muovi il puntatore sinistro avanti (i += 1)
                # 2. Aggiorna max_l se la nuova colonna è più alta
                # 3. Calcola l'acqua per la nuova colonna 'i' (max_l - height[i]) e aggiungila al totale
                i += 1
                max_l = max(max_l, height[i])
                water = max_l - height[i]
            else:
                # Il collo di bottiglia è a DESTRA. Lavoriamo su 'j'.
                # 1. Muovi il puntatore destro indietro (j -= 1)
                # 2. Aggiorna max_r se la nuova colonna è più alta
                # 3. Calcola l'acqua per la nuova colonna 'j' (max_r - height[j]) e aggiungila al totale
                j -= 1
                max_r = max(max_r, height[j])
                water = max_r - height[j]

            max_water += water
            
        return max_water



            