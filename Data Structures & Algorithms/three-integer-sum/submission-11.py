class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sorting in place - O(nlogn) in time, O(1) in space
        nums.sort() 

        res = []
        for i in range(len(nums)): 
            # skip duplicate: exploit sorting
            if i > 0 and nums[i] == nums[i-1]: continue
            k = i + 1
            j = len(nums) - 1
            # the problem is now reduced to 'Two sum II' with target (-nums[i])
            while k < j: 
                state = nums[i] + nums[j] + nums[k] 
                if state == 0: 
                    res.append([nums[i], nums[j], nums[k]])
                    while k < j and nums[k] == nums[k+1]: k+= 1 
                        
                if state > 0: j -= 1
                else: k += 1
        return res



