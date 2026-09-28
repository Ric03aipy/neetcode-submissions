class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # ===============
        # ripetizione #1
        # ===============

        # chi non viene mai rallentata e ci dà un riferimento di velocità (fissa) ? Quella che sta più avanti di tutte
        
        # ordinamento decrescente -> la prima è la più avanti
        info = sorted([(pos, sp) for pos, sp in zip(position, speed)], key=lambda x: -x[0]) 

        # ogni flotta ha un rappresentante: una macchina che non raggiunge mai quelle che stanno avanti a lei, ovvero che impiega un tempo superiore a chi è davanti: un "RE" a cui tutte quelle più veloci ma dietro si sottomettono

        # questo suggerisce l'uso di una stack monotonica, con l'obiettivo di mantenere alla fine un rappresentante per flotta in termini temporali

        # quindi la stack deve essere strettamente crescente in termini di "tempo di arrivo"

        stack: list[float] = []

        for pos, sp in info: 
            time = (target - pos) / sp

            stack.append(time)

            # forzatura della monotonia
            if len(stack) >= 2 and stack[-1] <= stack[-2]: # stack[-1] è time 
                stack.pop()

        return len(stack)