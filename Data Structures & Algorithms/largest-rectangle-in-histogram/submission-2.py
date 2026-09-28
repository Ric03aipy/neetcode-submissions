class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []

        max_area = max(heights)
        
        for i, h in enumerate(heights): 

            # strage: la colonna più bassa è il RE
            starting_idx = None
            while stack and h <= stack[-1][1]: 
                starting_idx, tall_h = stack.pop()
                # area che non può estendersi a destra = base * altezza
                area = (i - starting_idx) * tall_h

                # print(f"area=({i}-{starting_idx})*{h}={area}")
                if area > max_area: max_area = area

            # (new height, old index) or just (new height, new index) if grater
            stack.append((starting_idx if starting_idx is not None else i, h)) 
            

            # print(i, stack)

        # print(i, stack)
        # Dalle print vedo che all'ultima iterazione resta: i=5 -> [(0, 1), (2, 2), (5, 4)]
        # Posso calcolare le aree rimanenti facendo (len(height)-starting_idx) * h
        l = len(heights)
        for el in stack: 
            area = (l - el[0]) * el[1]
            # print(f"area=({l}-{el[0]})*{el[1]}={area}")
            if area > max_area: max_area = area
        
        return max_area