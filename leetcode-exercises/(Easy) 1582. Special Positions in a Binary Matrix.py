# 1582. Special Positions in a Binary Matrix
# Solved
# Easy • 529
# Topics
# premium lock icon
# Companies
# Hint
# Given an m x n binary matrix mat, return the number of special positions in mat.

# A position (i, j) is called special if mat[i][j] == 1 and all other elements in row i and column j are 0 (rows and columns are 0-indexed).



class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        filas={}
        mat_=[[0 for _ in range(len(mat))] for _ in range(len(mat[0]))]
        for i,val in enumerate(mat):
            for j,val_2 in enumerate(val):
                mat_[j][i]=mat[i][j]
        conteo=0
        # print(mat_)
        for i,val in enumerate(mat):
            # print(val)
            if sum(val)==1:
                for j,val_2 in enumerate(val):
                    if val_2==1:
                        # print(val_2,mat_[j])
                        if sum(mat_[j])==1:
                            conteo+=1          
        return conteo


        
