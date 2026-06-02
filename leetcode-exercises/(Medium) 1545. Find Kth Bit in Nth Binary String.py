

# Given the binary representation of an integer as a string s, return the number of steps to reduce it to 1 under the following rules:

# If the current number is even, you have to divide it by 2.

# If the current number is odd, you have to add 1 to it.

# It is guaranteed that you can always reach one for all test cases.

 
class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        cad="0"
        table = str.maketrans('01', '10')
        for i in range(n-1):
           cad=cad+"1"+cad.translate(table)[::-1]
        return cad[k-1]