class Solution:
    def trap(self, height: List[int]) -> int:
        # ===================
        # ripetizione #1 
        # ===================
        i = 0
        j = len(height) - 1
        
        highest_left = height[i]
        highest_right = height[j]
 
        total_water = 0
        while i < j: 
            # print("inizio", i, j)
            if highest_left < highest_right: 
                # la prima cosa da fare è aggiornare i puntatori
                i += 1

                highest_left = max(highest_left, height[i])
                water = highest_left - height[i]
                # le due righe precedenti a questa si possono anche invertire, ma poi bisogna controllare esplicitamente che water sia > 0
                
                # print("water left", water)
            else: 
                j -= 1
                highest_right = max(highest_right, height[j])
                water = highest_right - height[j]
                # print("water right", water)
            # print("fine", i, j)

            total_water += water
        return total_water
