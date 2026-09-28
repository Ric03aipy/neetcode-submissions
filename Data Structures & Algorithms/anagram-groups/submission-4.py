class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # ===========================================================================
        # questa è la scheda delle ripetizioni: cancella e riscrivi la soluzione
        # ===========================================================================

        alphabet = {c:i for i, c in enumerate("abcdefghijklmnopqrstuvwxyz")}
        res = {}
        for s in strs:
            active = [0] * 26 
            for c in s: 
                active[alphabet[c]] += 1
            active = tuple(active)
            if active in res: 
                res[active].append(s)
            else: 
                res[active] = [s]
        return list(res.values())