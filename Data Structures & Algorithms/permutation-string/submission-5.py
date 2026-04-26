class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        #We are dealing with permutations of a string.
        #We need to have the count of each character in s1 to compare it ot the frequency of characters in s2
        #We can do this using Hashmaps, or Hashtables.
        #If we use Hashtable, and a variable called matches, we don't have to compare the entire hashtables every iteration.

        #Initialize the required variables.
        s1count=[0]*26
        s2count=[0]*26
        matches=0
        n1=len(s1)
        n2=len(s2)

        if n1>n2:
            return False

        for i in range(n1):
            s1count[ord(s1[i])-97]+=1
            s2count[ord(s2[i])-97]+=1
        

        for i in range(26):
            if s1count[i]==s2count[i]:
                matches+=1
                
        if matches==26:
            return True

        for i in range(n1,n2):
            right=ord(s2[i])-97
            s2count[right]+=1

            if s2count[right]==s1count[right]:
                matches+=1
            elif s2count[right]-1==s1count[right]:
                matches-=1

            left= ord(s2[i-n1])-97
            s2count[left]-=1
            if s2count[left]==s1count[left]:
                matches+=1
            elif s2count[left]+1==s1count[left]:
                matches-=1
            
            if matches==26:
                return True

        return False

            
        
        

                
            
