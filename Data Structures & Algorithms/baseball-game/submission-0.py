class Solution:
    def calPoints(self, operations: List[str]) -> int:
        
        stack=[]
        n=len(operations)

        for op in operations:

            if op not in ['+','C','D']:
                stack.append(int(op))
            elif op=='+':
                add=int(stack[-1])+int(stack[-2])
                stack.append(add)
            elif op=='D':
                double=int(stack[-1])*2
                stack.append(double)
            else:
                stack.pop()
        return sum(stack)



