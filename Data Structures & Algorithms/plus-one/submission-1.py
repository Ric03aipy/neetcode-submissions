class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        if not digits: return []
        
        last = -1
        digits[last] += 1
        carry, digits[last] = divmod(digits[last], 10)
        while carry and last > -len(digits): # Maggiore stretto perché aggiorno come prima operazione
            last -= 1
            digits[last] += 1
            carry, digits[last] = divmod(digits[last], 10)
        if carry: 
            return [1] + digits
        return digits