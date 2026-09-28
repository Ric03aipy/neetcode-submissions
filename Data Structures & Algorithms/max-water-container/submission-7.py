class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights) - 1
        max_area = 0
        while i < j: 
            base = j - i
            height = min(heights[i], heights[j])
            area = base * height
            if max_area < area: max_area = area
            if heights[i] < heights[j]: i += 1
            else: j -= 1
        return max_area