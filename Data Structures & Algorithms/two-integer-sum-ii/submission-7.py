class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers)-1
        c = 0
        while c < len(numbers): 
            s = numbers[i] + numbers[j]
            if s == target: return [i+1,j+1]
            if s > target: 
                j -= 1 
            elif s < target: 
                i += 1
            c += 1        
        return []
