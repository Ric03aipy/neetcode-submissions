class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def is_anagram(a, b): # O(n)
            if len(a) != len(b): return False 
            for c1, c2 in zip(sorted(list(a)), sorted(list(b))): 
                if c1 != c2: return False
            return True

        res = []
        processed = set()
        for idx, s1 in enumerate(strs): 
            if s1 not in processed:
                anagram_of_i = [s1]
                processed.add(s1)
                for jdx, s2 in enumerate(strs[idx+1:]): 
                    if is_anagram(s1, s2): 
                        anagram_of_i.append(s2)
                        processed.add(s2)
                res.append(anagram_of_i)
        return res
                

