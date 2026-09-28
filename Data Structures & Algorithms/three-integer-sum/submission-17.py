class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # ===============
        # ripetizione #3
        # ===============

        nums.sort()
        res = []
        for i in range(len(nums)): 
            if i > 0 and nums[i] == nums[i-1]: continue
            j = i + 1
            k = len(nums) - 1
            while j < k: 
                if nums[i] + nums[j] + nums[k] == 0: 
                    res.append([nums[i], nums[j], nums[k]])
                    while j < k and nums[j+1] == nums[j]: 
                        j += 1
                if nums[i] + nums[j] + nums[k] > 0: 
                    k -= 1
                else: # se è uguale a 0 comunque un passetto va fatto altrimenti si va in loop infinito
                    j += 1
        return res