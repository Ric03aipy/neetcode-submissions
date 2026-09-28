class Solution:

    def myPow(self, x: float, n: int) -> float:
        # divide & conquer + memoization: l'idea è sfruttare la proprietà del prodotto di potenze: a^b * a^c = a^(b + c)

        mem = {0:1, 1:x, -1:1/x} # esponente - valore

        # Ausiliaria per sfruttare la memoization 
        def myPowAux(x, n): 

            # Casi base assorbiti dall'inizializzazione della memoria
            # if n == 0: return 1
            # if n == 1: return x

            if n in mem: return mem[n]

            left_half = myPowAux(x, int(n / 2))
            mem[int(n / 2)] = left_half
            right_half = myPowAux(x, n - int(n / 2))
            mem[n - int(n / 2)] = right_half
            
            return left_half * right_half

        return myPowAux(x, n)


        