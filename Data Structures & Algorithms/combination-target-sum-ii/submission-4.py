class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        # Nel template base con (i+1) se fossero tutti elementi distinti nell'array di partenza non avremmo possibilità
        # di avere duplicati, in quanto lo stesso elemento viene saltato con (i+1) (mentre preso un numero arbitrario di
        # volte se (i)).
        # Qui però candidates ha dei duplicati, quindi non importa se faccio (i+1). Ad un certo (i+k) potrebbe ripetersi
        # un valore già visto e avere la stessa lista. 
        # Una soluzione potrebbe essere
        # 1) ordino - costo nlogn, non viene preso in considerazione in un algoritmo con costo esponenziale come quelli 
        # che coinvolgono l'esplorazione di un albero di decisione
        # 2) salto tutti i numeri uguali ai precedenti (condizione di non validità) a patto di aver visto ogni indice 
        # una volta 
        # Devo però mantenere soluzioni come [2,2,4] in cui i doppioni sono elementi con indice diverso nell'array di input

        res = []
        candidates.sort()

        def backtrack(current_path, start_idx, remain): 
        
            if remain == 0: 
                res.append(current_path[:])
                return 

            for i in range(start_idx, len(candidates)): 

                if remain < 0: break
                
                if i > start_idx and candidates[i] == candidates[i-1]: continue 

                current_path.append(candidates[i])

                backtrack(current_path, i + 1, remain - candidates[i])

                current_path.pop()
            
        backtrack([], 0, target)
        return res