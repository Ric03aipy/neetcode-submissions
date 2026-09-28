class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_len = 0
        window = {} # {char: freq}
        left = 0
        k_currency = k
        for right in range(len(s)): 
            # il numero di caratteri che invalidano la cosa è dato dal numero di caratteri totali -
            # quelli di riferimento del più frequente
            window[s[right]] = window.get(s[right], 0) + 1

            highest_freq = 0
            most_freq = None # non realmente utile
            total_chars = 0
            for key, v in window.items(): 
                if v > highest_freq: 
                    most_freq = key   # non realmente utile
                    highest_freq = v
                total_chars += v
            k_required = total_chars - highest_freq
            if k_required > k: 
                if window[s[left]]: window[s[left]] -= 1
                else: del window[s[left]]
                left += 1

            max_len = max(max_len, right-left+1)

        return max_len


