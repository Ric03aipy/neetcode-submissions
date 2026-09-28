class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # ===============
        # ripetizione #4
        # ===============

        # Semplifico la logica facendo in modo che la lunghezza di nums1 sia sempre minore di nums2 quando non sono uguali
        # Voglio fare ricerca binaria sul più piccolo
        if len(nums1) > len(nums2): return self.findMedianSortedArrays(nums2, nums1)

        m, n = len(nums1), len(nums2) # Qui sono sicuro che m < n

        # Chiamo MERGE l'array ideale ottenuto per merge sort
        # Se divido MERGE in 2 metà se sono pari hanno la stessa dimensione, se sono dispari, supponiamo che la metà sinistra
        # abbia un elemento in più. L'ultimo elemento di questa metà sinistra sarà la mediana. 

        # half è il numero di elementi della parte sinistra di MERGE
        # Se so che m < n allora al più half è n; half \in [0, n] 
        half = (m + n + 1) // 2 # es. 3 + 4 -> mediana [3]; divisone [1,2,3,4 | 5,6,7] 

        # Ricerca binaria sul numero di elementi di nums1 che sono nella parte sinistra di MERGE
        left, right = 0, m


        while left <= right: 
            mid = left + (right - left) // 2
            # Necessariamente allora half - mid sono gli elementi di nums2 che sono nella parte sinistra di MERGE

            l1 = nums1[mid - 1] if mid > 0 else float("-inf")
            l2 = nums2[half - mid - 1] if half - mid > 0 else float("-inf")
            r1 = nums1[mid] if mid < m else float("inf")
            r2 = nums2[half - mid] if half - mid < n else float("inf")

            # Condizione di successo 
            if l1 <= r2 and l2 <= r1: 
                # Pari
                if (n + m) % 2 == 0: 
                    return (max(l1, l2) + min(r1, r2)) / 2.0
                # Dispari
                else: 
                    return float(max(l1, l2))

            # Cerco un altro indice
            
            # Se l1 > r2 devo muovere il taglio a sinistra
            if l1 > r2: right = mid - 1
            else: left = mid + 1

        