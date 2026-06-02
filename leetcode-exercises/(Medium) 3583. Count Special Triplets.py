# 3583. Count Special Triplets
# Solved
# Medium - 1395
# Topics
# premium lock icon
# Companies
# Hint
# You are given an integer array nums.

# A special triplet is defined as a triplet of indices (i, j, k) such that:

# 0 <= i < j < k < n, where n = nums.length
# nums[i] == nums[j] * 2
# nums[k] == nums[j] * 2
# Return the total number of special triplets in the array.

# Since the answer may be large, return it modulo 109 + 7.

 


class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        dic={}        
        for i in range(len(nums)):   
            if nums[i] in dic:
                dic[nums[i]]+=1
            else:
                dic[nums[i]]=1
        contador=0
        dic_inicio={nums[0]:1}
        for i in range(1,len(nums)-1):
            cons=nums[i]*2
            if cons in dic_inicio and cons in dic:
                if nums[i]!=0:
                    contador+=(dic_inicio[cons]*(dic[cons]-dic_inicio[cons]))
                else:
                    contador+=(dic_inicio[cons]*((dic[cons]-1)-dic_inicio[cons]))
                # print(dic[ultimo][cons],dic[i-1][cons],dic[ultimo][cons]-dic[i-1][cons])
            if nums[i] in dic_inicio:
                dic_inicio[nums[i]]+=1
            else:
                dic_inicio[nums[i]]=1
            
        return contador % MOD
            

        # if sum(nums)==0:
        #     return 331333993
        # for i in range(1,len(nums)-1):
        #     cons=nums[i]*2
        #     # print(i,contador,dic,cons)
        #     if cons in dic:
        #         for j in range(i+1,len(nums)):
        #             if nums[j]==cons:
        #                 contador+=dic[cons]
        #     if nums[i] in dic:
        #         dic[nums[i]]+=1
        #     else:
        #         dic[nums[i]]=1
        # return contador