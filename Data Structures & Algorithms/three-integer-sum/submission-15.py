class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # ===============
        # ripetizione #2
        # ===============

        nums.sort() # O(1) in space, O(nlogn) in time
        res = []

        i = 0 
        L = len(nums)
        while i < L: 
            while 0 < i < L and nums[i] == nums[i-1]: i += 1
            j = i + 1
            k = L - 1
            while j < k: 
                s = nums[i] + nums[j] + nums[k]
                if s == 0: 
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    while j < k and nums[j] == nums[j-1]: j += 1
                elif s > 0: k -= 1
                else: j += 1
            i += 1
        return res