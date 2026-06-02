
# 3741. Minimum Distance Between Three Equal Elements II
# Solved
# Medium - null
# Topics
# premium lock icon
# Companies
# Hint
# You are given an integer array nums.

# A tuple (i, j, k) of 3 distinct indices is good if nums[i] == nums[j] == nums[k].

# The distance of a good tuple is abs(i - j) + abs(j - k) + abs(k - i), where abs(x) denotes the absolute value of x.

# Return an integer denoting the minimum possible distance of a good tuple. If no good tuples exist, return -1.

class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        dic={}
        dic2={}
        minimo=float("inf")
        for i in range(len(nums)):
            if nums[i] in dic:
                if nums[i] in dic2:
                    if i-dic2[nums[i]]<minimo:
                        minimo=i-dic2[nums[i]]
                dic2[nums[i]] =dic[nums[i]]
                dic[nums[i]]=i
            else:
                dic[nums[i]]=i
        if minimo==float("inf"):
            return -1
        return 2*minimo