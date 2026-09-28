class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        d = {}
        for i in nums: 
            if d.get(i): return True
            else: d[i] = 1
        return False



        