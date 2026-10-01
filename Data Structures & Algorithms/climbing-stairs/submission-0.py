class Solution:
    def climbStairs(self, n: int) -> int:
        
        # Carta e penna... -> dp[i] definito come dp[i] = # combinazioni per arrivare ad altezza i 
        # Cosa ho notato in termini di ricorrenza facendo a mano dp[1,2,3,4]: dp[i] = dp[i-1] + dp[i-2]

        if n <= 2: return n

        # Casi base
        dp = [0] * (n+1)
        dp[1] = 1
        dp[2] = 2

        # Loop | Tabulation
        for i in range(3, n+1): dp[i] = dp[i-1] + dp[i-2]

        return dp[-1]