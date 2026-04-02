class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_cleaned= ''.join(c.lower() for c in s if c.isalnum())
        if s_cleaned== s_cleaned[::-1]:
            return True
        return False