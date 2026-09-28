class MedianFinder:

    """
    Nell'altro esercizio sulla mediana dividavamo ripetutamente l'array per cercare la divisione giusta (binary search)
    ed avere i 4 valori attorno all'indice di divisone. Poi se il numero di elementi era pari o dispari e la condizione 
    di avere gli estremi sx <= degli estremi destri avevamo finito. 
    """

    """
    Un'idea analoga potrebbe essere quella di dividere in 2 heap: se la lunghezza in un certo momento dello stream è n, metà
    è n // 2, arrotondata per difetto. Definiamo la metà "sinistra" di n // 2 elementi e "destra" dei rimanenti.
    Quindi se n è dispari, (n // 2 < n - n // 2) ovverò la metà sinistra avrà 1 elemento in meno di quella destra e quindi 
    il più piccolo della metà destra è la mediana. L'estrazione del più piccolo è O(1) per un MinHeap. Il costo è lo stesso
    se n è pari: devo peekare la cima di entrambi gli heap e fare la loro media. Attenzione però che uno la metà 
    destra è un MinHeap, quella sinistra è un MaxHeap. 

    Il problema quindi diventa: quale è il criterio per piazzare elementi in uno o nell'altro heap? 

    Suppongo di congerlare un array: [3,4,6,8,1] -> mediana = ? -> sort -> [1,3,4,6,8] -> mediana = 4
    Io leggo i numeri in ordine. I primi 2, non avendo informazioni ulteriori diventano le teste: Mheap=[3], mheap=[4]. 
    
    Leggo 6; se per ora io so che le info sulla mediana sono date da [3,4] posso sapere solo che 6 finisce a destra. 
    Se finisce a destra: [3,4,6] allora la mediana si sposta a destra. Quindi lo devo inserire in mheap=[4,6]
    
    Leggo 8; come per 6 anche questo nella lista ordinata dovrebbe finire a destra: mheap=[4,6,8]; a questo punto però
    la mediana non è più considerabile come la media delle teste. Dipende da chi ha più elementi. Non facciamo ipotesi di 
    bilanciamento. Nel caso peggiore mi viene fuori una lista di 1 elemento e una di n-1 elementi. Ma a quel punto come
    trovo la mediana? 
    Facciamo invece l'ipotesi di bilanciamento. Come bilancio? Posso prendere il minimo della metà destra e buttarlo 
    nella metà sinistra. In questo modo la differenza deve rimanere di al più 1 elemento. Quindi bilancio in 
    [4,3] (4 prima visto che è Maxheap), [6,8]

    Leggo 1; questo è minore di 3 quindi finisce a sinistra; [4,3,1], [6,8]

    Questa strada ha senso; provo a implementarla. 
    """


    import heapq

    def __init__(self):
        self.minheap = []   # metà dei valori più grandi 
        self.maxheap = []   # metà dei valori più piccoli - tutte le operazioni qui devono INVERTIRE il SEGNO
        self.n = 0

    def addNum(self, num: int) -> None:
        # L'inserimento dei primi due vogliamo che sia logicamente corretto 
        if not self.minheap: 
            self.minheap.append(num)
            return 
        if not self.maxheap:
            if num < self.minheap[0]:
                self.maxheap.append(-num)
            else: 
                el = self.minheap.pop()
                self.maxheap.append(-el)
                self.minheap.append(num)
            return 

        # Inserisco vedendo la testa delle strutture
        if num < self.maxheap[0]: 
            heapq.heappush(self.maxheap, -num)
        else: 
            heapq.heappush(self.minheap, num)
        self.n += 1

        # Aggiustamento della logica
        while self.minheap and self.minheap[0] < -self.maxheap[0]: 
            el = heapq.heappop(self.minheap)
            heapq.heappush(self.maxheap, -el)

        # Mantenimento del bilanciamento (se le lunghezze non sono uguali)
        while len(self.maxheap) > len(self.minheap): 
            el = -heapq.heappop(self.maxheap)
            heapq.heappush(self.minheap, el)
        # In questo punto self.maxheap (sx) si trova con 1 elemento in meno di self.minheap (dx)
        while len(self.minheap) > len(self.maxheap) + 1: 
            el = heapq.heappop(self.minheap)
            heapq.heappush(self.maxheap, -el)
        # Qui continua ad essere self.maxheap (sx) con al più 1 elemento in meno di self.maxheap (dx)
    
        # print("post inserimento di", num)
        # print("left", self.maxheap)
        # print("right", self.minheap)

    def findMedian(self) -> float:
        # Chiamate base su numero di dati limite (0 o 1 elementi)
        if not self.minheap and not self.maxheap: return 0.0
        if not self.minheap: return self.maxheap[0]
        if not self.maxheap: return self.minheap[0]

        # Per costruizione se il numero di elementi è pari faccio la media delle teste.
        # Se sono dispari restituisco la testa della metà destra. 
        if self.n % 2 == 0: 
            return (self.minheap[0] + (-self.maxheap[0])) / 2
        else: 
            return self.minheap[0]
        
        