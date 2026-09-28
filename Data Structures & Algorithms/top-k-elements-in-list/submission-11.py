class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # ===================
        # ripetizione #2 
        # ===================    

        # edge cases
        if not nums or not k: return []

        # freq
        freq = {}
        for n in nums: freq[n] = freq.get(n, 0) + 1

        # buckets
        max_f = max(freq.values())
        bucket = [[] for _ in range(max_f + 1)]
        for key, val in freq.items(): 
            bucket[val].append(key)
        res = []
        while k:
            if len(bucket[max_f]) <= k: 
                res.extend(bucket[max_f])  
                k -= len(bucket[max_f])
            else: 
                res.extend(bucket[max_f][:k])
                k -= k
            max_f -= 1
        return res



            