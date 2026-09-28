class MedianFinder:

    # ==============
    # ripetizione #1
    # ==============

    import heapq

    def __init__(self):
        # Inizializzo due array che rappresentano le 2 metà dello stream ordinato
        self.left = []  # MaxHeap
        self.right = [] # MinHeap

    def addNum(self, num: int) -> None: 
        # Aggiungo alla cieca a sinistra: è un MaxHeap, quindi negativo
        heapq.heappush(self.left, -num)
        # Travaso il massimo di sinistra sempre
        heapq.heappush(self.right, -heapq.heappop(self.left))
        # Assumendo che per merge di dimensione dispari right sia di 1 più grande, trabocco se è di 2 più grande di left
        if len(self.right) == len(self.left) + 2: 
            heapq.heappush(self.left, -heapq.heappop(self.right))

    def findMedian(self) -> float:
        # Totale PARI significa che devono avere per forza dimensione uguale per vincolo di costruzione in addNum
        if (len(self.left) + len(self.right)) % 2 == 0: 
            return (-self.left[0] + self.right[0]) / 2.0
        else: 
            return float(self.right[0])
        
        