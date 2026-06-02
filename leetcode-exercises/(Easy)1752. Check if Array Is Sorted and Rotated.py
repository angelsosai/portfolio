# 1752. Check if Array Is Sorted and Rotated
# Solved
# Easy - 1216
# Topics
# premium lock icon
# Companies
# Hint
# Given an array nums, return true if the array was originally sorted in non-decreasing order, then rotated some number of positions (including zero). Otherwise, return false.

# There may be duplicates in the original array.

# Note: An array A rotated by x positions results in an array B of the same length such that B[i] == A[(i+x) % A.length] for every valid index i.


class Solution:
    def check(self, nums: List[int]) -> bool:
        contador=0
        for i in range(len(nums)-1):
            if nums[i]>nums[i+1]:
                contador+=1
            if contador>1:
                return False
        if contador==1 and nums[-1]>nums[0]:
            return False
        return True