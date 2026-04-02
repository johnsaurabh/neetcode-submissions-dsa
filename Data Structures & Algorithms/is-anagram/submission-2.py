class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s)!=len(t):
            return False
        hmap={}
    
        for letter in s:
                
            hmap[letter]=hmap.get(letter, 0) + 1

        for letter in t:
            if letter in hmap:
                hmap[letter]=hmap.get(letter, 0) -1
            

        if all(v==0 for v in hmap.values()):
            return True
            
        return False
        