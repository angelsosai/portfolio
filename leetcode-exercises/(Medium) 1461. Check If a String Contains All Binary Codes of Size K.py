# 1461. Check If a String Contains All Binary Codes of Size K
# Solved
# Medium • 1444
# Topics
# premium lock icon
# Companies
# Hint
# Given a binary string s and an integer k, return true if every binary code of length k is a substring of s. Otherwise, return false.

class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        conj=set()
        # val=False
        for i in range(len(s)-k+1):
            conj.add(s[i:i+k])
            # print(conj,s[i:i+k]) 
        if len(conj)==2**k:
            return True
        return False