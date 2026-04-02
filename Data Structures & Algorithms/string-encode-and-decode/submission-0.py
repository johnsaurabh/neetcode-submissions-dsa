class Solution:

    def encode(self, strs: List[str]) -> str:

            return ''.join(f'{len(s)}#{s}'  for s in strs)


    def decode(self, s: str) -> List[str]:
        i=0
        result=[]

        while i<len(s):

            j=i
            while s[j]!='#':
                j+=1

            word= int(s[i:j])

            result.append(s[j+1 : j+1+word])
            i=j+1+word

        return result
