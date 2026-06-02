# 2033. Minimum Operations to Make a Uni-Value Grid
# Solved
# Medium - 1661
# Topics
# premium lock icon
# Companies
# Hint
# EPAM Systems
# You are given a 2D integer grid of size m x n and an integer x. In one operation, you can add x to or subtract x from any element in the grid.

# A uni-value grid is a grid where all the elements of it are equal.

# Return the minimum number of operations to make the grid uni-value. If it is not possible, return -1.


class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        n = len(grid)
        m = len(grid[0])
        if n == 1 and m == 1:
            return 0
        arr = []
        for i in range(n):
            for j in range(m):
                arr.append(grid[i][j])
        arr.sort()
        mid = arr[(n * m) // 2]
        ans = 0
        for i in range(n):
            for j in range(m):
                if (mid - grid[i][j]) % x != 0:
                    return -1
                ans += abs(mid - grid[i][j]) // x
        return ans