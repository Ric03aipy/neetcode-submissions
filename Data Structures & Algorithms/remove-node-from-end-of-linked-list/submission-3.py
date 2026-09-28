# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left = dummy
        right = dummy
        
        # 1. Distanzio right di n passi
        for _ in range(n):
            right = right.next
            
        # 2. Faccio scorrere la finestra finché right non è l'ULTIMO NODO (non None)
        while right.next:
            left = left.next
            right = right.next
            
        # 3. Ora 'left' è perfettamente posizionato un passo PRIMA del nodo da eliminare
        left.next = left.next.next
        
        # 4. Ritorno la nuova testa sicura (NON head)
        return dummy.next