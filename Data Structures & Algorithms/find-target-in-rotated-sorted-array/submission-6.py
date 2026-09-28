class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # ================
        # ripetizione #2
        # ================

        # Idea di fondo: io so fare ricerca binaria solo su una parte ordinata. Quindi la farò solo lì
        
        left, right = 0, len(nums) - 1
        
        while left <= right: 
            
            mid = left + (right - left) // 2

            if nums[mid] == target: return mid
            # dx ordinata
            if nums[mid] < nums[right]: 
                # target nella parte ordinata
                if nums[mid] < target <= nums[right]: left = mid + 1
                else: right = mid - 1
            # sx ordinata
            else: 
                if nums[left] <= target < nums[mid]: right = mid - 1
                else: left = mid + 1
        
        # Non trovo 
        return -1