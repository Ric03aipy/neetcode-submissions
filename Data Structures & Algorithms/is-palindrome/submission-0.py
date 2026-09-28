class Solution:
    def isPalindrome(self, s: str) -> bool:
        # clear string
        string_list = [c.lower() for c in s if c.isalnum()]
        for i in range(len(string_list) // 2): 
            if string_list[i] != string_list[-i-1]: 
                print(i, string_list[i], string_list[-i-1])
                return False
        return True