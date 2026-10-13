class Solution:
    def isValid(self, s: str) -> bool:
        # ================
        # ripetizione #3
        # ================

        match = {")":"(", "]":"[", "}":"{"}
        stack = []
        for par in s: 
            if par not in match: 
                stack.append(par)
            else: 
                if stack and match[par] == stack[-1]: stack.pop()
                else: return False
        return not stack