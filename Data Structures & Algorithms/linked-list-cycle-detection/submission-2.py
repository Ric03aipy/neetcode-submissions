# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head: return False
        # Il modo banale è ricordarsi tutti i nodi visitati e ogni nodo che si visita confrontare con quelli già visti
        # Ma costerebbe O(n^2) in time e O(n) in space
        
        # Fast/Slow porta a O(n) time e O(1) space
        slow = head
        fast = head.next

        while fast and fast.next: 
            
            if slow == fast: return True
            
            slow = slow.next
            fast = fast.next.next

        return False

