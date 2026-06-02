# 1356. Sort Integers by The Number of 1 Bits
# Solved
# Easy • 829
# Topics
# premium lock icon
# Companies
# Hint
# J.P. Morgan
# Accenture
# You are given an integer array arr. Sort the integers in the array in ascending order by the number of 1's in their binary representation and in case of two or more integers have the same number of 1's you have to sort them in ascending order.

# Return the array after sorting it.

class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        dic={}
        for i in arr:
            val=i.bit_count()
            if  val not in dic:
                dic[val]=[i]
            else:
                dic[val].append(i)
        lista=[]
        # print(len(dic),dic)
        for j in sorted(dic.keys()):
            lista=lista+sorted(dic[j])
        return lista
