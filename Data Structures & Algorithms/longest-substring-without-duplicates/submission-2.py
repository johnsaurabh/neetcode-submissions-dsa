class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left=0
        already_seen={}
        max_length=0
        n=len(s)

        for r,char in enumerate(s):
            
            if char in already_seen and already_seen[char]>=left:
                left=already_seen[char]+1

            already_seen[char]=r
            max_length=max(max_length,r-left+1)
        return max_length

                
              
            
        