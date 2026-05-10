class Solution:
    def minWindow(self, s: str, t: str) -> str:

        need=defaultdict(int)
        window=defaultdict(int)
        formed=0
        min_length=1000
        result=''

        if len(s)<len(t):
            return ''

        for char in t:
            need[char]+=1

        required=len(need)

        left=0
        for right,char in enumerate(s):
            window[char]+=1

            if char in need and window[char]==need[char]:
                formed+=1

            while formed==required:

                if right-left+1<min_length:
                    min_length=right-left+1
                    result=s[left:right+1]
                
                window[s[left]]-=1
                if s[left] in need and window[s[left]]<need[s[left]]:
                        formed-=1
                left+=1
        return result

            

                    

                    



