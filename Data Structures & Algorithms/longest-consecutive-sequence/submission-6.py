class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        max_len = 0
        for n in nums: 
            if n-1 not in numset: 
                curr_len = 1
                i = n
                while i + 1 in numset: 
                    i+=1
                    curr_len+=1
                max_len = max(max_len, curr_len)
        return max_len