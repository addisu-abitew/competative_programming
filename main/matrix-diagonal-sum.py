class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        diag_sum = 0
        for i in range(n):
            diag_sum += mat[i][i] + mat[i][n-i-1]
        if n%2:
            mid = n//2
            diag_sum -= mat[mid][mid]
        return diag_sum