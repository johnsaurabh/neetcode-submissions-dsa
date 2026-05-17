class MinStack:

    def __init__(self):
        self.stack=[]
        self.minstack=[]
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minstack:
            minval=self.minstack[-1]
            if val<minval:
                self.minstack.append(val)
            else:
                self.minstack.append(minval)
        else:
            self.minstack.append(val)    
        
    def pop(self) -> None:
        
        self.stack.pop()
        self.minstack.pop()
        

    def top(self) -> int:
        
        if self.stack:
            return self.stack[-1]


    def getMin(self) -> int:

        if self.minstack:
           return self.minstack[-1]
        else:
            return -1
        
