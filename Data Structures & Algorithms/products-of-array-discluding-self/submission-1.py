class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        fw = [1] * l
        bw = [1] * l
        for i in range(1, l): 
            fw[i] = fw[i-1] * nums[i-1]
        for i in range(l-1, 0, -1):
            bw[i-1] = bw[i] * nums[i]
        res = [f * b for f, b in zip(fw, bw)]
        return res        
        
            