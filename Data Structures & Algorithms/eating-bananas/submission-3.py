class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # 1) l'idea è quella dei raddoppi: se 1 all'ora non da un tot <= h allora provo 2 poi 4 poi 8
        # poi si può fare bin search tra il primo che soddisfa e l'ultimo che non soddisfa

        # 2) un altra idea è quella di usare come "right" il massimo di piles: se posso esaurire al più 1 bidone all'pra indipendentemente dal rate, allora sicuramente non possono chiedemi meno di len(piles) ore
        # e performare binsearch poi da 1 a right

        # la strada 2 sembra molto intuitiva da implementare

        # una nota sulla complessità: O(nlogm) è un prodotto, ciò significa che non è rilevante chi sia il ciclo interno e chi quello esterno purché la logica sia ciclo lineare su piles e logaritmico sul massimo valore in piles. Anche se la lettura può ingannare - viene prima n - non è detto che venga prima il ciclo su piles

        right = max(piles)  # tasso massimo per k - nel caso peggiore mid collassa su right
        left = 1            # tasso minimo per k
        last_good_candidate = None
        while left <= right: 
            
            mid = left + (right - left) // 2 # tasso da testare

            # controllo se k è sufficiente
            time = 0
            for pile in piles: 
                time += -(-pile // mid) # ceil senza importare math: // arrotonda fa floor, sui negativi signfica più negativo, poi ricambio il segno; invece per // precisa è solo un doppio cambio di segno ininfluente (letto da StackOverflow, molto figo come trucco)
            if time <= h: # se < vuol dire che è più veloce del dovuto, quindi successo comunque 
                last_good_candidate = mid
                right = mid - 1    # se è più grande del target, voglio andare più veloce

            else: 
                left = mid + 1 # se è più grande del target, voglio andare più veloce, questo è insuccesso

        return last_good_candidate




        