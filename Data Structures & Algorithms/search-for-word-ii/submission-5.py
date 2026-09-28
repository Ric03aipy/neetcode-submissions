"""
QUESTA è LA SOLUZIONE DA Competitive Programming puro: 
- modifico la struttura senza pensare al riutilizzo
- 
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
        def dfs(r: int, c: int, curr: TrieNode): 

            # Condizione di successo 
            if curr.word: res.add(curr.word)

            # Condizione di uscita - oob griglia, ripetizione celle, inconsistenza con il trie -  
            if r < 0 or r >= m or c < 0 or c >= n: return 
            if board[r][c] == "#": return 
            char = board[r][c]
            if char not in curr.children: return 

            board[r][c] = "#" # Questo rompe tutti i percorsi, quindi di fatti sostituisce path (set) - ma modifica l'input !

            dfs(r + 1, c, curr.children[char])
            dfs(r - 1, c, curr.children[char])
            dfs(r, c + 1, curr.children[char])
            dfs(r, c - 1, curr.children[char])

            board[r][c] = char # Ripristino anche con questa soluzione - la logica "template" resta



        # Il punto di partenza del backtracking deve essere una cella qualunque
        for i in range(m):
            for j in range(n): 
                dfs(i, j, trie.root)

        return list(res)








