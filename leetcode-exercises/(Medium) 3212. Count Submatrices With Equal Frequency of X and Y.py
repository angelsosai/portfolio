
# Given a 2D character matrix grid, where grid[i][j] is either 'X', 'Y', or '.', return the number of submatrices that contain:

# grid[0][0]
# an equal frequency of 'X' and 'Y'.
# at least one 'X'.
 






from collections import defaultdict
class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        suma=0
        dic={
            "X":0,
            "Y":0,
            ".":0
        }
        dic_indice = {
            0:[0,0]
        }
        matriz=0
        for i in range(len(grid)):
            dic["X"]=0
            dic["Y"]=0
            for j in range(len(grid[0])):
                if grid[i][j]=="X":
                    if j in dic_indice: 
                        dic_indice[j][0]+=1
                    else:
                        dic_indice[j]=[1,0]
                if grid[i][j]=="Y":
                    if j in dic_indice: 
                        dic_indice[j][1]+=1
                    else:
                        dic_indice[j]=[0,1]
                else:
                    if j not in dic_indice:
                        dic_indice[j]=[0,0]

                dic["X"]+=dic_indice[j][0]
                dic["Y"]+=dic_indice[j][1]
                # print(i,j,dic["X"],dic["Y"],dic_indice[j])
                if dic["X"]>0 and dic["X"]-dic["Y"]==0:
                    matriz+=1
                
        return matriz
                