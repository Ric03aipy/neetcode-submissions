class Solution:
    def rob(self, nums: List[int]) -> int:
        
        # Deinisco stato dp[i] = bottino ottenuto alla casa i
        # Hn - casa n
        # dp[0] = 0 - casa finta, non esiste 
        # dp[1] = 0 or H1 
        # dp[2] = 0 or H2
        # dp[3] = dp[1] + H3 or dp[2]
        # dp[4] = dp[2] + H4 or dp[3]
        # dp[i] = max(dp[i-2] + nums[i-1], dp[i-1])

        # Caso base
        if len(nums) <= 2: return max(nums)
        n = len(nums)

        # Inizializzazione struttura
        dp = [0] * (n + 1)
        # Ciclo
        for i in range(1, n + 1): 
            dp[i] = max(dp[i-2] + nums[i-1], dp[i-1])
            print(dp)

        return dp[-1]