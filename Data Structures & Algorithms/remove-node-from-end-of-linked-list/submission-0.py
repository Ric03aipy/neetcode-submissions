# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Approccio O(1) space ma senza troppo cervello: scorro e ottengo la lunghezza totale (es. 13)
        # L'ennesimo dalla fine (e. 4°) è l'elemento numero l-nth+1 (es. 13-4+1, il decimo nodo)
        # Un altra passata lineare e si salta esattamente quell'elemento ricordandosi il prev 
        # Tempo O(2n)=O(n) asinoticamente

        if not head: return head

        l = 0
        curr = head
        while curr: 
            l += 1
            curr = curr.next

        pos = l - n + 1

        if pos == 1: return head.next

        # print("lunghezza =", l, "posizione =", pos)

        seen = 1
        prev = None
        curr = head
        while curr: 
            if seen == pos: 
                # print(f"entra qui con valore = {curr.val}")
                prev.next = curr.next
            seen += 1
            prev = curr
            curr = curr.next

        return head
        
        