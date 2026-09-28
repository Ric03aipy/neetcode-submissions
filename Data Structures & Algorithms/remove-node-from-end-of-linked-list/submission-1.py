# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        # approccio finestra mobile su lista: n elementi in finestra

        # creo il dummy node 
        dummy = ListNode(0, head)
        left = dummy
        right = dummy
        winlen = 0

        # n passi per right
        while winlen < n: # è garantito che 1 <= n <= len(LinkedList)
            right = right.next
            winlen += 1

        print(left.val, right.val)
        # avanzo entrambi fino alla fine
        prev = dummy
        while right:
            prev = left
            left = left.next
            right = right.next
        print(prev.val, left.val)
        prev.next = left.next
        # print(left.val, left.next.val)


        return dummy.next
