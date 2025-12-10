# 2300. Successful Pairs of Spells and Potions
# Solved
# Medium - 1387
# Topics
# premium lock icon
# Companies
# Hint
# Goldman Sachs
# You are given two positive integer arrays spells and potions, of length n and m respectively, where spells[i] represents the strength of the ith spell and potions[j] represents the strength of the jth potion.

# You are also given an integer success. A spell and potion pair is considered successful if the product of their strengths is at least success.

# Return an integer array pairs of length n where pairs[i] is the number of potions that will form a successful pair with the ith spell.







import numpy as np
class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        lista=np.array(potions)
        r=len(spells)*[0]
        d=0
        dic={}
        for i in spells:
            # t=i*lista
            # print(t,t[t>=success],success)
            if i in dic:
                r[d]=dic[i]
            else:
                m=len(lista[lista>=(success/i)])
                r[d]=m
                dic[i]=m
            d+=1
        return r