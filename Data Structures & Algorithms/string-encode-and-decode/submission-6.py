class Solution:

    def encode(self, strs: List[str]) -> str:
        def add_metadata(s):
            return f"{len(s)}#{s}"
        enc = "".join([add_metadata(s) for s in strs])
        return enc 

    def decode(self, s: str) -> List[str]:
        print("Received:", s)
        def read_length(string: str) -> Tuple[int, str]:
            """Enter a single unit <len>#<everything else>."""
            i = 0
            if string == "": 
                return 0, 0, ""
            while string[i] != "#":
                i+=1
            return int(string[:i]), i, string[i+1:] # discard "#" as well
            # 5 hello5#world
        dec = []
        total_received = len(s)
        total_read = 0
        while total_read < total_received:
            to_read, n_cyphers, reminder = read_length(s)
            dec.append(reminder[:to_read])
            total_read += to_read + 1 + n_cyphers
            s = reminder[to_read:]

        return dec
