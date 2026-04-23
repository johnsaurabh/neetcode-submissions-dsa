class Solution:

    def encode(self, strs: List[str]) -> str:

        encoded=[]
        n=len(strs)
        for word in strs:
            encoded.append(f"{len(word)}#{word}")
        return ''.join(encoded)



    def decode(self, s: str) -> List[str]:

        decoded=[]
        n=len(s)

        i=0
        length=0

        while i<n:

            j=i

            while s[j]!="#":
                j+=1
            
            length=int(s[i:j])
            
            decoded.append(s[j+1:length+j+1])
            i=length+j+1

        return decoded
