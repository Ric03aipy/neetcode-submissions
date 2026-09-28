# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # ==============
        # ripetizione #1
        # ==============

        # Esemipo visivo per codice 1 -> 2 -> 3 -> 4 -> 5 -> 6

        def reverse(node: Optional[ListNode]) -> Optional[ListNode]: 
            """Inverte un segmento. Il segmento deve essere finito."""
            curr = node
            prev = None
            while curr: 
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
            return prev
        
        dummy = ListNode(next=head)
        group_prev = dummy
        while True: 
            head_of_group = group_prev.next # 1 --- 4 --- None
            last_of_group = group_prev # dummy diventa 3 a fine ciclo --- 1 diventa 6 a fine ciclo --- 6 diventa None
            for _ in range(k):
                last_of_group = last_of_group.next
                if not last_of_group: return dummy.next # ritorna
            head_of_next_group = last_of_group.next # 4 --- None
            last_of_group.next = None # delimita il blocco da invertire
            reversed_group_head = reverse(head_of_group) # 3 --- 6
            head_of_group.next = head_of_next_group # 1->4 --- 4 -> None
            group_prev.next = reversed_group_head # dummy->3 --- 1->6
            group_prev = head_of_group  # 1 --- 4
        
        # return dummy.next --- qui non ci arriva mai 