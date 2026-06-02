
# Given a positive integer, check whether it has alternating bits: namely, if two adjacent bits will always have different values.

 

class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        m=n<<1
        # print(m)
        if not n&1:
            m+=1  
        # print(m) 
        valor=(m)^n
        # print(valor,(n<<1))
        return valor&(valor+1)==0