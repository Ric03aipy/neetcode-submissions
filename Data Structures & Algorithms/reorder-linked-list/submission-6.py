# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # ==============
        # ripetizione #2
        # ==============

        # [0, n-1, 1, n-2, 2, n-3, ... n - n // 2 - 1, n - n // 2]
        # n=8 [0, 7, 1, 6, 2, 5, 3, 4]
        # n=9 [0, 8, 1, 7, 2, 6, 3, 5, 4]

        # Se avessi [0, 1, 2, 3] e [7, 6, 5, 4] sarebbe un semplice merge
        # Quindi mi serve dividere in 2 e poi invertire la seconda

        # =================== Divisione in 2 ===================

        # n pari (es.4) fast segue 0,2,4 puntando a None; nel frattempo slow segue 0,1,2 puntando 2nd elemento.
        # n dispari (es.5) fast segue 0,2,4 puntando a 5 (non esiste il next); nel frattempo slow segue 0,1,2. 
        # Quindi slow punta all len//2 esimo elemento -> la parte destra è sempre lunga almeno quando quella sinistra
        # Se però la testa della destra è slow.next allora è la parte sinistra ad essere sempre più lunga, strettamente.
        # Quando però la lunghezza iniziale è pari, con next & partenza fast=0 allora la lista di sinistra verrà 2 elementi 
        # più lunga di quella di destra. Va bene? 

        slow = head
        if not head.next: return # Caso singoletto
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Mi chiedo se è leggittimo dichiarare slow.next qui
        # Se fast è più avanti sicuramente sì. Quando slow e fast sono identici? Quando fin da subito fast.next non esiste.
        # Questo significa che la lista è un singoletto: [X]. 
        # Un singoletto si può ritornare subito, è già ordinato nel modo richiesto. Controllo che siano uguali i puntatori.


        # =================== Inversione della seconda metà ===================
        first_half = head
        second_half = slow.next
        slow.next = None
        
        # Ora le due liste sono separate
        prev = None
        while second_half: 
            tmp = second_half.next
            second_half.next = prev
            prev = second_half
            second_half = tmp
        # Ora second half è None, prev punta alla testa inveritita della second metà

        # =================== Merge: inserimenti di ogni nodo di l2 in l1 ===================
        l1 = first_half
        l2 = prev

        curr = l1

        while l2: 
            tmp1 = l1.next
            l1.next = l2
            tmp2 = l2.next
            l2.next = tmp1
            l1 = tmp1
            l2 = tmp2            

