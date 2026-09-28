# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    

    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # ==============
        # ripetizione #1
        # ==============
        

        l = len(lists)
        if l == 1: return lists[0]
        elif l == 2:  
            left_half, right_half = lists[0], lists[1]
        else: 
            left_half = lists[: l // 2]
            right_half = lists[l // 2: ]
            # print(left_half, right_half)
            
            # Divide 
            if l > 2: 
                # print("invio chiamata left", left_half)
                left_half = self.mergeKLists(left_half)
                # print("invio chiamata right", right_half)
                right_half = self.mergeKLists(right_half)
            
        # Merge a 2 - il dummy node mi evita di chiedermi se la lunghezza è 0,1,2
        # Qui left/right_half sono entrambe ordinate internamente

        # Impera

        # print("impera", left_half, right_half)
        # Mi servono le liste semplici, non liste di liste

        dummy = ListNode()
        curr = dummy
        while left_half and right_half: 
            if left_half.val <= right_half.val: 
                curr.next = left_half
                left_half = left_half.next
            else: 
                curr.next = right_half
                right_half = right_half.next
            curr = curr.next 
        
        if left_half: curr.next = left_half
        
        if right_half: curr.next = right_half

        return dummy.next    
        