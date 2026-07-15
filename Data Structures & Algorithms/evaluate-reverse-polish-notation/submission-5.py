class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        operators={'+','-','*','/'}
        res=0
        for token in tokens:
            if token not in operators:
                stack.append(int(token))
            else:

                right=stack.pop()
                left=stack.pop()
                
                if token=='+':
                    
                    res=left+right
                elif token=='*':
                    res=left*right
                elif token=='-':
                    res=left-right
                else:
                    res=int(left/right)
                stack.append(int(res))
        return stack[-1]
                