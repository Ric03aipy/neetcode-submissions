class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # O(n) in time, O(1) in space (results doens't count as auxiliary space !)
        l = len(nums)
        res = [1] * l
        for i in range(1, l): 
            res[i] = res[i-1] * nums[i-1]
        cumulative_b = 1
        for i in range(l-1, 0, -1):
            cumulative_b *= nums[i]
            res[i-1] = res[i-1] * cumulative_b
        return res    