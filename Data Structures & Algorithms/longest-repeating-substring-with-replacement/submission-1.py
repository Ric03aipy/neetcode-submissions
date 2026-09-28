class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        i = 0
        max_len = 0
        
        max_freq = 0
        frequencies = {c:0 for c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"}
        
        p = 0
        while p < len(s): 
            # print(f"Inizio iter: {p}")
            # temp = {k: v for k,v in frequencies.items() if v != 0}
            # print(f"freq={temp}")
            frequencies[s[p]] += 1
            max_freq = max(list(frequencies.values()))
            winlen = p - i + 1
            # print(f"Pre not: p={p}, i={i}, winlen={winlen}, k={k}")
            while not (winlen - max_freq <= k): 
                frequencies[s[i]] -= 1
                i += 1
                max_freq = max(list(frequencies.values()))
                winlen = p - i + 1
            max_len = max(max_len, winlen)
            # print(f"Fine iter: {p}")
            # temp = {k: v for k,v in frequencies.items() if v != 0}
            # print(f"freq={temp}, win={s[i:p+1]}")
            p += 1


        return max_len
