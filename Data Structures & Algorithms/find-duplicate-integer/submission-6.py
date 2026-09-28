class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # ===============
        # ripetizione #1 SLOW & FAST PTRS 
        # ===============

        # LOGICA: 
        # nums è lungo n+1 
        # nums contiene numeri da 1 a n 
        # Userei un approccio 'two pointers' come su liste 'fast and slow' per trovare l'inizio del ciclo
        # l'approccio è fast & slow ma non procedendo di uno o due passi posizionali bensì uno o due passi basati
        # sul contenuto delle celle (che sono posizioni valide !)
        # Una volta trovato l'ingesso del ciclo,
        
        slow, fast = 0, 0 

        while True: 
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast: break
        
        slow2 = 0 
        while True: 
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2: break

        return slow