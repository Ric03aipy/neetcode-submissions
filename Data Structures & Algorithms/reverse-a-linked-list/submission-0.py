# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # O(1) in space richiesto quindi va fatto in place
        # Idea: invertire i link tra nodo x e nodo x+1

        # Inizializzazione
        prev = None
        curr = head

        # Nell'edge case in cui head = [] non entra nel while e viene ritornato [];
        # Nel caso comune il ciclo finirà quando (curr is None) == True --> la testa invertita è il precedente
        while curr: 
            # salvo l'info che viene persa 
            nxt = curr.next     
            # inverto il ptr
            curr.next = prev    
            # muovo in avanti i puntatori (gli stessi dell'inizializzazione)
            prev = curr         
            curr = nxt

        return prev