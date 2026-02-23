# 868. Binary Gap
# Solved
# Easy • 834
# Topics
# premium lock icon
# Companies
# eBay
# X
# Given a positive integer n, find and return the longest distance between any two adjacent 1's in the binary representation of n. If there are no two adjacent 1's, return 0.

# Two 1's are adjacent if there are only 0's separating them (possibly no 0's). The distance between two 1's is the absolute difference between their bit positions. For example, the two 1's in "1001" have a distance of 3.



class Solution:
    def binaryGap(self, n: int) -> int:
        cadena=str(bin(n))[2:]
        maxi=0
        aux=0
        primer=True
        for i,j in enumerate(cadena):
            if j=="1":
                if maxi<(i-aux):
                    maxi=i-aux
                aux=i
        return maxi


