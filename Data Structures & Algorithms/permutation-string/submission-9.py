class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        n1=len(s1)
        n2=len(s2)
        s1_count=[0]*26
        s2_count=[0]*26
        matches=0

        if n2<n1:
            return False

        for i in range(n1):
            val1=ord(s1[i])-97
            val2=ord(s2[i])-97

            s1_count[val1]+=1
            s2_count[val2]+=1
        for i in range(26):
            if s1_count[i]==s2_count[i]:
                matches+=1
        if matches==26:
            return True
        
        left=0
        for i in range(n1,n2):
            right= ord(s2[i])-97

            s2_count[right]+=1

            if s1_count[right]==s2_count[right]:
                matches+=1
            if s1_count[right]==s2_count[right]-1:
                matches-=1
            left= ord(s2[i-n1])-97

            s2_count[left]-=1
            if s1_count[left]==s2_count[left]:
                matches+=1
            if s1_count[left]==s2_count[left]+1:
                matches-=1
            if matches==26:
                return True
        return False

            

        