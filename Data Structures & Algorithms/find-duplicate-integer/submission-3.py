class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Floyd's Cycle Detection
        # Array come lista: nums[x] è un puntatore, ovvero se nums[x] = 2 allora l'indice al prossimo giro è 2
        # Prima trovi il primo punto di intersezione dei puntatori slow & fast.
        # Il risultato teorico è: "la distanza dall'intersezione e l'inizio del ciclo è la stessa distanza tra l'inizio della 
        # lista e l'inizio del ciclo".

        slow, fast = 0, 0
        # Dato che rappresentano indici controllo quando puntano allo stesso oggetto (incrocio)
        while True: 
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast: break # non posso fare while slow != fast perché con (0,0) iniziale non partirebbe
        
        # Qui slow == fast, ma fast non ci serve più
        slow2 = 0
        while True: 
            slow2 = nums[slow2]
            slow = nums[slow]
            if slow == slow2: break # //
        
        return slow2 # ritorno l'indice 