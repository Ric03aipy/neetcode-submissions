class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        freq = {}
        idxs = {}
        for i, n in enumerate(nums): 
            freq[n] = freq.get(n, 0) + 1
            idxs[n] = i
        for i, n in enumerate(nums): 
            diff = target - n
            # checking for repeated values
            if diff == n:
                if freq[n] > 1: return sorted([i, idxs[diff]])
                # else do nothing
            else: 
                j = idxs.get(diff, 0)
                if j != 0: return sorted([i, j])
            

        return []

        

        


        

         
