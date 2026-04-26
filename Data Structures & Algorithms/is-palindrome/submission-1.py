class Solution:
    def isPalindrome(self, s: str) -> bool:
        #You need to join the string
        #you need to convert all the letters to lowercase or upppercase
        #only if they are letter, ifnore alphanumericals
        #reverse the string and compare.

        s_cleaned=''.join(c.lower() for c in s if c.isalnum())
        
        if s_cleaned==s_cleaned[::-1]:
            return True
        return False

