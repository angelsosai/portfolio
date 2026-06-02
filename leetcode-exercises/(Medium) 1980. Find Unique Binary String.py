
# 1980. Find Unique Binary String
# Solved
# Medium • 1214
# Topics
# premium lock icon
# Companies
# Hint
# Given an array of strings nums containing n unique binary strings each of length n, return a binary string of length n that does not appear in nums. If there are multiple answers, you may return any of them.

from itertools import product

class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:        
        for comb in product([0, 1], repeat=len(nums[0])):
            cad="".join(map(str, comb))
            if cad not in nums:
                return cad 
            