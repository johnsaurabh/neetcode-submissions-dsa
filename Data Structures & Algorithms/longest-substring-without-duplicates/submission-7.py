class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_seen={}
        max_length=0

        n=len(s)
        left=0
        
        for right,char in enumerate(s):

            if char in last_seen and last_seen[char]>=left:
                
                left=last_seen[char]+1

            last_seen[char]=right
            length=right-left+1
            max_length=max(max_length,length)
        return max_length
               
       
        