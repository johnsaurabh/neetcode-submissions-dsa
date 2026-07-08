class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        
        hmap=defaultdict(list)

        for word in strs:
            count=[0]*26

            for char in word:
                count[ord(char)-97]+=1
            hmap[tuple(count)].append(word)
        return list(hmap.values())

            
        