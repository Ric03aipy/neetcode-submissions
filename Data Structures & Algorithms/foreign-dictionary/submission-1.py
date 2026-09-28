class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        

        # L'idea è che un ordine lessicografico sia una lista
        # Quindi bisogna trovare un ordinamento topologico del grafo delle relazioni 
        # Ogni arco è una relazione tipo x < y cioè x viene prima di y nell'ordine lessicografico

        # Pulce nell'orecchio da HINT 1 (visto solo questo); ma non mi ha spiegato bene perché; la mia intuizione è questa:
        # Mi serve davvero controllare per la parola 1 le relazioni con la parola 4, 5, n? 
        # O posso sfruttrae la transitività per cui se comparo parola 1 e 2, parola 2 e 3 allora so che le relazioni
        # che scovo da 2-3 mi danno qualcosa anche per 1-3, anche se non esplicitamente? 
        # Questo abbasserebbe drasticamente il costo computazionale a una sola passata sulle stringhe, di costo
        # O(n * max([len(word) for word in words]) che comunque è meglio di avere un fattore n^2 lì. 


        # Stati per un ordinamento topologico
        UNEXPLORED, EXPLORING, EXPLORED = 0, 1, 2

        # Costruzione della lista di adiacenza 
        adj_list = {c:[] for word in words for c in word}
        state = [UNEXPLORED] * 26

        n = len(words)
        for i in range(n-1): # Fino a n-1 così [i+1] è sempre valido 
            w1, w2 = words[i], words[i+1]    
            min_len = min(len(w1), len(w2))
            
            # Condizione di uscita immediata: contraddizione interna al vocabolario: risolve ["abc","ab"]
            if len(w1) > len(w2) and w1[:min_len] == w2[:min_len]: return ""
            
            for j in range(min_len):
                c1, c2 = w1[j], w2[j]
                if c1 != c2: 
                    adj_list[c1].append(c2)
                    # Solo la prima differenza è rilevante
                    break

        # Ordinamento topologico: stati + dfs + inversione della lista se non ci sono cicli
        res = []
        def dfs(node): 
            if state[ord(node) - ord('a')] == EXPLORED: return True
            # Cycle detection
            if state[ord(node) - ord('a')] == EXPLORING: return False

            state[ord(node) - ord('a')] = EXPLORING
            for child in adj_list[node]:
                if not dfs(child): return False
                
            state[ord(node) - ord('a')] = EXPLORED
            res.append(node)
            return True

        for node in adj_list:
            if state[ord(node) - ord('a')] == UNEXPLORED:
                if not dfs(node): return ""


        return "".join(res[::-1]) 






