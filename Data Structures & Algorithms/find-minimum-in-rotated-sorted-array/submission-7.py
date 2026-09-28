class Solution:
    def findMin(self, nums: List[int]) -> int:
        # ===============
        # ripetizione #2
        # ===============

        left, right = 0, len(nums) - 1
        curr_min = min(nums[left], nums[right])
        while left <= right:
            mid = left + (right - left) // 2
            # parte sx ordinata -> vado a dx
            if nums[left] <= nums[mid]: 
                # controllo il valore che sto per scartare potenziale minimo, ovvero il più piccolo della porzione
                curr_min = min(curr_min, nums[left])
                left = mid + 1
            else:
                # controllo il valore che sto per scartare potenziale minimo, ovvero il più piccolo della porzione
                curr_min = min(curr_min, nums[mid])
                right = mid - 1
        return curr_min