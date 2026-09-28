class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        idxs = {}
        for i, n in enumerate(nums): 
            diff = target - n 
            if diff in idxs: 
                return [idxs[diff],i]
            idxs[n] = i
        return []

        

        


        

         
