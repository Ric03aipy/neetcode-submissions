# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Il merge sort di per se è molto semplice: pesco da uno dei due array ordinati facendo confronti a ogni aggiunta
        # Invece di 2 array ho 2 liste
        # Questa intuizione è O(n+m) in time e in space

        # La richiesta è O(n+m) in time, ma O(1) in space
        # Con le liste infatti non devo allocare n+m nuovi nodi necessariamente, ma devo inserire al posto giusto i nodi 

        # Tutti gli edge case per non rompere listX.val
        if not list1 and list2: return list2
        if not list2 and list1: return list1
        if not list1 and not list2: return None

        # potremmo fare la furbata di chiamare la funzione per assicurarci che una delle due abbia la testa minore
        # ma non è necessario perché è sufficiente un dummy node con valore minimo per iniziare ad attaccare dei pezzi
        # Dai constraints del problema: -100 <= Node.val <= 100 
        
        dummy = ListNode(-101)
        curr = dummy

        while list1 and list2: 
            if list1.val <= list2.val:
                curr.next = list1
                list1 = list1.next
            else: 
                curr.next = list2
                list2 = list2.next
            curr = curr.next 
            # curr non è mai None: prima aggiorno curr e poi la lista, quando la lista è non il ciclo si interrompe

        if list1: 
            # print(curr.__dict__)
            curr.next = list1

        if list2: 
            # print(curr.__dict__)
            curr.next = list2

        return dummy.next