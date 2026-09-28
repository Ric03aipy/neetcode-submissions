class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # ===============
        # ripetizione #1
        # ===============
        
        slow = 0 
        fast = 0
        slow = nums[slow]
        fast = nums[nums[fast]]
        while slow != fast: 
            slow = nums[slow]
            fast = nums[nums[fast]]

        slow2 = 0
        while slow2 != slow:
            slow2 = nums[slow2]
            slow = nums[slow]
        return slow