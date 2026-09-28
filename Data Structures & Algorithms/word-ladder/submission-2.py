class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        from collections import deque

        # Variabili strettamente necessarie per la mia logica
        q = deque()
        q.append((beginWord, 1))
        alphabet = [chr(i) for i in range(ord('a'), ord('z') + 1)]
        # visited = set() INVECE DI MARCARE LE PAROLE TROVATE, ELIMINALE DALLA LISTA TRA QUELLE DA CERCARE

        # Variabili ausiliarie
        n = len(wordList) + 2       # numero totale di parole
        m = len(beginWord)          # lunghezza delle parole
        wordList = set(wordList)    # non perdo informazione perché mi è detto esplicitamente che sono tutte parole distinte

        # BFS: preferisco in questo caso perché mi permette di ritornare la sequenza più breve senza tracciare la profondità
        while q: # O(n)
            curr_word, curr_seq_len = q.popleft()
            # Test di validità subito
            if curr_word == endWord: return curr_seq_len
            
            # Provo a sostituire una lettera alla volta
            for idx, char in enumerate(curr_word): # O(m)
                for letter in alphabet: # O(26)
                    test_word = curr_word[:idx] + letter + (curr_word[idx+1:] if idx != m - 1 else "") # O(m)
                    if test_word in wordList: # O(1) dopo essere diventata un set; sarebbe stata O(n*m) con lista perché con hash set confronta gli hash, con lista avrebbe fatto il confronto tra stringhe che costa il minimo della lunghezza, che in questo caso è la stessa per entrambe le stringhe comparate, m
                    # Devo anche scartare la possibilità di tornare indietro es cat->bat->cat quindi uso un set visited
                        q.append((test_word, curr_seq_len + 1))
                        wordList.remove(test_word)

        # Se la BFS ha fallito vuol dire che non esiste alcun percorso che porta a endWord
        return 0



"""
from collections import deque

        # Variabili strettamente necessarie per la mia logica
        q = deque()
        q.append((beginWord, 1))
        alphabet = [chr(i) for i in range(ord('a'), ord('z') + 1)]
        visited = set()

        # Variabili ausiliarie
        n = len(wordList) + 2       # numero totale di parole
        m = len(beginWord)          # lunghezza delle parole
        wordList = set(wordList)    # non perdo informazione perché mi è detto esplicitamente che sono tutte parole distinte

        # BFS: preferisco in questo caso perché mi permette di ritornare la sequenza più breve senza tracciare la profondità
        while q: # O(n)
            curr_word, curr_seq_len = q.popleft()
            # Test di validità subito
            if curr_word == endWord: return curr_seq_len
            # MARCARE SUBITO PER EVITARE DI METTERE DUPLICATI IN CODA
            visited.add(curr_word)
            # Provo a sostituire una lettera alla volta
            for idx, char in enumerate(curr_word): # O(m)
                for letter in alphabet: # O(26)
                    test_word = curr_word[:idx] + letter + (curr_word[idx+1:] if idx != m - 1 else "")
                    if test_word in wordList and test_word not in visited: # O(n) dopo essere diventata un set; sarebbe stata O(n*m) con lista perché con hash set confronta gli hash, con lista avrebbe fatto il confronto tra stringhe che costa il minimo della lunghezza, che in questo caso è la stessa per entrambe le stringhe comparate, m
                    # Devo anche scartare la possibilità di tornare indietro es cat->bat->cat quindi uso un set visited
                        q.append((test_word, curr_seq_len + 1))

        # Se la BFS ha fallito vuol dire che non esiste alcun percorso che porta a endWord
        return 0

"""