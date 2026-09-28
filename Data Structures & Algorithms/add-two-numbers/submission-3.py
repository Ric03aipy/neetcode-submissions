# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # ====================
        # ripetizione #1
        # ====================

        # Creo un nodo che fa da puntatore alla testa e mi para dai corner case
        dummy = ListNode() 
        curr = dummy

        carry = 0   # riporto

        # Se ho delle liste oppure ho un carry avanzante ho bisogno di continuare a creare nodi 
        while l1 or l2 or carry: 
            
            # Sfrutto l'elemento neutro dell'addizione per scrivere codice compatto
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0 
            
            # Calcolo la somma
            s = v1 + v2 + carry
            carry, unit = divmod(s, 10)

            # Aggiungo il nodo e 
            node = ListNode(unit)
            curr.next = node

            # Avanzo i puntatori
            curr = curr.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next 

        # Ritorno tipico della tecnica del dummy node
        return dummy.next

