class MinStack:

    def __init__(self):
        self.stack = []
        self.minimums = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minimums: 
            self.minimums.append(val)
        else: 
            if val <= self.minimums[-1]: self.minimums.append(val)
        # print(f"stack after push = {self.stack} | {self.minimums}")


    def pop(self) -> None:
        val = self.stack.pop()
        if val == self.minimums[-1]:
            self.minimums.pop()      
        # print(f"stack after pop = {self.stack} | {self.minimums}")

        
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        # print(f"minimo richiesto = {self.minimums[-1]}")
        return self.minimums[-1]
