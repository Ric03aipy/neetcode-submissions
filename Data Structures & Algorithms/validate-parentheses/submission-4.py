class Solution:
    def isValid(self, s: str) -> bool:
        opener_of = {"}": "{", "]":"[", ")":"("}
        stack = []
        for c in s: 
            if c not in opener_of: # Se non è una chiave (quindi non è una parentesi chiusa)
                stack.append(c) # Allora è un'aperta!
            else: 
                match = opener_of[c]
                if stack and match == stack[-1]: # if stack verifica che non sia vuota evitanod OutOfRange
                    stack.pop()
                else: 
                    return False
        return len(stack) == 0  # Nel caso in cui alla fine di s la pila non è vuota