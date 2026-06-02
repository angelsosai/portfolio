

# 1262. Greatest Sum Divisible by Three
# Solved
# Medium - 1736
# Topics
# premium lock icon
# Companies
# Hint
# DE Shaw
# Given an integer array nums, return the maximum possible sum of elements of the array such that it is divisible by three.

 

class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        suma=sum(nums)
        objetivo=suma%3
        if objetivo==0:
            return suma
        dic={
            0:[],
            1:[],
            2:[]
        }
        nums=sorted(nums)
        for i in range(len(nums)):
            val=nums[i]%3
            dic[val].append(nums[i])
        # print(dic,suma,objetivo)
        len1=len(dic[1])
        len2=len(dic[2])
        if dic[objetivo]!=[]:
            if objetivo==1 and len2>0:
                if len2>1:
                    return suma-min(dic[1][0],dic[2][0]+dic[2][1])
            if objetivo==2 and len1>1:
                return suma-min(dic[2][0],dic[1][0]+dic[1][1])
            return suma-dic[objetivo][0]
        else:
            if objetivo==2 and len1>1:
                return suma-dic[1][0]-dic[1][1]
            if objetivo==1 and len2>1:
                return suma-dic[2][0]-dic[2][1]
        return 0    
