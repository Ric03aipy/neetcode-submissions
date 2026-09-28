class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # ===============
        # ripetizione #1 
        # ===============

        nums.sort()
        res = []

        l = len(nums)
        i = 0
        while i < l:
            
            j = i + 1
            k = l - 1

            while j < k: # i is fixed in this loop

                s =  nums[i] + nums[j] + nums[k]

                # condizioni del two pointers pattern
                if s == 0: 
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    while j < k and nums[j] == nums[j-1]: j+= 1

                elif s > 0: k-= 1
                else: j += 1
            
            # update di default 
            i += 1
            # ATTENZIONE: IN PYTHON nums[-1] NON CRUSHA!!!
            while i < l and nums[i] == nums[i-1]: i+= 1 # se i=l : j=l+1 > k=l-1 non entra mai nel while e ritorna res safely


        return res

