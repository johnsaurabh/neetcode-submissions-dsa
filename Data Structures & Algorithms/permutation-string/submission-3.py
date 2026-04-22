class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        n=len(s1)
        s1count=[0]*26
        s2count=[0]*26
        matches=0

        if n>len(s2):
            return False

        for i in range(n):
            s1count[ord(s1[i])-ord("a")]+=1
            s2count[ord(s2[i])-ord("a")]+=1

        for i in range(26):
            if s1count[i]==s2count[i]:
                matches+=1
        
        if matches==26:
            return True

        for i in range(n,len(s2)):
            right=ord(s2[i])-ord("a")
            s2count[right]+=1

            

            if s2count[right]==s1count[right]:
                matches+=1
            elif s2count[right]-1==s1count[right]:
                matches-=1
                
            left= ord(s2[i-n])-ord("a")
            s2count[left]-=1

            if s2count[left]==s1count[left]:
                matches+=1
            elif s2count[left]+1==s1count[left]:
                matches-=1
                

            if matches==26:
                return True
        return False




        