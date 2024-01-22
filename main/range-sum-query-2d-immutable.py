class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        rows, cols = len(matrix), len(matrix[0])
        presum = [[0 for _ in range(cols+1)] for _ in range(rows+1)]
        for i in range(rows):
            for j in range(cols):
                presum[i+1][j+1] = presum[i+1][j] + presum[i][j+1] - presum[i][j] + matrix[i][j]
        self.presum = presum
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.presum[row2+1][col2+1] - self.presum[row1][col2+1] - self.presum[row2+1][col1] + self.presum[row1][col1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)