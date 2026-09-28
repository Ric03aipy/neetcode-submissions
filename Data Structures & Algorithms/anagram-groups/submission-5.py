class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # ===================
        # ripetizione #2
        # ===================

        # l'algoritmo naive è O(k*n^2) in tempo, O(1) in spazio; il seguente è O(n) in tempo ... spazio

        stringmap = {}

        for s in strs: 
            key = [0] * 26 
            for c in s: key[ord(c) - ord('a')] += 1
            key = tuple(key)
            if key not in stringmap: stringmap[key] = []
            stringmap[key].append(s)

        return list(stringmap.values()) 

