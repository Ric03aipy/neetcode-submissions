class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        import heapq
        from collections import deque 

        # ['A', 'A', 'A', 'B', 'C'] e n = 2. Il più difficile task da piazzaere è "A". 
        # A -> idle -> idle -> A -> idle -> idle -> A.
        # La priorità è LA FREQUENZA: serve un MaxHeap
        # Poiché la dimensione di tasks però mi cambia può essere utile avere un contatore di idle da spendere. 
        # Se il cooldown minimo è 2 e idle è 1 devo saltare un giro per avere idle = 2, se fosse 0 dovrei aspettare 2 turni

        # La chiave per validare questo approccio è questo NON-vincolo: "tasks may be completed in any order."

        # La dimenisone della struttura è un array di esattamente 26 caratteri --> O(1) space soddisfatto

        # Poiché il costo normalmente per un Heap a dimensione fissa è O(nlogk) ma k è 26 fisso allora è O(n) in time




        # Segno una frequenza negativa per avere un MaxHeap. Registro (frequenza, valore).
        # Mi serve ricordare anche il valore perché quando faccio heapify l'indice non mi aiuta più in quanto 
        # l'array viene riorganizzato
        arr = [[0, ""] for _ in range(26)] # TRAPPOLONE : [[0, ""]]*26 non è una copia profonda!!!
        for task in tasks:
            idx = ord(task) - ord("A") 
            arr[idx][0] -= 1 
            arr[idx][1] = task
        # per leggibilità e debug mi riduco gli elementi inutili: 
        arr = [el for el in arr if el[0] != 0]
        heapq.heapify(arr)

        # print(arr)
        # print()

        waiting_room = deque()
        global_time = 0

        while arr or waiting_room: # Finché non ho nessun processo congelato e nessuno da eseguire
            freq = val = None

            # Se nella sala d'attesa qualcuno ha finito il congelamento può rientrare
            if waiting_room and waiting_room[0][0] <= global_time: 
                _, f, v = waiting_room.popleft()
                heapq.heappush(arr, [f, v])

            # Che voglia terminare il processo o congelarlo comunque deve essere buttato fuori dai processabili
            if arr: freq, val = heapq.heappop(arr)

            # Prima aggiorno il tempo globale poi sommo n nella waiting room: il ciclo corrente di processamento 
            # non va incluso nel tempo di cooldown
            global_time += 1

            # Se non lo termino va in sala d'attesa - registro tempo di **S**congelamento, nuova frequenza, valore
            if freq and freq != -1: waiting_room.append([global_time + n, freq + 1, val])
            

            # print(arr)
            # print(waiting_room)
            # print(global_time)
            # print()
        
        return global_time




        


