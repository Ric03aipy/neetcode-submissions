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
        # ========================
        # ripetizione #1 con mappa
        # ========================

        matches = {None:None}
        
        curr = head
        while curr: 
            matches[curr] = Node(curr.val)
            curr = curr.next

        curr = head
        while curr:
            matches[curr].next = matches[curr.next]
            matches[curr].random = matches[curr.random]
            curr = curr.next
        
        return matches[head]
