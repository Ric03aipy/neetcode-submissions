"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        """"Versione più veloce, e addirittura con O(1) in spazio - meglio della richiesta"""

        if not head:
            return None
        
        # FASE 1: Intreccio i cloni nella lista originale
        curr = head
        while curr:
            # Creo il clone
            clone = Node(curr.val)
            
            # Lo inserisco tra curr e curr.next
            clone.next = curr.next
            curr.next = clone
            
            # Avanzo di 2 passi (salto il clone appena creato)
            curr = clone.next
            
        # FASE 2: Assegno i puntatori random ai cloni
        curr = head
        while curr:
            if curr.random:
                # Il random del clone punta al NEXT del random originale
                curr.next.random = curr.random.next
            
            # Salto al prossimo nodo originale
            curr = curr.next.next
            
        # FASE 3: Separo le due liste
        curr = head
        clone_head = head.next # Questa sarà la testa da restituire
        
        while curr:
            clone = curr.next
            
            # Ripristino la lista originale (A -> B)
            curr.next = clone.next
            
            # Collego la lista clonata (A' -> B')
            if clone.next:
                clone.next = clone.next.next
                
            # Avanzo sulla lista originale
            curr = curr.next
            
        return clone_head