class TrieNode: 
    def __init__(self): 
        self.children = {}  # {carattere: nodo}
        self.is_end_of_word = False # Serve come stop

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:

        # Parto sempre dalla radice (vuota - come se fosse un dummy node di appoggio)
        curr = self.root

        for char in word: 
            # Se non posso scendere nell'albero allora creo un nuovo branch
            if not char in curr.children: 
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        
        # Termine della parola così posso ricercarla non come prefisso ma come parola vera e propria
        curr.is_end_of_word = True


    def search(self, word: str) -> bool:
        
        # Parto sempre dalla radice (vuota - come se fosse un dummy node di appoggio)
        curr = self.root

        for char in word: 
            # Se non esiste la sequenza allora non l'ho mai vista
            if char not in curr.children: return False
            curr = curr.children[char]

        # Controllo se la parola cercata è nell'albero come prefisso o come parola effettiva
        return curr.is_end_of_word

    def startsWith(self, prefix: str) -> bool: # Come search ma non mi interessa se sia una parola effettiva

        # Parto sempre dalla radice (vuota - come se fosse un dummy node di appoggio)
        curr = self.root

        for char in prefix: 
            # Se non esiste la sequenza allora non l'ho mai vista
            if char not in curr.children: return False
            curr = curr.children[char]

        # La parola cercata è nell'albero 
        return True
        
        