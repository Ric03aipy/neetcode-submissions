class Solution:

    # ======================
    # ripetizione #2
    # ======================

    def encode(self, strs: List[str]) -> str:
        return "".join([f"{len(s)}#{s}" for s in strs])

    def decode(self, s: str) -> List[str]:
        res = []

        i = 0
        while i < len(s):
            num_chars = 0
            while s[i+num_chars] != "#": 
                num_chars += 1
            to_read = int(s[i:i+num_chars]) 
            i += num_chars
            i += 1
            res.append(s[i:i+to_read])
            i += to_read

        return res
