class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        # Stato: dp[i] = costo minimo per andare oltre lo scalino i
        # Carta e penna e facendo prove su chi è dp[i] in relazione ai 2 valori prima
        # Relazione matematica scoperta: dp[i] = min(dp[i-2]+cost[i-2], dp[i-1], cost[i-1]) visto che devo
        # 1) essere allo scalino i-2 o i-1 e pagare il salto da quello scalino

        # Caso base, non gestito dall'array dp
        if (n := len(cost)) <= 2: return min(cost[0], cost[1])

        # Array 1-indexed per "visualizzazione" - così lo scalino 1 è all'indice 1; indice 0 quello "sprecato"
        dp = [0] * (n + 1) 
        # Per andare oltre scalino 1 e 2 non pago 
        for i in range(2, n + 1):
            dp[i] = min(dp[i-2]+cost[i-2], dp[i-1]+cost[i-1])
        
        # Cosa ritorno? Per come ho definito lo stato, l'ultimo elemento è il costo per saltare gli n scalini precedenti
        return dp[-1]
