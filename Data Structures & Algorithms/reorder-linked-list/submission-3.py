# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next: return 

        # ======== 1. Trovo la metà ==========
        slow, fast = head, head.next
        while fast and fast.next: 
            slow = slow.next # Corretto: avanza di 1
            fast = fast.next.next
            
        # ======== 2. Inverto la seconda metà ==========
        curr = slow.next
        slow.next = None # Spezzo definitivamente la prima metà dalla seconda
        
        prev = None
        while curr: 
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
            
        # prev ora è la testa della seconda lista capovolta

        # ======== 3. Merge alternato (L'intreccio) ==========
        first = head
        second = prev
        
        # 'second' sarà sempre uguale o più corta di 'first', 
        # quindi basta controllare che non sia finita
        while second: 
            # Salvo i nodi successivi prima di rompere i collegamenti
            tmp1 = first.next
            tmp2 = second.next
            
            # Intreccio le frecce (first -> second -> tmp1)
            first.next = second
            second.next = tmp1
            
            # Mando avanti i puntatori principali per il prossimo ciclo
            first = tmp1
            second = tmp2