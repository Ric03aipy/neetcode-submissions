# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # ==============
        # ripetizione #1
        # ==============

        slow = head
        fast = head.next
        while fast and fast.next: 
            slow = slow.next
            fast = fast.next.next

        # partendo con fast avanzato:
        # se pari, slow si trova alla metà inderiore & fast è None
        # se dispari, slow è metà esatta & fast è l'ultimo elemento

        head_inv = slow.next
        prev = None
        slow.next = None
        curr = head_inv
        while curr: 
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp

        # prev è la testa della seconda metà invertita

        # prendo le due teste e inizio a unire
        first = head
        second = prev   # questa è più corta per costruzione
        while second: 
            first_nxt = first.next
            second_nxt = second.next
            first.next = second
            second.next = first_nxt
            # aggiornamento puntatori
            first = first_nxt
            second = second_nxt
        return 







