class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # edge case
        if not tokens: return 0
        
        operators = ["+", "-", "*", "/"] 
        # dry run - ["1","2","+","3","*","4","-"]
        # Assume that division between integers always truncates toward zero 
        # --> Invece di / uso // 
        # The operands may be integers or the results of other operations. 
        # --> Un operatore si aspetta 1 o 2 operandi 
        # errore per tokens=["10","6","9","3","+","-11","*","/","*","17","+","5","+"] --> non necessariamente operazioni a 2, ma anche espressioni annidate
        # 10, 6, 9, 3 in stack
        # leggo + prendo 3, 9 li sommo e metto 12 in stack -> 10, 6, 12
        # appendo -11 -> 10, 6, 12, -11
        # leggo * prendo -11, 12 e li moltiplico, metto -132 in stack -> 10, 6, -132
        # OCCHIO ALL'ORDINE: leggo / prendo -132, 6 e li divido: 6/-132=0, metto 0 in stack -> 10, 0
        # leggo * prendo 0, 10 e li molitplico, metto 0 in stack -> 0
        # appendo 17 -> 0, 17
        # leggo + prendo 0, 17 e li sommo, metto 17 in stack -> 17
        # appendo 5 -> 17, 5
        # leggo + prendo 17, 5 -> 22

        # Idea: con un approccio greedy, 
        # appena vedo un operatore faccio i calcoli con gli operandi che ho in memoria
        stack = []
        for token in tokens: 
            if token in operators: 
                # alla prima iterazione sono sicuro ci siano 2 operandi perché tutti gli operatori sono binari
                # --- 
                # alle iterazioni successive ci operand_1 è un nuovo operando, operand_2 è il risultato 
                # precedente
                # se la logica applicata è corretta, il casting esplicito non può andare in errore
                operand_1 = int(stack.pop())
                operand_2 = int(stack.pop())
                match token:
                    case "+": res = operand_2 + operand_1
                    case "-": res = operand_2 - operand_1
                    case "*": res = operand_2 * operand_1
                    case "/": res = int(operand_2 / operand_1)
                    case _: 
                        print("Devi fare debugging della logica che stai applicando...")
                stack.append(res)
            else: 
                stack.append(token)
            # print(stack)
        return int(stack[0]) # se la logica è corretta resta un unico elemento nella pila, converte in int per l'edge case di token=['1'] (solo numeri)


