class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {} # (array) : [list anagrams]
        alphabet = {c:i for i, c in enumerate("abcdefghijklmnopqrstuvwxyz")}
        for i, s in enumerate(strs): 
            entry = [0] * 26 # frequency array
            for c in s:
                entry[alphabet[c]] += 1
            entry = tuple(entry)
            if entry in res: 
                res[entry].append(s)
            else: 
                res[entry] = [s]
        return list(res.values())
            
