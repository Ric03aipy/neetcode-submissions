class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        # Ordiniamo al contrario (da quella più vicina al target a quella più lontana)
        infos = sorted([(pos, sp) for pos, sp in zip(position, speed)], key=lambda x: -x[0])
        
        stack = [] # Conterrà i TEMPI DI ARRIVO dei leader di ogni flotta
        
        for pos, sp in infos:
            t = (target - pos) / sp
            
            stack.append(t)
            
            # IL CUORE MONOTONO (Modificato per gli scontri)
            # Se abbiamo almeno 2 macchine nello stack, e quella dietro (appena entrata in cima)
            # ci mette MENO o LO STESSO tempo di quella davanti, significa che sbatte.
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                # La macchina dietro viene "assorbita" dalla flotta di quella davanti.
                # Quindi rimuoviamo l'ultima entrata (il bolide), e lasciamo il leader lento!
                stack.pop() 

        return len(stack)