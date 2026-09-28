class KthLargest:

    # devo implementare un minheap di dimensione k: in pos [0] il più piccolo dei k più grandi!

    def __init__(self, k: int, nums: List[int]):
        self.capacity = k
        self.size = 0
        self.data = [float('inf')] * k  # è un minheap quindi gli infiniti sono i valori "sentinella" da non prendere
        for n in nums: self.add(n)

    def _swap(self, idx1: int, idx2: idx2): self.data[idx1], self.data[idx2] = self.data[idx2], self.data[idx1]

    def _get_parent(self, idx: int): return (idx - 1) // 2

    def _left(self, idx: int): return 2 * idx + 1

    def _right(self, idx: int): return 2 * idx + 2

    def _sift_down(self): # imposta la regola "ogni nodo maggiore dei figli" top-down - singola iterazione, O(logn)
        idx = 0
        # Ciclo finché esiste ALMENO un figlio (cioè quello sinistro)
        while self._left(idx) < self.capacity :
            left_idx, right_idx = self._left(idx), self._right(idx)
            # Trovo chi è il più piccolo tra i figli presenti
            smallest = left_idx
            # Se esiste anche il destro, e il destro è minore del sinistro, vince il destro
            if right_idx < self.capacity and self.data[right_idx] < self.data[left_idx]:
                smallest = right_idx
            # Se il mio nodo corrente è più grande del figlio più piccolo, faccio swap
            if self.data[idx] > self.data[smallest]:
                self._swap(idx, smallest)
                idx = smallest # Scendo
            else:
                # Se sono minore di entrambi i figli, l'heap è valido! Mi fermo.
                break

    def add(self, val: int) -> int:
        
        if self.size >= self.capacity: # sto sforando
            # Se il nuovo valore è minore o uguale al più scarso (in cima), lo ignoro
            if val <= self.data[0]: 
                return self.data[0] 
            
            # Altrimenti sostituisco la cima e faccio scendere il nuovo arrivato
            self.data[0] = val 
            self._sift_down()

        else: # non sto sforando
            # Inserisco in coda (Sift-Up)
            self.data[self.size] = val
            idx = self.size
            self.size += 1
            # Finché non sono la radice (idx > 0) e sono minore di mio padre, salgo!
            while idx > 0 and self.data[idx] < self.data[self._get_parent(idx)]: 
                parent_idx = self._get_parent(idx)
                self._swap(idx, parent_idx)
                idx = parent_idx

        return self.data[0]


        
        
