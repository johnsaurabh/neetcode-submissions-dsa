class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n=len(strs[0])
        word=word=strs[0]
        result=[]

        for i in range(n):

            for j in range(1, len(strs)):
                if i>=len(strs[j]):
                    return ''.join(result)
                if word[i]!=strs[j][i]:
                    return ''.join(result)
            result.append(word[i])
        return ''.join(result)

