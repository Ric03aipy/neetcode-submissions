# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    

    def merge(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        while list1 and list2: 
            if list1.val <= list2.val: 
                curr.next = list1
                list1 = list1.next
            else: 
                curr.next = list2
                list2 = list2.next
            curr = curr.next
        if list1: curr.next = list1
        if list2: curr.next = list2
        return dummy.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # L'idea è in realtà abbastnza semplice: 
        # Faccio il merge sort a coppie disgiunte di 2 liste (letteralmente chiamo l'esercizio "easy: merge 2 list")
        # Poi faccio il merge dei risultati finché non ho una sola unica lista

        k = len(lists)
        if k == 0: return None
        elif k == 1: 
            # qui non ci facciamo niente -> potenzialmente si può fare il merge tra lista non vuota e lista vuota
            # e rendere più compatto il codice
            return lists[0]
        elif k == 2: 
            # qui facciamo il merge a 2, "conquer"
            return self.merge(lists[0], lists[1])
        else: 
            # qui si fa il "divide" 
            half_len = k // 2
            # print(f"passero: {len(lists[:half_len])} elementi")
            left_list = self.mergeKLists(lists[:half_len])
            right_list = self.mergeKLists(lists[half_len:])
            return self.merge(left_list, right_list)











