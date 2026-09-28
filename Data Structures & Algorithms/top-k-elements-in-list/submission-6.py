from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {} # {value: frequency}
        max_freq = -1
        for n in nums: 
            seen[n] = seen.get(n, 0) + 1 
            max_freq = max(max_freq, seen[n])
        freqs = defaultdict(list) # {freq: list[values]}
        for key, value in seen.items(): 
            freqs[value].append(key)
        res = []
        i = 0
        while max_freq > 0 and i < k:
            res.extend(freqs[max_freq])
            i += len(freqs[max_freq])
            max_freq -= 1
        return res