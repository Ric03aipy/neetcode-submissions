# Definizione della struttura data per ricerca su vocabolario di parole in modo efficiente

class TrieNode: 
    def __init__(self, word=None): 
        self.children = {}
        self.word = word
    def __str__(self): 
        return str(self.children)

class Trie: 
    def __init__(self): 
        self.root = TrieNode()
        self.ptr = self.root
    
    def add(self, word:str):
        curr = self.root
        for c in word: 
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.word = word 

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        # Grandezze e strutture dati preliminari        
        ROWS, COLS = len(board), len(board[0])
        vocab = Trie()
        for word in words: vocab.add(word)
        res = []

        def dfs(r, c, curr): 

            if r < 0 or c < 0 or r >= ROWS or c >= COLS or board[r][c] == "#": return 
        
            char = board[r][c]
            board[r][c] = "#" # Marco come esplorato 
            if char not in curr.children:
                board[r][c] = char
                return 
            if curr.children[char].word: 
                res.append(curr.children[char].word)
                curr.children[char].word = None
            dfs(r + 1, c, curr.children[char]) 
            dfs(r - 1, c, curr.children[char]) 
            dfs(r, c + 1, curr.children[char]) 
            dfs(r, c - 1, curr.children[char])
            board[r][c] = char
            
        for i in range(ROWS):
            for j in range(COLS): 
                dfs(i, j, vocab.root)
            
        return res




