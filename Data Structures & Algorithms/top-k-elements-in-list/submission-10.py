class Solution:
    # ripetizione #1
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # dry run: example [1,2,2,3,3,3], k=2 and [7,7], k=1

        freq = {}
        # computing frequency 
        for n in nums: freq[n] = freq.get(n, 0) + 1
        # frequency buketes
        buckets = {}
        for key,val in freq.items(): 
            if not val in buckets: buckets[val] = []
            buckets[val].append(key)
        
        # dry run: bucktes = {1: [1], 2: [2], 3:[3]} and {2:[7]}
        # print(buckets)
        max_freq = max(buckets.keys())
        res = []
        while k and max_freq: 
            if max_freq in buckets:
                for v in buckets[max_freq]: 
                    res.append(v)
                    k -= 1
            max_freq -= 1

        return res



