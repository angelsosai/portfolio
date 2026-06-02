# 2946. Matrix Similarity After Cyclic Shifts
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# You are given an m x n integer matrix mat and an integer k. The matrix rows are 0-indexed.

# The following proccess happens k times:

# Even-indexed rows (0, 2, 4, ...) are cyclically shifted to the left.


# Odd-indexed rows (1, 3, 5, ...) are cyclically shifted to the right.


# Return true if the final modified matrix after k steps is identical to the original matrix, and false otherwise.

 

class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        v=len(mat[0])
        modulo=k%v
        if modulo==0:
            return True
        new_matrix=[]
        ind=1
        for i in mat:
            if ind==1:
                new_matrix.append(i[modulo:]+i[:modulo])
            else:
                new_matrix.append(i[v-modulo:]+i[:v-modulo])
            ind=ind*-1
        # print(new_matrix,modulo)
        return new_matrix==mat
        