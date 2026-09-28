class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area = 0
        max_area = 0 
        i = 0
        j = len(heights) - 1
        # n_interbar_spaces = j - i 
        # capacity = min(heights[i], heights[j])
        # area = n_interbar_spaces * capacity
        # if area > max_area: max_area = area
        while i < j: 
            n_interbar_spaces = j - i 
            if heights[i] < heights[j]: 
                capacity = heights[i]
                move_left = True
            else: 
                capacity = heights[j]
                move_left = False
            area = n_interbar_spaces * capacity
            print(f"i={i}, j={j}, hi={heights[i]}, hj={heights[j]}, capacity={capacity}, bars={n_interbar_spaces}")
            if area > max_area: max_area = area
            if move_left: i+= 1
            else: j-=1

        return max_area
            
