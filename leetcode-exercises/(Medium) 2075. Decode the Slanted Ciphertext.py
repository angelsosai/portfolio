
# 2075. Decode the Slanted Ciphertext
# Solved
# Medium - 1724
# Topics
# premium lock icon
# Companies
# Hint
# Grammarly
# A string originalText is encoded using a slanted transposition cipher to a string encodedText with the help of a matrix having a fixed number of rows rows.

# originalText is placed first in a top-left to bottom-right manner.


class Solution:
    
    
    
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        if rows==1:
            return encodedText
        leng=len(encodedText)
        col=leng//rows
        t=""
        for i in range(col):
            aux=0
            for j in range(0,min(rows,col-i)):
                t+=encodedText[aux*col+j+i]
                aux+=1
        return t.rstrip()