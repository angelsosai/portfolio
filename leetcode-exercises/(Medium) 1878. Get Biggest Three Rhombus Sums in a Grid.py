
# You are given an m x n integer matrix grid​​​.

# A rhombus sum is the sum of the elements that form the border of a regular rhombus shape in grid​​​. The rhombus must have the shape of a square rotated 45 degrees with each of the corners centered in a grid cell. Below is an image of four valid rhombus shapes with the corresponding colored cells that should be included in each rhombus sum:

class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        x=len(grid)
        y=len(grid[0])
        set_=set()
        def suma_r(m,n,lon):
            suma=grid[m][n]
            # print(m,n,suma,lon)
            suma+=grid[m+lon][n+lon]
            suma+=grid[m+lon][n-lon]
            suma+=grid[m+2*lon][n]
            # print(suma)
            for i in range(1,lon):
                suma+=grid[m+i][n+i]
                # print(suma,grid[m+i][n+i])
                suma+=grid[m+i][n-i]
                suma+=grid[m+2*lon-i][n-i]
                suma+=grid[m+2*lon-i][n+i]
                # print(suma)
            return suma
        for i in range(x):
            for j in range(y):
                set_.add(grid[i][j])
                minimo_x=min(j,y-j-1)
                minimo_y=(x-1-i)//2
                # print(grid[i][j],min(minimo_x,minimo_y))
                tam=min(minimo_x,minimo_y)
                # print(i,j,tam,minimo_x,minimo_y)
                if tam>=1:
                    # print("---------")
                    # print(tam)
                    for kl in range(1,tam+1):
                        # print(i,j,suma_r(i,j,kl))
                        set_.add(suma_r(i,j,kl))
        return sorted(set_, reverse=True)[0:3] 