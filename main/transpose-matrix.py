class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        transpose = []
        for j in range(len(matrix[0])):
            transpose.append([])
            for i in range(len(matrix)):
                transpose[j].append(matrix[i][j])
        return transpose