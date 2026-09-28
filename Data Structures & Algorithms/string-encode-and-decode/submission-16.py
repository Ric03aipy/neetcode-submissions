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
            next_len_elem = []
            while s[i + j].isdigit(): 
                next_len_elem.append(s[i+j])
                j += 1
            # print(next_len_elem, "".join(next_len_elem))
            next_len = int("".join(next_len_elem))
            # print(f"bisogna leggere {next_len} valori")
            i += j + 1
            res.append(s[i: i + next_len])
            i += next_len
            # print(res)

        return res








