
# 2840. Check if Strings Can be Made Equal With Operations II
# Solved
# Medium - 1357
# Topics
# premium lock icon
# Companies
# Hint
# You are given two strings s1 and s2, both of length n, consisting of lowercase English letters.

# You can apply the following operation on any of the two strings any number of times:

# Choose any two indices i and j such that i < j and the difference j - i is even, then swap the two characters at those indices in the string.
# Return true if you can make the strings s1 and s2 equal, and false otherwise.

 
class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        dic={
            "s1":
                {"bolsa_impar":[],
                "bolsa_par":[]},         
            "s2":
                {"bolsa_impar":[],
                "bolsa_par":[]}

        }
        for i in range(len(s1)):
            if i%2==0:
                dic["s1"]["bolsa_impar"].append(s1[i])
                dic["s2"]["bolsa_impar"].append(s2[i])
            else:
                dic["s1"]["bolsa_par"].append(s1[i])
                dic["s2"]["bolsa_par"].append(s2[i])
        return sorted(dic["s1"]["bolsa_impar"])==sorted(dic["s2"]["bolsa_impar"]) and sorted(dic["s1"]["bolsa_par"])==sorted(dic["s2"]["bolsa_par"]) 