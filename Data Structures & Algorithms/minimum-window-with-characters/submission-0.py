class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n1=len(t)
        n2=len(s)
        need = defaultdict(int)
        window=defaultdict(int)
        min_length= 1000
        formed=0
        result=''

        if n1>n2:
            return ''

        for char in t:
            need[char]+=1
        required=len(need)
        l=0
        for r, char in enumerate(s):
            window[char]+=1

            if char in need and window[char]==need[char]:
                formed+=1
        
            while required==formed:
                if r-l+1<min_length:
                    min_length=r-l+1
                    result=s[l:r+1]
                window[s[l]]-=1
                if s[l] in need and window[s[l]]<need[s[l]]:
                    formed-=1
                l+=1
        return result
            
    
        
        


        