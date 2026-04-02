class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length=0
        l=0
        char_index={}

        for r, ch in enumerate(s):

            if ch in char_index and char_index[ch]>=l:
                l= char_index[ch]+1

            char_index[ch]=r
            max_length=max(max_length,r-l+1)

        return max_length