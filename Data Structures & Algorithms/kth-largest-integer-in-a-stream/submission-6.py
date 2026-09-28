class KthLargest:

    from collections import heapq

    def __init__(self, k: int, nums: List[int]):
        self.data = []
        self.size, self.capacity = 0, k
        for n in nums: self.add(n)

    def add(self, val: int) -> int:
        if self.size == self.capacity:
            if val > self.data[0]: heapq.heapreplace(self.data, val)
        else: 
            heapq.heappush(self.data, val)
            self.size += 1
            
        return self.data[0]
