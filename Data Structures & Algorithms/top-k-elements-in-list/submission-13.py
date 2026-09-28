class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # ===================
        # ripetizione #6
        # ===================

        freq = {}
        for n in nums: freq[n] = freq.get(n, 0) + 1
        freq_buckets = [[] for _ in range(len(nums) + 1)] # da 0 a n frequenze
        for n, f in freq.items(): freq_buckets[f].append(n)
        res = []
        idx = len(nums)
        while k > 0: 
            if len(freq_buckets[idx]) <= k: 
                res.extend(freq_buckets[idx])
                k -= len(freq_buckets[idx])
                idx -= 1
            else: 
                res.extend(freq_buckets[idx][k-len(freq_buckets[idx])])
                k = 0
        return res