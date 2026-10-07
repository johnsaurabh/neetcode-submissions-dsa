class Solution:
    def validPalindrome(self, s: str) -> bool:

        n=len(s)
        i=0
        j=n-1
        while i<j:
            if s[i]!=s[j]:
                return self.is_pal(s[i+1:j+1]) or self.is_pal(s[i:j])
            i+=1
            j-=1
        return True
    def is_pal(self,check_str):
        n=len(check_str)
        i=0
        j=n-1
        while i<j:
            if check_str[i]!=check_str[j]:
                return False
            i+=1
            j-=1
        return True

                


        

            
