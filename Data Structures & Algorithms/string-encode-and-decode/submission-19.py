class Solution:
    # ripetizione #1
    def encode(self, strs: List[str]) -> str:
        return "".join([f"{len(s)}#{s}" for s in strs])

    def decode(self, s: str) -> List[str]:
        print("entra:", s)
        i = 0
        res = []
        while i < len(s): 
            to_read = 0 # num of chars to read
            while s[i + to_read] != "#": to_read += 1
            # print(to_read)
            word_len = int(s[i: i+to_read])
            # print(word_len)
            i = i + to_read + 1
            # print(i, s[i])
            word = s[i: i+word_len]
            res.append(word)
            # print(res)
            i += word_len
        return res


            


