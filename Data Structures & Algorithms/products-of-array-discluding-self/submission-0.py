class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if not nums: return [] 
        # forward: 
        fw = [1] # for each position i store the cumulative product from 0 to i-1 
        for i in range(1, len(nums)):
            fw.append(fw[-1] * nums[i-1])
        print(fw)

        bw = [1] # for each position i store the cumulative product from n to i+1 
        for i in range(len(nums)-2, -1, -1): 
            bw.insert(0, bw[0] * nums[i+1])
        print(bw)

        return [a * b for a, b in zip(fw, bw)] 
