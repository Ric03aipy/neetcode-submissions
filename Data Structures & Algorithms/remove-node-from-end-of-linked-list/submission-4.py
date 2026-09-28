# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Nodo dummy per 1) gestire casi tediosi come [singoletto] e 2) sapere sempre cosa ritornare, dummy.next
        dummy = ListNode(next=head)
        # Approccio sliding window
        left = dummy
        right = dummy
        # Es. [dummy, head=1,2,3,4] n=2 (valore 3)
        for i in range(n): right = right.next
        # Es. --> left.val=dummay.val, right.val=2
        while right.next: 
            left = left.next
            right = right.next 
        # Es. left.val=2, right.val=4
        # Il salto 
        left.next = left.next.next
        # return tipico del dummy node pattern 
        return dummy.next

