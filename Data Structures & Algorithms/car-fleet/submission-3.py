class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        # parallel sorting based on position, but reversed ...
        infos = sorted([(pos, sp) for pos, sp in zip(position, speed)], key=lambda x: -x[0])
        # print(infos)

        # l'idea risolutiva: calcolare il tempo è facile: tempo=(spazio=target-posizione)/velocità
        # se una macchina supera un'altra vuol dire che va abbastnza veloce da metterci meno tempo in termini assoluti (se si considera la possibilità di superare) o uguale tempo (con il vincolo di avere la stessa velocità quando viene formata la flotta con chi sta avanti)
        # quindi formano flotte distinte solo macchine con tempi crescenti

        stack = []
        for idx, (pos, sp) in enumerate(infos): 
            t = (target - pos)/sp
            # print(f"tempo impiegato da {idx} = {t}")
            if not stack or t > (target-infos[stack[-1]][0]) / infos[stack[-1]][1]: # la macchina corrente ci mette meno o stesso tempo, quindi formerà una flotta con qualche altra macchina davanti (già in stack)
                # stack.pop()
                stack.append(idx)
            # print(stack)
        return len(stack)
