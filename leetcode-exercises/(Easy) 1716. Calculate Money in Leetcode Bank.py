# Hercy wants to save money for his first car. He puts money in the Leetcode bank every day.

# He starts by putting in $1 on Monday, the first day. Every day from Tuesday to Sunday, he will put in $1 more than the day before. On every subsequent Monday, he will put in $1 more than the previous Monday.

# Given n, return the total amount of money he will have in the Leetcode bank at the end of the nth day.


class Solution:
    def totalMoney(self, n: int) -> int:
        itera=n//7
        suma=0
        cons=28
        resta=0
        for i in range(itera):
             suma+=cons
             cons-=(i+1)
             cons+=(i+8)
            #  print(suma)
        res=n%7
        # print(res,itera)
        suma+=int(((res+itera)+1)*(res+itera)/2-((itera)+1)*(itera)/2)
        return suma