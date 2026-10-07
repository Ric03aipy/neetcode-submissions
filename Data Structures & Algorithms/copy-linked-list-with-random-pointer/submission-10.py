"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # ===============
        # ripetizione #2
        # ===============

        # Costruisco la mappatura: {nodo vecchio: nodo nuovo}
        node_map = {None:None} # trick
        curr = head
        while curr: 
            node_map[curr] = Node(curr.val)
            curr = curr.next

        copy_head = node_map[head]
        copy_curr = copy_head
        curr = head
        while curr:
            copy_curr.next = node_map[curr.next]
            copy_curr.random = node_map[curr.random]

            copy_curr = copy_curr.next
            curr = curr.next


        return copy_head

        
        
