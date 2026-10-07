class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n=min(len(word1),len(word2))
        long_str=max(word1,word2,key=len)
        merged_str=[]

        for i in range(n):
            merged_str.append(f'{word1[i]}{word2[i]}')
        merged_str.append(long_str[n:])
        return ''.join(merged_str)




        