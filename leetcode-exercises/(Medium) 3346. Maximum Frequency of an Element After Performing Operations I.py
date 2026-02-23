# You are given an integer array nums and two integers k and numOperations.

# You must perform an operation numOperations times on nums, where in each operation you:

# Select an index i that was not selected in any previous operations.
# Add an integer in the range [-k, k] to nums[i].
# Return the maximum possible frequency of any element in nums after performing the operations.
import numpy as np
class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        dic=Counter(nums)
        aux=0
        maxi=max(list(dic.values()))
        mini=min(list(dic.keys()))
        max_=max(list(dic.keys()))+1
        nums=np.array(nums)

        for i in range(mini,max_):
            # print(i)
            aux=nums-i
            # print(i,nums,aux,dic[i])
            # print(aux[(aux<=k)&(0<aux)],len(aux[(aux<=k)&(0<aux)]))
            # print(aux[(aux>=-k)&(0>aux)])
            ax=len(aux[(aux<=k)&(0<aux)])
            if ax>numOperations:
                op=numOperations
            else:
                op=min(ax+len(aux[(aux>=-k)&(0>aux)]),numOperations)
            # print(op)
            res=op+dic[i]
            # print(res)
            if maxi<res:
                maxi=res
        return maxi