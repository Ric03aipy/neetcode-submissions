class Solution:
    def trap(self, height: List[int]) -> int:
        area = 0
        # maximum height seen
        max_l = 0  
        max_r = 0
        # two ptrs
        n = len(height)
        i = 0
        j = n - 1
        while i < j:
            l = height[i]
            r = height[j]
            area_l = max_l - l
            area_r = max_r - r
            if area_l > 0: area += area_l
            else: max_l = l
            if area_r > 0: area += area_r
            else: max_r = r
            if max_l < max_r: i += 1
            else: j -= 1
        return area


