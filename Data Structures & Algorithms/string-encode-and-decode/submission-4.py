class Solution:

    def encode(self, strs: List[str]) -> str:
        self.sep = "SPLIT"
        self.empty = "EMPTY" # []
        self.is_empty = len(strs) == 0
        enc = self.sep.join(strs) 
        return enc 

    def decode(self, s: str) -> List[str]:
        dec = s.split(self.sep) if not self.is_empty else []   
        return dec