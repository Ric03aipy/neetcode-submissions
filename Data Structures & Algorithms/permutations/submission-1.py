class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # ===============
        # ripetizione #1
        # ===============

        res = []

        def dfs(current_path): 
            
            if len(current_path) == len(nums): 
                res.append(list(current_path))
                return

            for idx in range(len(nums)): 
                if nums[idx] in current_path: continue
                current_path.append(nums[idx])
                dfs(current_path)
                current_path.pop()

        dfs([])

        return res
