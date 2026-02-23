# Given a binary string s, return the number of non-empty substrings that have the same number of 0's and 1's, and all the 0's and all the 1's in these substrings are grouped consecutively.

# Substrings that occur multiple times are counted the number of times they occur.


class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        tam=len(s)
        if tam==1:
            return 0
        primer=s[0]
        primer_n=1
        segundo_n=0
        aux=False
        pares=0
        for i in range(1,tam):
            if s[i]==primer:
                primer_n+=1
            else:
                aux=True
                if segundo_n!=0:
                    pares+=min(segundo_n,primer_n)
                segundo_n=primer_n
                primer_n=1
                primer=s[i]
        pares+=min(segundo_n,primer_n)
        # print(s[i],pares,segundo_n,primer,primer_n)
        if aux:
            return pares
        else:
            return 0
        

