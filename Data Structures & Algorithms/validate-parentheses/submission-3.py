class Solution:
    def isValid(self, s: str) -> bool:
        # DRY RUN per cercare l'idea 
        # s = ([{}])
        # leggo ( metto in pila
        # leggo [ metto in pila
        # leggo { metto in pila
        # leggo } estraggo dalla pila -> cio che ho estratto è { ? se non è è invalida
        # ...
        # default se arrivo alla fine è valida
        opener_of = {"}": "{", "]":"[", ")":"("}
        opener = list(opener_of.values())
        stack = []
        for c in s: 
            if c in opener: 
                stack.append(c)
            else: 
                match = opener_of[c]
                if stack and match == stack[-1]: # if stack verifica che non sia vuota evitanod OutOfRange
                    stack.pop()
                else: 
                    return False
        if stack: return False # Nel caso in cui alla fine di s la pila non è vuota
        return True