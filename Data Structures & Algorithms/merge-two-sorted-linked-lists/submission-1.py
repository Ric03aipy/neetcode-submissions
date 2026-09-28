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
        
        # non ci sono edge case perché sono tutti assorbiti: se le liste sono vuote né il while ne gli if si attivano

        dummy = ListNode(0) # il valore del dummy non viene mai letto da nessuno!
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