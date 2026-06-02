
# 1513. Number of Substrings With Only 1s
# Solved
# Medium

# Given a binary string s, return the number of substrings with all characters 1's. Since the answer may be too large, return it modulo 109 + 7.

from itertools import groupby
class Solution:
    def numSub(self, s: str) -> int:
        MOD=10**9+7
        conteo=0
        for key, group in groupby(s):
            if key=="1":
                n=len(list(group))
                conteo+=(n)*(n+1)//2
        return conteo%MOD
