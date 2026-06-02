
# Code
# Code Sample
# Code Sample
# Testcase
# Test Result
# Test Result
# 3546. Equal Sum Grid Partition I
# Solved
# Medium - null
# Topics
# premium lock icon
# Companies
# Hint
# You are given an m x n matrix grid of positive integers. Your task is to determine if it is possible to make either one horizontal or one vertical cut on the grid such that:

# Each of the two resulting sections formed by the cut is non-empty.
# The sum of the elements in both sections is equal.
# Return true if such a partition exists; otherwise return false.


class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        dic_columnas={}
        dic_filas={}
        suma_total=0
        filas=len(grid[0])
        for i in range(len(grid)):
            suma_aux=0
            for j in range(filas):
                if j in dic_filas:
                    dic_filas[j]+=grid[i][j]
                else:
                    dic_filas[j]=grid[i][j]
                suma_aux+=grid[i][j]
                suma_total+=grid[i][j]
            if i in dic_columnas:
                dic_columnas[i]+=suma_aux
            else:
                dic_columnas[i]=suma_aux
        aux=0
        for i in dic_columnas:
            aux+=dic_columnas[i]
            if aux==(suma_total-aux):
                return True
        aux=0
        for i in dic_filas:
            aux+=dic_filas[i]
            # print(aux)
            if aux==(suma_total-aux):
                return True
        return False
                