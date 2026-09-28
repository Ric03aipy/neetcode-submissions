class Node: 
    def __init__(self): 
        self.children = {}
        self.eow = False # end of word

class WordDictionary:
    # ==============
    # ripetizione #1
    # ==============

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        curr = self.root
        for char in word: 
            if char not in curr.children: 
                curr.children[char] = Node()
            curr = curr.children[char]
        curr.eow = True

    def search(self, word: str) -> bool:
        
        def dfs(curr: Node, word_idx:int) -> bool:

            if word_idx == len(word): return curr.eow
            
            if word[word_idx] == ".": 
                for child in curr.children: 
                    if dfs(curr.children[child], word_idx + 1): return True
                return False
            else: 
                if word[word_idx] not in curr.children: return False
                return dfs(curr.children[word[word_idx]], word_idx + 1)
        


        curr = self.root
        return dfs(curr, 0)


