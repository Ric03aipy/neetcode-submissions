class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums) # O(nlogn)
        if nums[0] > 0: return [] # just to speed up trivial case
        # print(nums)
        n = len(nums)
        res = []
        for k in range(n-2): 
            if k > 0 and nums[k] == nums[k-1]: 
                continue     
            i = k + 1       
            j = n - 1
            while i < j: 
                if nums[i] + nums[j] + nums[k] == 0:
                    res.append([nums[i], nums[j], nums[k]])
                    # LOGIC: move both i and j inward, skipping over any values that are the same as the ones you just used.
                    prec_i = nums[i]
                    prec_j = nums[j]
                    while i < n and nums[i] == prec_i: i += 1
                    while j > 0 and nums[j] == prec_j: j -= 1
                elif nums[i] + nums[j] + nums[k] > 0: j-=1
                else: i+=1

        return res
            
                
                

        