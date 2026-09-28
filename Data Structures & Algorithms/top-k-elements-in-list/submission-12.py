class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # ===================
        # ripetizione #3
        # ===================

        """
        ok i bucket di frequenza, cmq li devi implementare xke non ci 6 arrivato, ma
        che ne pensi anche dell'idea del puntatore che fa gli spostamenti per ordinare tuple (freq, valore) ? 
        """

        freq_buck = [[] for _ in range(len(nums) + 1)]
        freq = {}
        for n in nums: freq[n] = freq.get(n, 0) + 1
        for key, val in freq.items(): 
            freq_buck[val].append(key)
        res = []
        for i in range(len(freq_buck) - 1, -1, -1): 
            if len(freq_buck[i]) <= k: 
                k -= len(freq_buck[i])
                res.extend(freq_buck[i])
            else: 
                for j in range(k): 
                    res.append(freq_buck[i][j])
        return res