class TrieNode:
    def __init__(self):
        self.children = {} 
        self.is_end_of_word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for char in word: 
            if char not in curr.children: 
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.is_end_of_word = True

    def search(self, word: str) -> bool:

        # Il ciclo lineare visto nell'esercizio precedente (Trie base con caratteri senza significato particolare)
        # non va bene se mi dici "'.' può essere quaunque lettera". 
        # A questo punto quando vedo '.' devo far partire tante ricerche "in parallelo" (sintomo di ricorsione)
        # quante sono le lettere che ho in un certo nodo. 
        # La ricorsione in stile backtracking, che prevede di ritirare la mossa mi fa potare la ricerca appena mi accorgo 
        # di essere in un percorso sbagliato (lettera cercata non figlia di quella correntemente esplorata nella struttura). 
        # In questo assomiglia al problema "word search" della sezione backtracking. 
        # Bisogna però includere anche i casi base in cui la lettera è effettiva e non è '.'. In questo caso la 
        # dfs non esplora molti percorsi ma ne seleziona esattamente 1. Se word non contiene '.' sarà lineare, solo in una
        # maniera di scrittura fancy (dfs). 

        def dfs(idx, curr) -> bool: 
            """
            idx: indice della lettera di word che sta venendo cercata
            curr: TrieNode correntemente in esplorazione
            """
            
            # Condizione di successo
            if idx == len(word): return curr.is_end_of_word

            if word[idx] != ".":
                # Pruning
                if word[idx] not in curr.children: return False
                # Chiamata lineare
                return dfs(idx + 1, curr.children[word[idx]])
            
            for letter in curr.children: 
                if dfs(idx + 1, curr.children[letter]): return True

            return False

        res = dfs(0, self.root)
        return res
        
            






