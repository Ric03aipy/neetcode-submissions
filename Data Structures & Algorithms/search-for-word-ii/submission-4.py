"""
QUESTA SOLUZIONE USA BENE IL TRIE. APPLICA UNA INEFFICIENZA IN MEMORIA PE FAVORIRE LA LEGGIBILITà. 
VEDI Solution 3 PER AVERE QUESTA STESSA SOLUZIONE MA RISPARMIANDO IL set() CHE INDIVIDUA LE RIPETIZIONI
"""


class TrieNode: 
    def __init__(self): 
        self.children = {}
        # INVECE DI SEGNALARE LA FINE DI UNA PAROLA...
        # self.is_end_of_word = False 
        # ...SEGNO LA PAROLA CHE FINISCE A QUESTO NODO...
        self.word = None

class Trie: 
    def __init__(self): 
        self.root = TrieNode()

    def addWord(self, word:str) -> None: 
        curr = self.root
        for char in word:
            if char not in curr.children: 
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.word = word

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        # Inizializzo la struttura
        trie = Trie()
        m, n = len(board), len(board[0])  # m righe, n colonne

        # Inserisco nel Trie tutte le parole da cercare 
        for word in words: 
            trie.addWord(word)

        res = set() # Elimino in partenza i duplicati

        # Backtracking su griglia
        def dfs(path: set, r: int, c: int, curr: TrieNode): 

            # Condizione di successo 
            if curr.word: res.add(curr.word)

            # Condizione di uscita - oob griglia, ripetizione celle, inconsistenza con il trie -  
            if r < 0 or r >= m or c < 0 or c >= n: return 
            if (r, c) in path: return 
            char = board[r][c]
            if char not in curr.children: return 

            path.add((r, c))

            dfs(path, r + 1, c, curr.children[char])
            dfs(path, r - 1, c, curr.children[char])
            dfs(path, r, c + 1, curr.children[char])
            dfs(path, r, c - 1, curr.children[char])

            path.remove((r, c))



        # Il punto di partenza del backtracking deve essere una cella qualunque
        for i in range(m):
            for j in range(n): 
                dfs(set(), i, j, trie.root)

        return list(res)








