# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # ==============
        # ripetizione #1
        # ==============

        # Inizio del risultato - pattern con dummy node per evitare corner case e sapere sempre cosa restituire (dummy.next)
        dummy = ListNode()
        curr = dummy

        # Inizializzo la varibaile di riporto
        carry = 0

        # Processo entrambe le liste fino alla fine di entrambe
        while l1 or l2 or carry: 

            # Calcolo della somma
            tot =   (l1.val if l1 else 0) + \
                    (l2.val if l2 else 0) + \
                    carry # al più è 9 + 9 + 1 = 19
            carry, unit = divmod(tot, 10)
            curr.next = ListNode(unit)

            # Aggiorno tutti i puntatori
            if l1: l1 = l1.next
            if l2: l2 = l2.next
            curr = curr.next
        
        return dummy.next

        
        