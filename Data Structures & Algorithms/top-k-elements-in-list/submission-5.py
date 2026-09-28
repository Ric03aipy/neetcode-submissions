from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {} # {value: frequency}
        MIN_N = -1001
        k_most_freq = [MIN_N] * k
        max_freq = -1
        for n in nums: 
            seen[n] = seen.get(n, 0) + 1 
            max_freq = max(max_freq, seen[n])
        # print(seen, max_freq)
        freqs = defaultdict(list) # {freq: list[values]}
        for key, value in seen.items(): 
            freqs[value].append(key)
        # print(freqs)
        res = []
        i = 0
        while max_freq > 0 and i < k:
            # print(res, i, max_freq)
            res.extend(freqs[max_freq])
            i += len(freqs[max_freq])
            max_freq -= 1
            # print(res, i, max_freq)
            # print()
        return res