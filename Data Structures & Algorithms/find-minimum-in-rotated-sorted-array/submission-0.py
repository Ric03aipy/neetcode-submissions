class Solution:
    def findMin(self, nums: List[int]) -> int:
        # [4,5,0,1,2,3] se mid = 1 e lo dividi in [4,5,0] e [1,2,3] per sapere è il minimo non mi basta
        # sfruttare l'info di ordinamento e quindi sapere che l'elemento minimo del subarray è [0], 
        # devo vedere il minimo tra [0] e [-1] per ciascun subarray. Chi contiene il minimo assoluto è il candidato. 

        left, right = 0, len(nums) - 1
        min_found = float('inf')
        while left <= right: 
            mid = left + (right - left) // 2
            
            # controllo su mid
            min_found = min(min_found, nums[mid])

            # subarray sx : nums[left:mid] - mid escluso, left incluso
            min_left = min(nums[left], nums[mid-1]) if mid != 0 else nums[left]
            # subarray dx : nums[mid+1:right+1] - mid escluso, right incluso    
            min_right = min(nums[mid+1], nums[right]) if mid != len(nums)-1 else nums[right]

            # Il testo cita "all elements in the rotated sorted array nums are unique" -> no interesse in ==
            if min_left < min_right: 
                right = mid - 1
            else: left = mid + 1
        
        return min_found
            