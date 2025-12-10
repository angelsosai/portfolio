# Given an array nums of n integers and an integer k, determine whether there exist two adjacent subarrays of length k such that both subarrays are strictly increasing. Specifically, check if there are two subarrays starting at indices a and b (a < b), where:

# Both subarrays nums[a..a + k - 1] and nums[b..b + k - 1] are strictly increasing.
# The subarrays must be adjacent, meaning b = a + k.
# Return true if it is possible to find two such subarrays, and false otherwise.


class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        contador=0
        aux=False
        if k==1:
            if len(nums)>1:
                return True
            else:
                return False
        for i in range(1,len(nums)):
            # print(contador)
            if nums[i-1]<nums[i]:
                contador+=1
            else:
                if contador>=k-1:
                    aux=True
                else:
                    aux=False
                contador=0
            if contador==2*k-1:
                return True
            if aux and contador>=k-1:
                return True
            # print(contador,aux)
        return False