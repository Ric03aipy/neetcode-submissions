class Solution:
    def trap(self, height: List[int]) -> int:
        # ===================
        # ripetizione #4
        # ===================

        left, right = 0, len(height) - 1
        h_left, h_right = height[left], height[right]
        water = 0

        while left < right:
            # minimo meno corrente 
            if h_left < h_right: 
                left += 1
                water += max(h_left - height[left], 0)
                h_left = max(h_left, height[left])
            else: 
                right -= 1
                water += max(h_right - height[right], 0)
                h_right = max(h_right, height[right])

        return water