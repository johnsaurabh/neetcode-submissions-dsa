class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        max_length=0
        l=0
        already_seen={}

        for r,char in enumerate(s):

            if char in already_seen and already_seen[char]>=l:

                l=already_seen[char]+1
            
            already_seen[char]=r

            max_length=max(max_length,r-l+1)

        return max_length


                

         







            



        