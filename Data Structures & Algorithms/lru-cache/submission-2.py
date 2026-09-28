class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}  # {key: Node}
        
        # Dummy nodes per LRU (sinistra) e MRU (destra)
        self.left, self.right = Node(0, 0), Node(0, 0)
        # Li colleghiamo: left <-> right
        self.left.next = self.right
        self.right.prev = self.left

    # --- HELPER 1: Rimuove un nodo dalla lista ---
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev

    # --- HELPER 2: Inserisce un nodo a DESTRA (prima del dummy right, ovvero MRU) ---
    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        
        # Inserisco il nodo in mezzo
        prev.next = node
        nxt.prev = node
        
        # Aggiorno i puntatori del nodo
        node.prev = prev
        node.next = nxt

    # ==========================================

    def get(self, key: int) -> int:
        if key in self.cache:
            # Trovato! Lo stacco da dove si trova e lo rimetto a destra (recente)
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        # Se esiste già, lo rimuovo dalla lista vecchia
        if key in self.cache:
            self.remove(self.cache[key])
            
        # Creo il nodo nuovo (o aggiornato), lo metto nella mappa e lo inserisco a destra
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])
        
        # Controllo la capacità!
        if len(self.cache) > self.cap:
            # Il nodo da cacciare è quello subito a destra del dummy 'left'
            lru = self.left.next
            self.remove(lru)
            # Rimuovo anche dal dizionario (ECCO perché il nodo doveva salvare anche la sua key!)
            del self.cache[lru.key]