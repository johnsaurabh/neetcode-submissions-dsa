class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
       


        for num in tokens:
            if num in "-+*/":
                num1=int(stack.pop())
                num2=int(stack.pop())
                if num=="+":
                    res=num1 + num2
                    print(f'num1 {num1}, num2 {num2}, and result is {res}')
                elif num=="-":
                    res=num2 - num1
                    print(f'num1 {num1}, num2 {num2}, and result is {res}')
                elif num=="*":
                    res=num1 * num2
                    print(f'num1 {num1}, num2 {num2}, and result is {res}')
                elif num=="/":
                    res=num2/num1
                    print(f'num1 {num1}, num2 {num2}, and result is {res}')

                
                
                stack.append(res)
            else:
                stack.append(int(num))
        return int(stack.pop()) 

