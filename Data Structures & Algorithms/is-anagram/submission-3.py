class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        hmap=defaultdict(int)
        hmap2=defaultdict(int)

        if len(s)!=len(t):
            return False
        
        for ch in s:
            hmap[ch]+=1

        for ch in t:
            if hmap[ch]==0:
                return False
            hmap[ch]-=1

        for key,value in hmap.items():
            if hmap[key]!=0:
                return False

        return True


        