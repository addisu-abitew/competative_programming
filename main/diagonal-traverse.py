class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        i = j = 0
        diag = []
        diag_sum = 0
        m, n = len(mat), len(mat[0])
        while diag_sum < m+n-1:
            
            if diag_sum%2 == 0:
                while i>0 and j+1<n:
                    diag.append(mat[i][j])
                    i -= 1
                    j += 1
                diag.append(mat[i][j])
                if j+1==n:
                    i += 1
                else:
                    j += 1
            else:
                while j>0 and i+1<m:
                    diag.append(mat[i][j])
                    j -= 1
                    i += 1
                diag.append(mat[i][j])
                if i+1==m:
                    j += 1
                else:
                    i += 1
            diag_sum += 1
        return diag