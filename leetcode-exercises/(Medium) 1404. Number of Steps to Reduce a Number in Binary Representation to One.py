# 1404. Number of Steps to Reduce a Number in Binary Representation to One
# Solved
# Medium • 1246
# Topics
# premium lock icon
# Companies
# Hint
# Geico
# Given the binary representation of an integer as a string s, return the number of steps to reduce it to 1 under the following rules:

# If the current number is even, you have to divide it by 2.

# If the current number is odd, you have to add 1 to it.

# It is guaranteed that you can always reach one for all test cases.


class Solution:
    def numSteps(self, s: str) -> int:
        aux=s[::-1]
        conteo=0
        while aux!="1":
            conteo+=1
            if aux[0]=="1":
                if "0" in aux:
                    index=aux.find("0") 
                    aux="0" *(index)+"1"+aux[index+1:]
                else:
                    aux="0" *(len(aux))+"1"
            else:
                aux=aux[1:]
            # print(aux)
        return conteo