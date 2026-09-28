class Solution:
    def trap(self, height: List[int]) -> int:
        area = 0
        # maximum height seen
        max_l = 0  
        max_r = 0
        # two ptrs
        i = 0
        j = len(height) - 1
        while i < j:
            # l'idea è quella di contare solo l'acqua sopra una certa colonna: 
            # vedo: 
            # 1) quale è il massimo a sinistra/destra e dove si trova il puntatore
            # 2) se la differenza di altezze è positiva vuol dire che quel massimo mi permette di inserire acqua
            # 3) se la differenza è negativa vuol dire che sono su un altro bordo del contenitore 
            #   (es. se sei in posizione [3] della figura a sinistra allora la somma sarà 2-3=-1): non hai acqua da 
            #   contare su questa colonna e il bacino che si è formato (posizione [2]) l'hai già contata nelle iterazioni
            #   precedenti
            # I due puntatori sono essenziali per tracciare i cambiamenti minimi: non puoi muoverti solo con uno perché
            # avresti problemi con l'orizzonte, se devi annullare qualcosa, e non ti basta un flag perché potresi sovrastimare
            # l'altezza di una colonna (es. [5, 1, 3, 0, 2])
            l = height[i]
            r = height[j]
            area_l = max_l - l
            area_r = max_r - r
            if area_l > 0: area += area_l
            else: max_l = l
            if area_r > 0: area += area_r
            else: max_r = r
            if max_l < max_r: i += 1
            else: j -= 1
        return area


