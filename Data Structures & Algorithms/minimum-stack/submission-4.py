class MinStack:

    def __init__(self):
        self.stack=[]
        self.minstack=[]
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minstack:
            if self.minstack[-1]>=val:
                self.minstack.append(val)
            elif self.minstack[-1]<val:
                self.minstack.append(self.minstack[-1])
        else:
            self.minstack.append(val)

        

    def pop(self) -> None:
        self.stack.pop()
        self.minstack.pop()
        

    def top(self) -> int:
       return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minstack[-1] 
        
