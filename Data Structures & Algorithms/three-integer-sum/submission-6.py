class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        # sort - O(nlogn)
        nums = sorted(nums)
        l = len(nums)
        i = 0 
        while i < l: 
            j = i + 1
            k = l - 1
            while j < k: 
                s = nums[j] + nums[k]
                if s == -nums[i]: 
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    while j < k and nums[j] == nums[j - 1]: j += 1
                elif s > -nums[i]: k -= 1
                else: j += 1 
            while i+1 < len(nums) and nums[i+1]==nums[i]: i += 1
            i += 1
        return res