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

        for old_node, new_node in matches.items(): 
            if old_node: 
                new_node.next = matches[old_node.next]
                new_node.random = matches[old_node.random]
        
        return matches[head]
