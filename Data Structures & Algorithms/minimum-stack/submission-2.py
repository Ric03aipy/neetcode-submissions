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

    def pop(self) -> None:
        val = self.stack.pop()
        if val == self.minimums[-1]:
            self.minimums.pop()      
        
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minimums[-1]
