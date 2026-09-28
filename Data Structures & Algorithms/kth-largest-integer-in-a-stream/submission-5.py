class KthLargest:

    # ===============
    # ripetizione #1
    # ===============


    def __init__(self, k: int, nums: List[int]):
        self.capacity = k
        self.size = 0
        self.data = []
        for n in nums: self.add(n)        

    def get_parent(self, idx) -> int | None:
        """Return the index of the parent of the input node index"""
        return (idx - 1) // 2 if idx != 0 else None

    def get_children(self, idx) -> tuple[int|None, int|None]: 
        """Return the indeces of the children of the input node index""" 
        left = 2 * idx + 1
        right = 2 * idx + 2
        return (left if left < self.size else None, right if right < self.size else None)

    def add(self, val: int) -> int:
        # Se la capacità è piena posso solo estrarre e aggiungere e aggiustare dall'alto
        if self.size == self.capacity:
            # Se è più piccolo di ciò che sta in cima (k esimo più grande) non lo inserisco affatto
            # Altrimenti lo inserisco come potenziale k esimo o i esimo inferiore a k
            # (Sto costruendo un minheap dei k valori maggiori)
            if val > self.data[0]:
                self.data[0] = val
                self.adjust_top_down()  # SIFT DOWN 
        else:
            # Altrimenti lo aggiungo e aggiusto dal basso
            self.data.append(val)
            self.size += 1
            self.adjust_bottom_up()         # SIFT UP
        return self.data[0]


    # In un minheap la radice è sempre minore dei figli, per ogni possibile sottoalbero
    def adjust_top_down(self, i=0): # Si può fare anche da un indice specifico: serve per il SIFT UP
        idx = i
        while True: 
            left, right = self.get_children(idx)
            # Casi d'uscita: sono arrivato al termine oppure sono a un nodo prima della foglia ma sono ok
            if left is None and right is None: break
            if right is None:
            # Caso in cui c'è un solo figlio (necessariamente left) -> dummy node per fare i calcoli uguali al caso generale
                if self.data[idx] > self.data[left]: 
                    self.data[left], self.data[idx] = self.data[idx], self.data[left]
                break

            # Qui esistono entrambi i figli. Il nodo potrebbe essere maggiore di entrambi i figli.
            # Se il nodo è già messo bene non faccio niente
            if self.data[idx] <= self.data[left] and self.data[idx] <= self.data[right]: break 
            # Altrimenti lo scambio con il minimo dei figli: in questo modo è garantito che chi finisce dove c'è data[idx]
            # continua a essere più piccolo dei figli
            minimum_idx = left if self.data[left] <= self.data[right] else right
            self.data[minimum_idx], self.data[idx] = self.data[idx], self.data[minimum_idx]
            idx = minimum_idx

    def adjust_bottom_up(self): 
        # L'ultimo entrato
        idx = self.size - 1
        parent = self.get_parent(idx)
        while parent is not None and self.data[idx] < self.data[parent]: 
            self.data[idx], self.data[parent] = self.data[parent], self.data[idx]
            idx = parent
            parent = self.get_parent(idx)
        
        self.adjust_top_down(parent if parent is not None else 0)
        







