class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        left, right = 0, len(nums)-1

        while left <= right: 
            mid = left + (right-left) // 2

            if nums[mid] == target: return mid
            
            # [6 1 2 3 4 5]; 4 -> 2 -> [3 4 5]; 4 -> 4; 4
             
            if nums[mid] < nums[right]: # condizione di non rotazione 
                if nums[mid] < target <= nums[right]: left = mid + 1 # se c'è poi anche il target
                else: right = mid - 1 # se il target non c'è
            else: # se invece è ruotato ho certezze solo sul lato sinistro
                if nums[left] <= target < nums[mid]: right = mid - 1 # applico quello che so nello standard a sx
                else: left = mid + 1

        return -1 