class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        string_freq= defaultdict(int)
        if len(s)!=len(t):
            return False

        for char in s:
            string_freq[char]+=1

        for char in t:
            if char in string_freq and string_freq[char]>0:
                string_freq[char]-=1

            else:
                return False
        return True


        