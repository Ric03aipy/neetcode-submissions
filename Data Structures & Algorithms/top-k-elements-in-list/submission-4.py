class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        top_k = []  
        # count occurencies
        for num in nums: 
            counter[num] = counter.get(num, 0) + 1
        max_occ = max(counter.values()) # [1,1,2,2,1] --> 2
        # dict[freq: list[int]]
        freq_levels = {}
        for key, v in counter.items(): # DO NOT CALL THIS k
            freq_levels.setdefault(v, []).append(key)
        # take k values starting from the ones with maximum occurencies
        while k > 0: 
            if max_occ in freq_levels: 
                if k - len(freq_levels[max_occ]) > 0:
                    top_k.extend(freq_levels[max_occ])
                    k -= len(freq_levels[max_occ])
                else: 
                    top_k.extend(freq_levels[max_occ][:k])
                    break
            max_occ -= 1

        return top_k
        