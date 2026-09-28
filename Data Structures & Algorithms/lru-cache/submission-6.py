class ListNode: 
    def __init__(self, key: int = 0, val: int = 0, pred: Optional[ListNode] = None, succ: Optional[ListNode] = None): 
        self.key = key
        self.val = val
        self.pred = pred
        self.succ = succ

class LRUCache:

    # ===============
    # ripetizione #1
    # ===============

    def __init__(self, capacity: int):
        self.capacity = capacity    # massimo numero di nodi
        self.size = 0               # conta il numero di nodi
        self.cache = {}             # {key: node}
        self.left_dummy = ListNode()
        self.right_dummy = ListNode()
        
        # all'inizio ho solo i due nodi ma devono essere connessi per avere senso di lista
        self.left_dummy.succ = self.right_dummy
        self.right_dummy.pred = self.left_dummy

    def _delete(self, key:int) -> None: 
        # Comportamento come "discard" per i set
        if key not in self.cache: return 
        
        # Prendo i link del nodo da rimuovere
        node = self.cache[key]
        succ = node.succ
        pred = node.pred

        # Dico al gc che la memoria non è usata
        node.succ = None
        node.pred = None
        del self.cache[key] # Anche la mappa deve essere agigonrnata

        # Connetto i restanti 
        succ.pred = pred
        pred.succ = succ

    def _append(self, key:int, val:int) -> None: 
        # tmp info 
        last = self.right_dummy.pred
        
        # Creo il nuovo nodo
        node = ListNode(key = key, val = val, pred = last, succ = self.right_dummy)
        
        # Complete the insertion
        last.succ = node
        self.right_dummy.pred = node

        # Aggionro la mappa di tracciamento
        self.cache[key] = node

    def get(self, key: int) -> int:
        val = -1
        if key in self.cache: 
            val = self.cache[key].val
            self._delete(key)
            self._append(key, val)
        return val

    def put(self, key: int, value: int) -> None:

        # ==============================================
        # Update the value of the key if the key exists.
        # ==============================================

        if key in self.cache: 
            self._delete(key)
            self._append(key, value)
            return 

        # QUI INVECE FACCIO INSERIMENTO NUOVO

        # Qui va usata la capacità
        if self.size == self.capacity:
            # Rimuovo il LRU
            lru = self.left_dummy.succ
            self._delete(lru.key)
            self.size -= 1

        # In ogni caso devo aggiungere un nodo 
        self._append(key, value)
        self.size += 1




