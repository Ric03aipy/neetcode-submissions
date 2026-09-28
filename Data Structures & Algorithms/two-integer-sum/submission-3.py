class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {x: idx for idx, x in enumerate(nums)} 
        idxs = []
        for i in range(len(nums)): 
            diff = target - nums[i]
            if diff in d and i != d[diff]: 
                return [i, d[diff]]
        return []
        

        


        

         
