class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # curo il caso limite ora e non ci penso dopo
        if len(nums) == 0: return 0
        # la soluzione più facile che mi viene in mente è O(nlogn) in tempo e O(1) in spazio

        # serve una soluzione O(n) in tempo e in spazio

        # mi segno l'esistenza di predecessori
        # se un elemento non ha predecessori allora è l'inizio di una catena
        # esplorando solo le catene trovo quella più lunga

        # O(n) in tempo credo, e O(n) in spazio
        numset = set(nums)

        # uso un set per l'O(1) in media di accesso, quindi questa struttura costa di nuovo O(n) in tempo e spazio 
        pred = {n for n in nums if n-1 in numset}

        # conto la lunghezza delle catene se possono costruirsi
        max_len = 0
        for n in pred: 
            curr_len = 0
            # inizio di una catena
            if n-1 not in pred: 
                # print(f"{n} è l'inizio di una catena")
                i = n
                while i in pred:
                    curr_len += 1
                    i += 1
                max_len = max(max_len, curr_len)

        return max_len + 1 # in pred non c'è il vero starter, ma si parte dal secondo elemento
        
                


                

            

