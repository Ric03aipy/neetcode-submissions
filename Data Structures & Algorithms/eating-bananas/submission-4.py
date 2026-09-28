class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # ================
        # ripetizione #1
        # ================

        left, right = 1, max(piles) # numero minimo e massimo di banana da mangiare all'ora
        best_h = -1   # k del testo
        while left <= right: 
            mid = left + (right - left) // 2 # candidato k

            # il candidato può soddisfare la richiesta e allora cerchiamo di ottimizzare oppure no e cerchiamo di soddisfare
            # la soddisfacibilità si vede chiedendosi se il numero di ore impiegate 'hours' è <= alla richiesta 'h' 
            hours = 0
            for p in piles: hours += (-(-p // mid)) # ceil() trick 

            if hours <= h: # soddisfatto 
                best_h = mid
                right = mid - 1
            else: # non soddisfatto
                left = mid + 1
            
        return best_h



