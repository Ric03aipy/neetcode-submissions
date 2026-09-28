class Solution:
    def isValid(self, s: str) -> bool:
        # ===============
        # ripetizione #2
        # ===============

        pairs = {")": "(", "]":"[" , "}":"{"}
        stack = []
        for p in s: 
            if p not in pairs: stack.append(p)
            # se c'è un match rimuovo, altrimenti aggiungo quello che ho in speranza di un futuro match
            else: 
                if stack and pairs[p] == stack[-1]: stack.pop()
                else: stack.append(p)
        return len(stack) == 0