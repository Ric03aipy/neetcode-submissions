class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        import heapq

        # MinHeap dei k valori più grandi: il kth più grande è la radice. 

        first_k = [nums[i] for i in range(k)]  # O(k) in space
        heapq.heapify(first_k)                  # O(k) in time

        for i in range(k, len(nums)):           # O(n) in time
            if nums[i] > first_k[0]: 
                heapq.heapreplace(first_k, nums[i]) # O(log k) in time

        return first_k[0]





