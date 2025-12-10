# Given an array nums of n integers, your task is to find the maximum value of k for which there exist two adjacent subarrays of length k each, such that both subarrays are strictly increasing. Specifically, check if there are two subarrays of length k starting at indices a and b (a < b), where:

# Both subarrays nums[a..a + k - 1] and nums[b..b + k - 1] are strictly increasing.
# The subarrays must be adjacent, meaning b = a + k.
# Return the maximum possible value of k.

# A subarray is a contiguous non-empty sequence of elements within an array.


class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        contador=1
        aux=False
        aux_2=False
        tam=len(nums)
        contador_1=0
        maximo=1
        if tam==1:
            return 0
        if tam==2:
            return 1
        for i in range(1,len(nums)):
            # print(contador,nums[i])
            if nums[i-1]<nums[i]:
                contador+=1
                aux=True
            else:
                maximo=max(maximo,contador//2)
                # print(maximo,nums[i],contador,contador_1)
                if aux and aux_2:
                    maximo=max(maximo,min(contador,contador_1))
                aux_2=aux
                contador_1=contador
                contador=1
                aux=False
        if aux and aux_2:
            maximo=max(maximo,min(contador,contador_1))
                
        # print(maximo,contador)
        maximo=max(maximo,contador//2)
            # print(contador,aux)
        return maximo