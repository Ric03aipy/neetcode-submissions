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
            head_of_group = group_prev.next # 1
            last_of_group = group_prev # dummy->3
            for _ in range(k):
                last_of_group = last_of_group.next
                if not last_of_group: return dummy.next
            head_of_next_group = last_of_group.next # 4
            last_of_group.next = None
            reversed_group_head = reverse(head_of_group) # 3
            head_of_group.next = head_of_next_group # 1->4
            group_prev.next = reversed_group_head
            group_prev = head_of_group
        
        return dummy.next