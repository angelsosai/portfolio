# You are given a 2D array points of size n x 2 representing integer coordinates of some points on a 2D plane, where points[i] = [xi, yi].

# Count the number of pairs of points (A, B), where

# A is on the upper left side of B, and
# there are no other points in the rectangle (or line) they make (including the border).
# Return the count.
class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        tam=len(points)
        dic={}
        points=sorted(points)
        for i in points:
            if i[0] in dic: 
                dic[i[0]].append(i)
            else:
                dic[i[0]]=[i]
        res=0
        for i in range(tam-1):
            for j in range(i+1,tam):
                res+=1
                if points[i][1]<points[j][1] and points[i][0]!=points[j][0]:
                    res-=1
                    continue
                aux=0
                for k in range(points[i][0],points[j][0]+1):
                    if  k in dic:
                        for m in dic[k]:
                            if ((points[j][1]<=m[1]) and(m[1]<=points[i][1])) or ((points[j][1]>=m[1]) and(m[1]>=points[i][1])):
                                aux+=1
                            if aux>2:
                                res-=1
                                break
                    if  aux>2:
                        break

        return res