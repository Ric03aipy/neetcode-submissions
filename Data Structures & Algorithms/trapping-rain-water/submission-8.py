class Solution:
    def trap(self, height: List[int]) -> int:
        # ===================
        # ripetizione #3
        # ===================

        left, right = 0, len(height)-1
        left_h, right_h = height[left], height[right]
        tot_water = 0

        while left < right: 
            
            # Muro di sx visto finora (da 0 a left) più piccolo di quello finora osservato a dx (da right a len(height) - 1)
            if left_h < right_h: 
                left += 1
                left_h = max(left_h, height[left])
                water = left_h - height[left]
            else: 
                right -= 1
                right_h = max(right_h, height[right])
                water = right_h - height[right]
            
            tot_water += water

        return tot_water

                