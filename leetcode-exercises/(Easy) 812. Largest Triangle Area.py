

# Given an array of points on the X-Y plane points where points[i] = [xi, yi],
# return the area of the largest triangle that can be formed by any three different points. Answers within 10-5 of the actual answer will be accepted

class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        tam=len(points)
        
        maximo=0
        for i in range(tam-2):
            for j in range(i+1,tam-1):
                for k in range(j+1,tam):
                    area=(1/2) * abs(points[i][0] * (points[j][1] - points[k][1]) + points[j][0] * (points[k][1] - points[i][1]) + points[k][0]* (points[i][1] - points[j][1]))
                    if area>maximo:
                        maximo=area
        return maximo