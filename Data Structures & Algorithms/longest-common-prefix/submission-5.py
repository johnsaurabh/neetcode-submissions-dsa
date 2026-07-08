class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        n=len(strs[0])
        word=strs[0]
        res=[]

        for i in range(n):
            
            for j in range(1, len(strs)):
                if i>=len(strs[j]) or word[i]!=strs[j][i] :
                    return ''.join(res)
            res.append(word[i])
        return ''.join(res)

        