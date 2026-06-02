# 3637. Trionic Array I
# Solved
# Easy - null
# Topics
# premium lock icon
# Companies
# Hint
# You are given an integer array nums of length n.

# An array is trionic if there exist indices 0 < p < q < n − 1 such that:

# nums[0...p] is strictly increasing,
# nums[p...q] is strictly decreasing,
# nums[q...n − 1] is strictly increasing.
# Return true if nums is trionic, otherwise return false.


class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        ind=True
        p=-1
        for i in range(len(nums)-1):
            if nums[i]>=nums[i+1]:
                p=i
                if i<1:
                    return False
                break
        if p==-1:
            return False
        q=-1
        for i in range(p,len(nums)-1):
            if nums[i]<=nums[i+1]:
                q=i
                if i<p+1:
                    return False
                break
        if p==-1:
            return False
        for i in range(q,len(nums)-1):
            if nums[i]>=nums[i+1]:
                return False
        return True