class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # ===============
        # ripetizione #1 (alternativa)
        # ===============

        info = sorted([(pos, sp) for pos, sp in zip(position, speed)], key=lambda x: -x[0]) 

        stack = []


        for pos, sp in info:

            time = (target - pos ) / sp

            if not stack or time > stack[-1]: stack.append(time)
        
        return len(stack)