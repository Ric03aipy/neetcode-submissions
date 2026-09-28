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

        """Forse non la soluzione più efficiente (a parità di costo asintotico) ma logicamente chiara."""

        if not head: return head

        seen = {} # id_old: id_new
        news = {} # id_new: Node
        
        curr = head

        # costruisco le corrispondenze
        while curr: 
            new_node = Node(curr.val)
            news[id(new_node)] = new_node
            seen[id(curr)] = id(new_node)
            curr = curr.next

        curr = head

        while curr: 
            new_curr = news[seen[id(curr)]]
            new_curr.next = news[seen[id(curr.next)]] if curr.next else None
            new_curr.random = news[seen[id(curr.random)]] if curr.random else None
            curr = curr.next

        return news[seen[id(head)]]


            
