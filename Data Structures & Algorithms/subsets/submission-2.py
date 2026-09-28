class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # =======================
        # ripetizione #1
        # =======================

        res = [] 

        def dfs(current_path, start_idx):
            
            # ogni percorso è un sottoinsieme valido
            res.append(current_path[:])

            # per ongi elemento posso fare la scelta oppure no
            for i in range(start_idx, len(nums)): 
                # faccio la scelta
                current_path.append(nums[i])
                # ricorsione
                dfs(current_path, i + 1)
                # non faccio la scelta - e ne faccio un altra poi
                current_path.pop()

        dfs([], 0)

        return res