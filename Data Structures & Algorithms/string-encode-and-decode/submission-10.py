class Solution:

    def encode(self, strs: List[str]) -> str:
        def add_metadata(s):
            return f"{len(s)}#{s}"
        enc = "".join([add_metadata(s) for s in strs])
        return enc 

    def decode(self, s: str) -> List[str]:
        dec = []
        i = 0
        while i < len(s): 
            j = i
            while s[j] != "#": j += 1
            length = int(s[i:j])
            start = j + 1 # where i points + <len> + "#"
            end = start + length
            dec.append(s[start: end])
            i = j + 1 + length 
        return dec
