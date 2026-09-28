class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        numset = set(nums)
        maxlen = 1
        for num in nums: 
            if num-1 not in numset and num+1 in numset: 
                seqlen=1
                val=num
                while (val + 1) in numset: 
                    val += 1
                    seqlen += 1
                if seqlen > maxlen: maxlen = seqlen
        return maxlen
                


                

            

