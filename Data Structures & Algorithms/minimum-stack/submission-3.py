class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.minStack) == 0:
            self.minStack.append(val)
        else:
            self.minStack.append(min(val, self.minStack[-1]))

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]


 #def getMin(self) -> int:
        #temp = []
        #min_ = self.stack[-1]

        ## find the min by popping off og stack
        ## append all numbers to temp
        #while len(self.stack):
        #    min_ = min(min_, self.stack[-1])
        #    temp.append(self.stack.pop())

        ## re append the nums back to stack using temp
        #while len(temp):
        #    self.stack.append(temp.pop())