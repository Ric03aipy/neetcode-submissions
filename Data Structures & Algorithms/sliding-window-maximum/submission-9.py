class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # ===============
        # ripetizione #3
        # ===============

        from collections import deque

        # qui ci metto gli indici, che rappresentano la scadenza degli elementi ;
        # struttura monotonica decrescente: via tutti gli elementi che non hanno speranza di essere massimi in una finestra
        candidates_for_max = deque()

        # a ogni turno faccio un inserimento qui
        maxs = []

        for right in range(len(nums)): 
            # nums[right] indica il valore che entra a ogni giro

            left = right - k + 1 # right = 3, k = 3 -> left = ? deve essere 1 in modo da selezionare indici [1,2,3] 

            # elimino un elemento se non è più valido: potrebbe trovarsi un elemento valido per ancora qualche turno 
            # a causa del ciclo che forza la monotonia
            if candidates_for_max and left > candidates_for_max[0]: candidates_for_max.popleft()

            # forzo la monotonia decrescente 
            while candidates_for_max and nums[right] > nums[candidates_for_max[-1]]: candidates_for_max.pop()
            
            # aggiungo il nuovo elemento
            candidates_for_max.append(right)

            # ottengo il massimo di questa finestra: attenzione alle prime iterazioni, solo quando right supera il minimo
            if left >= 0: maxs.append(nums[candidates_for_max[0]])

        return maxs