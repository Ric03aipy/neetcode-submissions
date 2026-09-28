# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        group_prev = dummy
        
        while True:
            # 1. Trovo il k-esimo nodo (la fine del blocco attuale)
            kth = self.getKth(group_prev, k)
            
            # Se non c'è un k-esimo nodo, significa che siamo alla fine 
            # e i nodi rimanenti sono meno di k. Usciamo dal ciclo!
            if not kth:
                break
                
            # Salvo il resto della lista prima di spezzare i legami
            group_next = kth.next
            
            # 2. Inversione IN-PLACE del blocco
            # TRUCCO: Invece di inizializzare 'prev = None', lo inizializzo 
            # a 'group_next'. In questo modo, quando inverto l'ultimo nodo, 
            # si attacca già automaticamente al resto della lista!
            prev, curr = group_next, group_prev.next
            
            while curr != group_next:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
                
            # 3. Ricollego l'Ancora alla nuova testa del gruppo invertito
            # 'kth' è diventato la nuova testa dopo l'inversione.
            # 'group_prev.next' (la vecchia testa) è diventato la nuova coda.
            
            tmp = group_prev.next # Mi salvo la vecchia testa (nuova coda)
            group_prev.next = kth # Attacco l'Ancora alla nuova testa
            group_prev = tmp      # Sposto l'Ancora sulla nuova coda per il prossimo giro!
            
        return dummy.next

    # Helper function per trovare il k-esimo nodo a partire da un nodo 'curr'
    def getKth(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr