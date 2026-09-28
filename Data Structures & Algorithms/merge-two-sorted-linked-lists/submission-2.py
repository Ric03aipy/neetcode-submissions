# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode()
        curr = dummy
        curr1 = list1
        curr2 = list2 

        while curr1 and curr2:
            if curr1.val <= curr2.val:
                curr.next = ListNode(curr1.val)
                curr1 = curr1.next
            else: 
                curr.next = ListNode(curr2.val)
                curr2 = curr2.next
            curr = curr.next 

        if curr1: curr.next = curr1
        if curr2: curr.next = curr2

        return dummy.next   # head


