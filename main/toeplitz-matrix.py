class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        # check from row
        for i in range(len(matrix[0])):
            num = matrix[0][i]
            for j in range(1, min(len(matrix), len(matrix[0]) - i)):
                if matrix[j][i+j] != num:
                    return False
        
        # check from col
        for i in range(len(matrix)):
            num = matrix[i][0]
            for j in range(1, min(len(matrix)-i, len(matrix[0]))):
                if matrix[i+j][j] != num:
                    return False
        
        return True
