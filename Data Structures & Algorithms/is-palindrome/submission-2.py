class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_cleaned=''.join(c.lower() for c in s if c.isalnum())
        i=0
        j=len(s_cleaned)-1
        while i<j:
            if s_cleaned[i]!=s_cleaned[j]:
                return False
            j-=1
            i+=1
        return True
