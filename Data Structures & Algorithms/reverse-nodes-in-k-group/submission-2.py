# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # La lista può essere lunga meno di k elementi, k elementi, o più di k elementi. 
        # La complessità richiesta è O(n) in tempo e O(1) in spazio, quindi fare una passata per conoscere la lunghezza
        # potrebbe non essere la cosa più efficiente ma non rompe la complessità asintotica richiesta e facilita il compito.
        # Supponiamo di avere la lunghezza L, es. L=8, e supponiamo k=3
        # Supponiamo head = [1,2,3,4,5,6,7,8], l'output atteso è [3,2,1,6,5,4,7,8]
        # Con divmod posso sapere quante liste devo invertire esattamente e quanti nodi restano fuori 
        # Ogni k posso chiamare una funzione che inverte la lista in place (problema easy di sezione)

        # def print_list(node: Optional[ListNode]) -> None:
        #     s = ""
        #     curr = node
        #     while curr:
        #         s += str(curr.val) + "->"
        #         curr = curr.next
        #     print(s)

        # Calcolo la lunghezza - O(n)
        def get_len(node: Optional[ListNode]) -> int:
            l = 0
            curr = node
            while curr: 
                l += 1
                curr = curr.next
            return l

        l = get_len(head)

        # Caso base in cui non c'è niente da fare, mi risparmio il rischio di enrare in loop senza motivo
        if l < k: return head 
        
        # Conto quante inversioni devo fare
        div, rem = divmod(l, k) # l = div * k + rem

        # Inversione effettiva - O(div)*O(k)=O(n)
        def reverse(node: Optional[ListNode], k:int) -> (Optional[ListNode], Optional[ListNode]): 
            """Reverse IN PLACE. Return head and tail of the reversed list."""
            curr = node
            prev = None
            for _ in range(k): 
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
            # print_list(prev)
            return prev, node # prev non è puntato da niente punta al prox nodo, node è puntato dal penultimo, punta a None

        heads = []
        tails = []

        dummy_head = ListNode()
        final_head = ListNode()
        curr = head
        for i in range(div): 

            pre_advancing_node = curr
            for _ in range(k): 
                curr = curr.next
            post_advancing_node = curr
            rev_head, rev_tail = reverse(pre_advancing_node, k)

            heads.append(rev_head)
            tails.append(rev_tail)
  
        # print([h.val for h in heads])
        # print([t.val for t in tails])

        for i in range(1, len(heads)):
            tails[i-1].next = heads[i]
        tails[-1].next = curr

        return heads[0]















