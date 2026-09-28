class Solution:

    def myPow(self, x: float, n: int) -> float:
        # divide & conquer: l'idea è sfruttare la proprietà del prodotto di potenze: a^b * a^c = a^(b + c)
        # Resa però smart: le due metà sono identiche nel caso pari e nel caso dispari manca un solo prodotto

        # Casi base 
        if n == 0: return 1
        if n == 1: return x
        if n < 0: 
            # Tolgo di mezzo il segno meno sfruttando la proprieta della potenza di potenza
            n = -n 
            x = 1 / x

        # Una quasi metà a dire il vero: è metà esatta se n è pari altrimenti hai una metà che è più piccola (es. 15 = 7+7+1)
        half = self.myPow(x, int(n / 2)) # int(n / 2) arrotonda per essere sempre più vicina allo zero

        return half * half if n % 2 == 0 else half * half * x



        