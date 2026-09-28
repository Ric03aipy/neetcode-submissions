class Solution:
    def isPalindrome(self, s: str) -> bool:
        # initialize indeces
        i = 0
        j = len(s) - 1
        while i < j: 
            si_valid = s[i].isalnum()
            sj_valid = s[j].isalnum()
            if si_valid and sj_valid:
                # print(f"Confronto tra {i}->{s[i]}, {j}->{s[j]}")
                if s[i].lower() != s[j].lower(): return False
                i += 1
                j -= 1
            elif not si_valid: i+= 1
            else: j-= 1

        return True