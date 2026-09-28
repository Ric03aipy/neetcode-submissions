class Solution:
    def isValid(self, s: str) -> bool:
        # ===============
        # ripetizione #1 
        # ===============

        matches = {"{": "}", "[": "]", "(": ")"}

        stack = []

        for c in s: 
            if c in matches: stack.append(c)
            if c in matches.values(): 
                if not stack or c != matches[stack[-1]]: return False
                stack.pop()
                
        return not stack

     