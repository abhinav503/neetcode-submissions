class MinStack:
    def __init__(self):
        self.minStack = []
        self.value = []

    def push(self, val: int) -> None:
        self.value.append(val)
        if not self.minStack or val <= self.minStack[-1]:
            self.minStack.append(val)

    def pop(self) -> None:
        if self.value:
            if self.minStack[-1] == self.value[-1]:
                self.minStack.pop()
            self.value.pop()
        
    def top(self) -> int:
        return self.value[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
      
