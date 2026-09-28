class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # ================
        # ripetizione #1
        # ================

        # [1,2,1]
        nums.sort()
        # [1,1,2] start = 0 -> [1], [1,1], [1,2], [1,1,2]
        # [1,1,2] start = 1 -> [1], [1, 2]
        res:List[List[int]] = []

        def dfs(path, start): 
            
            # Tutto ciò che entra è un sottoinsieme valido
            res.append(path[:])

            # Imposto il ciclo di subset senza duplicati
            for i in range(start, len(nums)):
                # if nums[start] == nums[i]: continue               # NO: salto la prima iterazione di ogni ciclo
                # if i > 0 and nums[start] == nums[i-1]: continue   # NO: non è diversa nella sostanza dalla precedente: prima o poi nums[i-1] raggiunge nums[i] della prima condizione creando una distorsione allos tesso modo
                # if i > 0 and nums[i] == nums[i-1]: continue        # NO: la condizione è troppo debole e fa saltare numeri vicini: [1,1,2] i primi [1,1] devono essere presi 1 volta, quindi per ogni ricorsione voglio prendere 1 volta esatta ogni sequenza di doppioni, in quanto una sequenza di k doppioni costituisce un sottoinsieme valido
                if i > start and nums[i] == nums[i-1]: continue
                path.append(nums[i])
                dfs(path, i + 1)
                path.pop()

        dfs([], 0)
        return res

