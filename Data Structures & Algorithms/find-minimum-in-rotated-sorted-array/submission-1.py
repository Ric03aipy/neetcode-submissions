class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        min_found = float('inf')
        while left <= right: 
            mid = left + (right - left) // 2
            
            # controllo su mid
            min_found = min(min_found, nums[mid])

            
            if nums[mid] > nums[right]: left = mid + 1 # il breakpoint e quindi il minimo è tra mid e right
            else: right = mid - 1 # mid è già nella metà contenente il minimo
        
        return min_found