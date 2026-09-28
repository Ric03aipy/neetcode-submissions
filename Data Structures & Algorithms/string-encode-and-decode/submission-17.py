class Solution:

    def encode(self, strs: List[str]) -> str:
        str_list = []
        for s in strs: str_list.append(f"{len(s)}#{s}")
        """
        Example:
        ['Hello', 'World']
        #5#Hello#5#World
        ['', '5', 'Hello', '5', 'World']

        Example: 
        []
        ['']

        Example: 
        ['']
        #0#
        ['', '0', '']

        Example: 
        ['']
        #0##0#
        ['', '0', '', '0', '']
        """
        return "".join(str_list)

    def decode(self, s: str) -> List[str]:
        # print(s)
        res = []
        i = 0
        while i < len(s): 
            # === read length ===
            j = 0 # pointer to length of next word to read
            # this while loop build seach for lengths with an arbitrary number of digits
            next_len_elem = []  
            while s[i + j].isdigit(): 
                next_len_elem.append(s[i+j])
                j += 1
            next_len = int("".join(next_len_elem))

            # skip the metadata
            i += j + 1
            # read the word
            word = []
            c = 0
            while c < next_len:
                # [i: i + next_len]
                word.append(s[i + c])
                c += 1
            res.append("".join(word))
            
            # update the pointer to the next metadata
            i += next_len
            # print(res)

        return res








