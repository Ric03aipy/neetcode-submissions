class Solution:
    # ======================
    # ripetizione #2
    # ======================
    def encode(self, strs: List[str]) -> str:
        return "".join([f"{len(s)}#{s}" for s in strs])


    def decode(self, s: str) -> List[str]:
        
        res = []

        read = 0
        while read < len(s): 
            n2read_left = read
            n2read_right = read
            while s[n2read_right] != "#": n2read_right += 1
            n2read = int(s[n2read_left:n2read_right])
            read += n2read_right - n2read_left + 1
            res.append(s[read: read + n2read])
            read += n2read

        return res