class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded=[]
        for word in strs:
            encoded.append(f'{len(word)}#{word}')
        return ''.join(encoded)

    def decode(self, s: str) -> List[str]:

        decoded=[]
        i=0

        while i<len(s):
            j=i

            while s[j]!='#':
                j+=1
            length=s[i:j]
            word=s[j+1:int(length)+j+1]
            decoded.append(word)
            i=int(length)+j+1
        return decoded
        
