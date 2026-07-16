class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        already_seen=defaultdict(int)
        max_length=0

        left=0
        for right,char in enumerate(s):

            if char in already_seen and already_seen[char]>=left:
                left=already_seen[char]+1

            already_seen[char]=right
            length=right-left+1
            if max_length<length:
                max_length=length
        return max_length
                



