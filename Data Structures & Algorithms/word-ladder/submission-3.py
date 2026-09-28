class Solution:

    """
    SOLUZIONE STANDARD CON WILDCARDS (jolly). 
    
    IDEA: 
    Una parola come "cat" ha 3 stati intermedi: "*at", "c*t", e "ca*".
    Se anche "bat" esiste nel dizionario, condividerà lo stato "*at".
    Invece di provare l'alfabeto, pre-calcoliamo un grafo raggruppando le parole in base ai loro Jolly.

    """

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        # Ottimizzazione per uscita rapida
        if endWord not in wordList: return 0

        from collections import defaultdict, deque

        # Il grafo che costruisco è del tipo {pattern: [lista parole che rispettano il pattern]} es. {*at: [cat, bat, sat]}
        adj_list = defaultdict(list)
        for word in wordList: 
            for j in range(len(word)): 
                pattern = word[:j] + "*" + word[j+1: ]
                adj_list[pattern].append(word)

        # Inizializzo la coda con l'idea di immagazzinare anche l'informazione sul numero di parole viste
        q = deque([(beginWord, 1)])

        # Set dei nodi visti
        visited = set()
        wordList = set(wordList) # Visto che le parole sono distinte rendo la ricerca più veloce

        # BFS 
        while q: 
            curr_word, step = q.popleft()
            
            # Controllo di successo 
            if curr_word == endWord: return step
            
            # Segno subito il nodo come visitato per evitare duplicati in coda
            visited.add(curr_word)

            # I vicini della parola estratta sono tutti quelli che condividono uno dei possibili pattern
            for i in range(len(curr_word)): 
                pattern = curr_word[:i] + "*" + curr_word[i+1:]
                for neighbor in adj_list[pattern]: 
                    if neighbor not in visited: 
                        q.append((neighbor, step + 1))



        # La parola c'è nella lista data ma non è raggiungibile
        return 0
