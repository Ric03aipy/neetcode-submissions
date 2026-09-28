class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # ==============
        # ripetizione #1
        # ==============

        import heapq
        from collections import deque

        cycles = 0

        # Conto le frequenze
        freqs = [[0, chr(ord('A') + i)] for i in range(26)]
        for task in tasks: freqs[ord(task) - ord('A')][0] += 1
        # Pulisco e preparo per avere un MaxHeap
        freqs = [(-f, c) for f, c in freqs if f]
        heapq.heapify(freqs)

        waiting_room = deque() # [(char, +freq, time_back)]

        while freqs or waiting_room: 

            # Peek 
            if waiting_room: 
                c, f, t = waiting_room[0]
                # Se il tempo globale ha raggiunto il tempo di scongelamento allora facciamo rientrare l'elemento in attesa
                if t == cycles: 
                    c, f, t = waiting_room.popleft()
                    heapq.heappush(freqs, (-f, c))

            cycles += 1

            # Posso estrarre solo se ci sono elementi
            if freqs: 
                neg_f, c, = heapq.heappop(freqs)
                # Se la frequenza è superiore a 1 allora dopo essere stato processato l'elemento va in sala d'attesa
                new_f = -neg_f - 1
                # ... processing ...
                if new_f > 0: 
                    waiting_room.append((c, new_f, cycles + n))
                

        return cycles