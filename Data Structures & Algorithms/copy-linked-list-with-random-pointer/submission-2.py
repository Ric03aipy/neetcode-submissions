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
        if not head: return head

        matches = {}
        
        curr = head

        # costruisco le corrispondenze
        while curr: 
            new_node = Node(curr.val)
            matches[curr] = new_node
            curr = curr.next

        curr = head

        while curr: 
            new_curr = matches[curr]
            new_curr.next = matches[curr.next] if curr.next else None
            new_curr.random = matches[curr.random] if curr.random else None
            curr = curr.next

        return matches[head]


