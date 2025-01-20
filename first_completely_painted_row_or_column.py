from typing import List
# 2661. First Completely Painted Row or Column
# Medium

# You are given a 0-indexed integer array arr, and an m x n integer matrix mat. arr and mat both contain all the integers in the range [1, m * n].
# Go through each index i in arr starting from index 0 and paint the cell in mat containing the integer arr[i].
# Return the smallest index i at which either a row or a column will be completely painted in mat.
class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        
        pos = {mat[i][j]: (i, j) for i in range(m) for j in range(n)}
        

        print(pos)

        row_count = [0] * m
        col_count = [0] * n

        for i, num in enumerate(arr):
            r, c = pos[num]
            row_count[r] += 1
            col_count[c] += 1

            if row_count[r] == n or col_count[c] == m:
                return i
            
        return -1



