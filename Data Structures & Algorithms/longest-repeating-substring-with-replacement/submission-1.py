class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_freq=defaultdict(int)
        max_freq=0
        max_substring=0

        left=0

        for right,char in enumerate(s):

            char_freq[char]+=1
            max_freq=max(max_freq,char_freq[char])
            window=right-left+1
            if window -max_freq>k:
                char_freq[s[left]]-=1
                left+=1
            max_substring=max(right-left+1,max_substring)
        return max_substring
                #but how do I subtract left from char_freq? 
                # I didn't track char_freq[left].. my key is the value right..



        