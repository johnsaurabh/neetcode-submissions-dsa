class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap=defaultdict(list)
    
        for word in strs:
            array= [0]*26
            for letter in word:
                pos= ord(letter)-ord('a')
                array[pos]+=1

            hmap[tuple(array)].append(word)

        return list(hmap.values())
        