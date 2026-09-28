class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        def is_palindrome(s: str) -> bool: 
            half = len(s) // 2
            for i in range(half): 
                if s[i] != s[len(s) - i - 1]: 
                    return False
            return True

        # Qui devo tagliare a ogni carattere che mi permette di dire "tutto ciò che sta prima di questo taglio è palindromo"
        # s = "aab"
        # Taglio a i=0: s[:i+1] = "a" e taglio a i=0, "a" è sicuramente palindroma. Devo verificare ciò che viene dopo. 
        # Chiamata ricorsiva su "ab". Taglio di nuovo 1 lettera: "a" che è palindorma. Devo verificare ciò che viene dopo.
        # Chiamata ricorsiva su "b". Taglio dopo 1 letterea: "b" è palindroma. Dopo non c'è niente. (Un ciclo che non inizia)
        # Taglio a i=1, s[:i+1] = "aa", è palindroma, devo vedere ciò che sta dopo. 
        # Chiamata ricorsiva su "b". Taglio dopo 1 letterea: "b" è palindroma. Dopo non c'è niente. (Un ciclo che non inizia)
        # Il path è composto da [a, a, b] oppure da [aa, b], res deve prendere un path completo, quindi quando non c'è più resto. 
        # Taglio a i=2, s[:i+1] = "aab". Non è palindroma. Non va aggiunta al res. 

        res: List[List[str]] = []
        
        def dfs(path:List[str], cut_idx:int): 
            # Condizione di terminazione 
            if cut_idx == len(s): 
                res.append(path[:])
                return # non necessario esplicitare: il ciclo non partirebbe
            
            for i in range(cut_idx, len(s)): 
                # deve partire non dall'inizio ! s[: i+1] è tutto dall'inizio!
                current_string = s[cut_idx: i+1]   # si può ottimizzare scrivendo una funzione is_palindrome che prende un numero di posizioni dopo cui fermarsi ma non so neanche se l'approccio funziona, quidni non ha senso soffermarsi su questo dettaglio

                # Condizione di non-validità: non ha senso tagliare se so che a questo taglio va male
                if not is_palindrome(current_string): continue

                # Quello che **ho** (tempo passato) tagliato è palindromo
                path.append(current_string)

                # Passo ricorsivo
                dfs(path, i + 1)

                # Torno indietro e esploro un taglio più grande 
                path.pop()


        dfs([], 0)
        return res
