class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
    
        n=len(strs[0])
        word=strs[0]
        longestcommonprefix=[]

        for i in range(0, n):
            for j in range(1, len(strs)):
                if i>= len(strs[j]):
                    return  "".join(longestcommonprefix)
                if word[i]!=strs[j][i]:
                    return  "".join(longestcommonprefix)
                    
            longestcommonprefix.append(word[i])
        return "".join(longestcommonprefix)
        