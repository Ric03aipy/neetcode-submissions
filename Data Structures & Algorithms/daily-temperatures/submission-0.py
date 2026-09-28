class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures) # inizializzo a zero in modo che il while quando non viene verificato non tocca nessun indice qui, dunque il valore di default è già presente ; l'edge case vuoto -> [] è già coperto perché non fa iterazioni nel ciclo for e va direttamente alla return finale
        stack = [] # inserisco qui tuple (indice, temperatura)
        for i, t in enumerate(temperatures): 
            # if stack serve per la prima iterazione, si portrebbe anche mettere fuori ciclo
            while stack and t > stack[-1][1]: # la stack è costuita in modo che sopra ci finisce sempre la più calda, e quando viene trovata la più calda si svuota 
                res_idx, temp_res_idx = stack.pop()
                result[res_idx] = i - res_idx

            stack.append((i, t)) # conservo l'indice corrente e la temperatura


        return result