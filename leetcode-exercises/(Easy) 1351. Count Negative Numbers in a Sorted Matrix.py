# 1351. Count Negative Numbers in a Sorted Matrix
# Solved
# Easy - 619
# Topics
# premium lock icon
# Companies
# Hint
# Given a m x n matrix grid which is sorted in non-increasing order both row-wise and column-wise, return the number of negative numbers in grid.

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        n=len(grid)
        m=len(grid[0])
        conteo=0
        res=n
        ind=m-1
        for i in range(n):
            if grid[i][0]<0:
                break
            res-=1
            while grid[i][ind]<0 :
                ind-=1
            conteo+=m-ind-1
            # print(i,conteo,ind)
        conteo+=res*m
        return conteo