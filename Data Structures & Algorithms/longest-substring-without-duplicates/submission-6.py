class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n=len(s)
        max_length=0
        left=0
        already_seen={}

        for right, char in enumerate(s):
            if char in already_seen and already_seen[char]>=left:
                left=already_seen[char]+1
            
            already_seen[char]=right
            max_length=max(right-left+1,max_length)

        return max_length
            
            

        