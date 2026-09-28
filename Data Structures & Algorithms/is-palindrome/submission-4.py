class Solution:
    def isPalindrome(self, s: str) -> bool:
        """Soluzione più pulita"""


        i, j = 0, len(s) - 1
        
        while i < j:
            # Salta i caratteri non alfanumerici da sinistra
            while i < j and not s[i].isalnum():
                i += 1
            # Salta i caratteri non alfanumerici da destra
            while i < j and not s[j].isalnum():
                j -= 1
                
            # Ora siamo sicuri che entrambi i puntatori sono su caratteri validi
            if s[i].lower() != s[j].lower():
                return False
                
            i += 1
            j -= 1
            
        return True