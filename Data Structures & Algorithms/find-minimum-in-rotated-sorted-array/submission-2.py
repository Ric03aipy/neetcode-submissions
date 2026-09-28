class Solution:
    def findMin(self, nums: List[int]) -> int:
        # ===============
        # ripetizione #1
        # ===============

        left, right = 0, len(nums) - 1
        res = float('inf')
        while left <= right: 
            mid = left + (right - left) // 2
            if nums[mid] <= nums[right]: # parte dx ordinata
                res = min(res, nums[mid])
                right = mid - 1 # se è ordinata allora sicuramente il potenzilae minimo successivo non è in mezzo
            else: 
                left = mid + 1
        return res