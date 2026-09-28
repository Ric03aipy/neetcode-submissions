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

        # Current_node per non alterare le liste iniziali
        c1, c2 = l1, l2

        # Inizializzo la varibaile di riporto
        carry = 0

        # Processo entrambe le liste fino alla fine di entrambe
        while c1 or c2 or carry: 

            # Calcolo della somma
            tot =   (c1.val if c1 else 0) + \
                    (c2.val if c2 else 0) + \
                    carry # al più è 9 + 9 + 1 = 19
            carry, unit = divmod(tot, 10)
            curr.next = ListNode(unit)

            # Aggiorno tutti i puntatori
            if c1: c1 = c1.next
            if c2: c2 = c2.next
            curr = curr.next
        
        return dummy.next

        
        