class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        
        while left <= right: 
            mid = left + (right-left) // 2  # trucco, matematicamente uguale a (right + left) // 2 :
                                            # (2left + right - left) // 2 = (right + left) // 2
            if nums[mid] == target: return mid
            elif nums[mid] < target: left = mid + 1 # evitiamo loop infiniti (controlli sempre mid)
            else: right = mid - 1 # evitiamo loop infiniti (controlli sempre mid)
        
        return -1