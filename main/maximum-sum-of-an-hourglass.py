class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        max_sum = 0
        rows, cols = len(grid), len(grid[0])
        for i in range(rows-2):
            for j in range(cols-2):
                cur_sum = grid[i+1][j+1]
                for k in range(3):
                    cur_sum += grid[i][j+k] + grid[i+2][j+k]
                max_sum = max(max_sum, cur_sum)
        return max_sum