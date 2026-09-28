class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        # Ordiniamo in-place per avere spazio O(1)
        nums.sort() 
        
        # 1. FISSIAMO IL PRIMO ELEMENTO (i)
        for i in range(len(nums)):
            
            # SALTO DUPLICATI ESTERNO
            # Se i > 0 (non siamo al primo giro) e il numero attuale è uguale al precedente,
            # abbiamo già calcolato tutte le triplette per questo numero. Saltiamolo!
            if i > 0 and nums[i] == nums[i - 1]:
                continue 
            
            # 2. TWO SUM II SUI RESTANTI ELEMENTI A DESTRA
            j = i + 1
            k = len(nums) - 1
            
            while j < k:
                # È più pulito calcolare la somma totale e confrontarla con 0
                s = nums[i] + nums[j] + nums[k]
                
                if s == 0:
                    # TRIS! Abbiamo trovato una combinazione
                    res.append([nums[i], nums[j], nums[k]])
                    
                    # SALTO DUPLICATI INTERNO
                    j += 1 # Spostiamo il puntatore sinistro per cercare altre soluzioni
                    
                    # Finché il nuovo 'j' è uguale a quello di prima, continuiamo a spostarlo
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                        
                    # (Domanda da colloquio: "Perché non sposti anche k e salti i suoi duplicati?"
                    # Risposta: "Non serve! Avendo cambiato j con un numero DIVERSO, al prossimo 
                    # giro la somma 's' non sarà più 0, quindi il codice sposterà j o k in automatico
                    # finendo negli if sottostanti.")
                    
                elif s > 0:
                    # Somma troppo grande, dobbiamo ridurla spostando il puntatore destro
                    k -= 1
                else:
                    # Somma troppo piccola, dobbiamo aumentarla spostando il puntatore sinistro
                    j += 1
                    
        return res