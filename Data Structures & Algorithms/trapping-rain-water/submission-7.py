class Solution:
    def trap(self, height: List[int]) -> int:
        # ===================
        # ripetizione #2
        # ===================

        i = 0
        j = len(height) - 1

        highest_left = height[i]
        highest_right = height[j]

        tot_water = 0

        while i < j: 

            if highest_left < highest_right: 
                i += 1
                highest_left = max(highest_left, height[i])
                water = highest_left - height[i]
            else: 
                j -= 1
                highest_right = max(highest_right, height[j])
                water = highest_right - height[j]
        
            tot_water += water

        return tot_water
            
