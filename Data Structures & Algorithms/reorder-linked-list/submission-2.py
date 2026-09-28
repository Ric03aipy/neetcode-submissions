# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        if not head: return  

        # ======== trovo la metà ==========

        slow, fast = head, head.next
        while fast and fast.next: 
            slow = slow.next
            fast = fast.next.next
            if slow == fast:    # controllo per cicli
                slow.next = None
            
        # print(f"slow={slow.val}") # slow è l'ultimo elemento che fa parte della prima metà
        # ======== inverto la seconda metà ==========

        curr = slow.next
        slow.next = None
        prev = None
        while curr: 
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        # prev è la testa della seconda lista

        # ======== merge alternato ==========
        
        i = 0
        dummy = ListNode()
        curr = dummy
        while head and prev: 
            if not i % 2: 
                # print("aggiungo da head i=",i)
                dummy.next = head
                # print("aggiunto=", dummy.next.val)
                head = head.next
            else: 
                # print("aggiungo da prev i=",i)
                dummy.next = prev
                # print("aggiunto=", dummy.next.val)
                prev = prev.next
            dummy = dummy.next
            i += 1

        if head: 
            # print("completo head")
            dummy.next = head
        if prev: 
            # print("completo prev")
            dummy.next = prev

        head = curr.next
        
        
        
# ricarica conto hype
# ricarica telefonica per chiamare



