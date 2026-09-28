class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # ================
        # ripetizione #2
        # ================

        min_speed = 1
        max_speed = max(piles)
        best = max_speed

        while min_speed <= max_speed: 
            # Scegli una velocità
            speed = min_speed + (max_speed - min_speed) // 2

            # La velocità scelta è valida? Se sì, possiamo fare anche meglio (diminuendola)? 
            time = 0
            for pile in piles: time += -(-pile // speed)
            if time <= h: 
                best = speed
                max_speed = speed - 1
            # Se non è valido proviamo ad andare più veloce
            else: 
                min_speed = speed + 1
        
        return best


