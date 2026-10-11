# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # ==============
        # ripetizione #1
        # ==============

        # dummy per i border case
        dummy = ListNode(next=head)
        left = dummy
        right = dummy
        # ciclo per creare la distanza di n+1 celle (bordi inclusi) --- ovvero la finestra
        for _ in range(n): right = right.next 
        # ciclo per far scorrere la finestra e far fermare left davanti all'elemento da eliminare
        while right and right.next: 
            right = right.next
            left = left.next
        # elimino
        left.next = left.next.next
        return dummy.next
            
