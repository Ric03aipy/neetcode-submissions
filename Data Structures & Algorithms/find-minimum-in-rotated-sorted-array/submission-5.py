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
            curr_min = min(curr_min, nums[mid], nums[right], nums[left])
            if nums[left] <= nums[mid]: 
                left = mid + 1
            else:
                right = mid - 1
        return curr_min