class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        # Tagliamo verticalmente i due array
        # [parte < | parte > ] rispetto alla mediana
        # [ , , , , | , , ] 
        #       [ , | , , , , , ] 
        # --> [left half | right half]
        # Se half è il numero di elementi, dove per convenzione se dispari left half ha 1 elemento in più
        # usando la formula (m + n + 1) // 2
        # Supponiamo che (i) elementi di nums1 vanno in left half, allora ne mancano (half - i) da nums2 
        # Come capire se il taglio è giusto? Osservo i 4 numeri a cavallo della linea.
        # Il target da cercare nella ricerca binaria è realizzare (L2 <= R1 and L1 <= R2)
        # (L1<=R1, L2<=R2 già verificate per sorting) 
        # La ricerca binaria si fa sull'indice i. 

        # TRAPPOLA 1: Vogliamo fare la ricerca binaria sull'array più piccolo.
        # Se nums1 è più grande, scambiamo i due array.
        # Questo garantisce che 'j' (elementi presi da nums2) non vada mai in negativo.
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)
        
        m, n = len(nums1), len(nums2)
        
        # Dimensione della metà di sinistra (con 1 elemento extra se dispari)
        half_len = (m + n + 1) // 2 
        
        # Ricerca binaria sul NUMERO DI ELEMENTI da prendere da nums1 (da 0 a m)
        left, right = 0, m
        
        while left <= right:
            # i = quanti elementi prendiamo da nums1
            # j = quanti elementi dobbiamo necessariamente prendere da nums2
            i = left + (right - left) // 2
            j = half_len - i
            
            # TRAPPOLA 2 & 3: Gli elementi ai bordi del taglio.
            # Se prendiamo 0 elementi, l'elemento a sinistra non esiste (float('-inf')).
            # Se prendiamo tutti gli elementi, l'elemento a destra non esiste (float('inf')).
            L1 = nums1[i - 1] if i > 0 else float('-inf')
            R1 = nums1[i] if i < m else float('inf')
            
            L2 = nums2[j - 1] if j > 0 else float('-inf')
            R2 = nums2[j] if j < n else float('inf')
            
            # CONTROLLO INCROCIATO: Abbiamo trovato il taglio perfetto?
            if L1 <= R2 and L2 <= R1:
                # BINGO!
                # Se la somma delle lunghezze è dispari, la mediana è il max della metà sinistra
                if (m + n) % 2 != 0:
                    return float(max(L1, L2))
                # Se è pari, la mediana è la media tra il max a sx e il min a dx
                else:
                    return (max(L1, L2) + min(R1, R2)) / 2.0
            
            # Se L1 > R2, abbiamo preso troppi elementi da nums1. Spostiamo il taglio a sinistra.
            elif L1 > R2:
                right = i - 1
            # Se L2 > R1, abbiamo preso pochi elementi da nums1. Spostiamo il taglio a destra.
            else:
                left = i + 1


