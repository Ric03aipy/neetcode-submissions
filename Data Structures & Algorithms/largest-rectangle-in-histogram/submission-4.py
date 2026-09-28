class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # ==============
        # ripetizione #1
        # ==============

        stack = []
        max_area = 0

        for i, h in enumerate(heights): 
            
            old_i = None
            while stack and h <= stack[-1][1]: 
                old_i, old_h = stack.pop()
                old_area = (i - old_i) * old_h
                max_area = max(max_area, old_area)

            stack.append((old_i, h) if old_i is not None else (i, h))

            # print(stack)

        for idx, h in stack:
            base = i - idx + 1
            area = base * h
            max_area = max(max_area, area)
            # print(max_area)

        return max_area


