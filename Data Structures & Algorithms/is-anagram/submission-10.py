class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        hmap=defaultdict(int)

        if len(s)!=len(t):
            return False

        for ch in s:
            hmap[ch]+=1
        
        for ch in t:
            if ch not in hmap or hmap[ch]==0:
                return False
            hmap[ch]-=1
            
        return True

