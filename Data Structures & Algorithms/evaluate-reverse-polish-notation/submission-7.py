class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        operators={'+','-','*','/'}
        stack=[]

        for token in tokens:

            if token in operators:
                num1=int(stack.pop())
                num2=int(stack.pop())

                if token=='+':
                    result=num1+num2
                elif token=='*':
                    result=num1*num2
                elif token=='-':
                    result=num2-num1
                else:
                    result= num2/num1
                stack.append(result)
            else:
                stack.append(int(token))
        return int(stack[-1])
        

        
        