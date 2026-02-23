# You are given a 0-indexed integer array nums, where nums[i] represents the score of the ith student. You are also given an integer k.

# Pick the scores of any k students from the array so that the difference between the highest and the lowest of the k scores is minimized.

# Return the minimum possible difference.

class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        if k==1:
            return 0
        lista=sorted(nums)
        tam=len(nums)
        minimo=float("inf")
        for i in range(0,tam-k+1):
            if lista[i+k-1]-lista[i]<minimo:
                minimo=lista[i+k-1]-lista[i]
            if minimo==k-1:
                return k-1
        return minimo