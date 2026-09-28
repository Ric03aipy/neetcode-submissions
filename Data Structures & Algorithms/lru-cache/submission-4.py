class Node: 
    def __init__(self, key:int=0, val:int=0, nxt:Optional[Node]=None, prev:Optional[Node]=None):
        self.key = key
        self.val = val
        self.next = nxt
        self.prev = prev
    def __repr__(self):
        return f"({self.key}, {self.val})"

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.dummy_lru = Node()
        self.dummy_mru = Node()
        self.dummy_lru.next = self.dummy_mru
        self.dummy_mru.prev = self.dummy_lru

    def remove(self, node:Node):
        """Removes a node."""
        prv, nxt = node.prev, node.next
        prv.next = nxt
        nxt.prev = prv

    def insert(self, node:Node):
        """Insert at right"""
        last = self.dummy_mru.prev
        last.next = node
        node.prev = last
        node.next = self.dummy_mru
        self.dummy_mru.prev = node

    def get(self, key: int) -> int:
        if key not in self.cache: return -1 
        node = self.cache[key]
        res = node.val
        self.remove(node)
        self.insert(node)
        return res

    def put(self, key: int, value: int) -> None:
        if key not in self.cache: # inserimento di un nuovo nodo
            new_node = Node(key=key, val=value)
            if len(self.cache) + 1 > self.capacity: # se non c'è disponibilità prima devo fare spazio
                lru = self.dummy_lru.next
                del self.cache[lru.key]
                self.remove(lru)
            self.cache[key] = new_node
            self.insert(new_node)
        else: # aggiornamento di un vecchio nodo 
            node = self.cache[key]
            del self.cache[key]
            self.remove(node)
            # self.insert(node)
            self.put(key, value)







