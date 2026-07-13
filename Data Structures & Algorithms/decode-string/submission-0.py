class Solution:
    def decodeString(self, s: str) -> str:

        current_string=''
        stack=[]
        count=0

        for ch in s:

            if  ch =='[':
                stack.append([current_string,count])
                current_string=''
                count=0
            elif ch.isdigit():
                count=count*10 +int(ch)
            elif ch ==']':
                prev_string,prev_count=stack.pop()
                current_string=prev_string+current_string*prev_count
            else:
                current_string+=ch
        return current_string
        

            

        